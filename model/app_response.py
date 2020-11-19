from json import JSONEncoder
from typing import List

class AppResponse:
    def __init__(self, data=None, code: int =2000, message: str ='Operation Successfull', status: bool =True):
        self.data = data
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