from flask_restful import Resource
from flask_api import status
from model.app_response import AppResponse, ResponseEncoder
import json


class Validate(Resource):

    def get(self):
        """
        Example of Api to check if app is up and running.
        """
        app_response = AppResponse('Validate')
        response = ResponseEncoder().encode(app_response)
        return json.loads(response), status.HTTP_200_OK
