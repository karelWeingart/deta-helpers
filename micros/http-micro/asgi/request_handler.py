from asgi.models.response import Response
from asgi.models.request import Request
from matchers.matcher import Matcher
from asgi.base_request_handler import BaseRequestHandler
from typing import Callable
import json


class RequestHandler(BaseRequestHandler):

    def __init__(self) -> None:
        super(RequestHandler, self).__init__()

    async def __call__(self, scope, receive, send):
        if scope['type'] == "http":
            request = Request(scope)
            response = Response(send, request)
            await self.__receive_body__(receive, request)
            is_matched, matched_path, path_parameters = Matcher.match(self._app_methods[scope['method']], scope['path'])
            if is_matched:
                request.path_parameters = path_parameters
                await self._app_methods[scope['method']][matched_path](request, response)
            else:
                raise Exception(f"no controller method found for this request {request}")
        else:
            raise Exception(f"Invalid scope type {scope}")

    async def __receive_body__(self, receive: Callable, request: Request):
        more_body = True
        while more_body:
            message = await receive()
            request.raw_body += message.get('body', b'')
            more_body = message.get('more_body', False)
        request.body = request.raw_body.decode("utf-8")
        if 'content-type' in request.headers and request.headers['content-type'] == "application/json":
            request.dict_body = json.loads(request.body)