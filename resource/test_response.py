from flask_restful import Resource
from model.app_response import AppResponse, ResponseEncoder, ListResponse
import json

class Pen:
    def __init__(self, message):
        self.message = message

class Message:
    def __init__(self, data):
        self.data = data


class TestResponse(Resource):

    def get(self):
        """
        Example of response where data is of type Object i.e instance of Class
        """
        message = Message('Test Message')
        pen = Pen(message)

        app_response = AppResponse(pen)
        response = ResponseEncoder().encode(app_response)
        return json.loads(response), 200

    def delete(self):
        """
        Example of response where data is of type List
        """
        records = ['One', 'Two', 'Three']
        list_response = ListResponse(records)
        app_response = AppResponse(list_response)
        response = ResponseEncoder().encode(app_response)
        return json.loads(response), 200