"""request module"""
from dataclasses import dataclass
from typing import List, Dict


def _parse_headers(headers: List) -> Dict:
    ret = {header[0].decode("utf-8"): header[1].decode("utf-8") for header in headers}
    return ret


@dataclass(init=False)
class Request:
    """request class - request object is passed to implemented controller methods."""
    scheme: str
    method: str
    path: str
    query_string: bytes
    raw_headers: List
    body: str
    dict_body: dict
    path_parameters: Dict

    def __init__(self, scope: dict) -> None:
        self.scheme = scope['scheme']
        self.method = scope['method']
        self.path = scope['path']
        self.query_string = scope['query_string']
        self.headers = _parse_headers(scope['headers'])
        self.body = ""
        self.raw_body = b''
        self.dict_body = {}
        self.path_parameters = {}
