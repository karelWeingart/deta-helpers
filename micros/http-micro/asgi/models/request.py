from dataclasses import dataclass
from typing import List, Dict


def _parse_headers(headers: List) -> Dict:
    ret = {header[0].decode("utf-8"): header[1].decode("utf-8") for header in headers}
    return ret


@dataclass(init=False)
class Request:
    scheme: str
    method: str
    path: str
    query_string: bytes
    raw_headers: List
    raw_body: bytes
    body: str
    dict_body: dict
    path_parameters: Dict

    def __init__(self, scope: dict) -> None:
        self.scheme = scope['scheme']
        self.method = scope['method']
        self.path = scope['path']
        self.query_string = scope['query_string']
        self.raw_headers = scope['headers']
        self.headers = _parse_headers(self.raw_headers)
        self.body = ""
        self.raw_body = b''
        self.dict_body = {}
        self.path_parameters = dict()
