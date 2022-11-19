"""implementation of asgi interface"""
import json
from typing import Callable

from asgi.base_request_handler import BaseRequestHandler
from asgi.matchers.matcher import match_path
from asgi.models.request import Request
from asgi.models.response import Response


class RequestHandler(BaseRequestHandler):
    """implementation of asgi interface"""

    async def __call__(self, scope, receive, send):
        if scope['type'] == "http":
            request = Request(scope)
            response = Response(send, request)
            await self.__receive_body__(receive, request)
            is_matched, matched_path, path_parameters = \
                match_path(self._app_methods[scope['method']], scope['path'])
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
        if 'content-type' in request.headers and \
                request.headers['content-type'] == "application/json":
            request.dict_body = json.loads(request.body)
