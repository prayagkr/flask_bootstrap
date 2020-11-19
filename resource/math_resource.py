from flask_restful import Resource
from flask import request
from model.app_response import AppResponse, ResponseEncoder
import json

class MathResource(Resource):

    def get(self):
        app_response = AppResponse()
        response = ResponseEncoder().encode(app_response)
        return json.loads(response), 200

    def post(self):
        data = request.get_json()
        a = data['a']
        b = data['b']
        total = a + b
        result = {'result': total}

        app_response = AppResponse(result)
        response = ResponseEncoder().encode(app_response)
        return json.loads(response), 201


