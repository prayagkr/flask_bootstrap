from json import JSONEncoder
from typing import List


class AppResponse:
    def __init__(self, body=None, code: int = 2000, message: str = 'Operation Successful', status: bool = True):
        self.body = body
        self.code = code
        self.message = message
        self.status = status


class AppErrorResponse:
    def __init__(self, errors=None, code: int = 5000, message: str = 'Operation Failed', status: bool = False):
        self.errors = errors
        self.code = code
        self.message = message
        self.status = status


class ListResponse:
    def __init__(self, data: List):
        self.data = data
        self.count = len(data)


class ResponseEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
