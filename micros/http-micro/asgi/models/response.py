from typing import Callable, List, Tuple, Generator
import json
from dataclasses import asdict, is_dataclass
from asgi.utils.media_types import get_media_type
from asgi.models.request import Request


class Response:

    def __init__(self, send: Callable, request: Request) -> None:
        self._send = send
        self._status = 200
        self.headers = {}
        self._request = request
        self.headers['content-type'] = get_media_type(request.path)

    async def send(self, body: str, more_body=False):
        await self._send_headers()
        await self._send_body(body, more_body)

    async def send_chunks(self, generator: Generator):
        await self._send_headers()
        current_chunk = next(generator)
        next_chunk = None
        more_body = True
        while more_body:
            try:
                next_chunk = next(generator)
            except StopIteration:
                more_body = False
            finally:
                await self._send_body(current_chunk, more_body)
                current_chunk = next_chunk

    async def send_json(self, data: dict):
        self.headers['content-type'] = "application/json"
        await self.send(json.dumps(data))

    async def redirect(self, path: str, code: int = 302):
        self.headers['Location'] = path
        await self._send_headers(status=code)
        await self.send("")

    def get_headers(self) -> List[Tuple[bytes, bytes]]:
        return [
            (k.encode("utf-8"), v.encode("utf-8"))
            for k, v in self.headers.items()
        ]

    async def _send_body(self, body: str, more_body=False):
        await self._send({
            'type': 'http.response.body',
            'body': body if type(body) == bytes else body.encode("utf-8"),
            'more_body': more_body,
        })

    async def _send_headers(self, status=200) -> None:
        await self._send({
            'type': 'http.response.start',
            'status': status,
            'headers': self.get_headers(),
        })


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)
