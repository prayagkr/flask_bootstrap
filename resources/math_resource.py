import json
from flask_restful import Resource
from flask import request
from flask_api import status
from model.app_response import AppResponse, ResponseEncoder, AppErrorResponse
from marshmallow import Schema, fields, ValidationError, validates_schema, post_load
from datetime import date, datetime

# Importing custom exception for implementation 
from exception.custom_exception import CommonException, InvalidException
from exception.custom_code import IntenalCode as IC
from exception.custom_message import IntenalMessage as IM

from service.math_service import MathService


def strip_date(data: dict, key: str, fmt="%Y-%m-%d") -> datetime:
    try:
        return datetime.strptime(data[key], fmt)
    except ValueError as err:
        raise ValidationError({key: str(err)})


class MathSchema(Schema):
    """
    Implementing Input validation using marshmallow
    """
    first = fields.Integer(required=True, error_messages={"required": {"message": "first value is missing"}})
    second = fields.Int(required=True)
    name = fields.Str(required=True)
    start_date = fields.String(required=True)
    end_date = fields.String(required=True)

    @post_load
    def parse_date(self, data, **kwargs):
        data['start_date'] = strip_date(data, 'start_date')
        data['end_date'] = strip_date(data, 'end_date')
        return data

    @validates_schema
    def validate_numbers(self, data, **kwargs):
        if data["start_date"] > data["end_date"]:
            raise ValidationError("Start date should not be greater then end date.")


class MathResource(Resource):

    def get(self, id):
        app_response = AppResponse(id)
        response = ResponseEncoder().encode(app_response)
        return json.loads(response), status.HTTP_200_OK

    def post(self):
        try:
            schema = MathSchema()
            parsed_data = schema.load(request.get_json())
            first = parsed_data['first']
            second = parsed_data['second']
            total = first + second
            result = {'result': total}

            app_response = AppResponse(result)
            response = ResponseEncoder().encode(app_response)
            return json.loads(response), status.HTTP_201_CREATED

        except ValidationError as err:
            error_response = AppErrorResponse(code=4040, message=err.messages, status=False)
            response = ResponseEncoder().encode(error_response)
            return json.loads(response), status.HTTP_404_NOT_FOUND

        except Exception as e:
            error_response = AppErrorResponse(code=5000, message="Something went wrong", status=False)
            response = ResponseEncoder().encode(error_response)
            return json.loads(response), status.HTTP_500_INTERNAL_SERVER_ERROR


    def put(self):
        """
        In the put request we will use custom exception and service
        """
        try:
            schema = MathSchema()
            parsed_data: dict = schema.load(request.get_json())
            mathservice: MathService = MathService(parsed_data)
            total = mathservice.calculate()
            result = {'result': total}

            app_response = AppResponse(result)
            response = ResponseEncoder().encode(app_response)
            return json.loads(response), status.HTTP_201_CREATED

        except InvalidException as ex:
            error_response = AppErrorResponse(code=ex.code.value, message=ex.message.value, status=False)
            response = ResponseEncoder().encode(error_response)
            return json.loads(response), status.HTTP_404_NOT_FOUND

        except CommonException as ex:
            error_response = AppErrorResponse(code=ex.code.value, message=ex.message.value, status=False)
            response = ResponseEncoder().encode(error_response)
            return json.loads(response), status.HTTP_404_NOT_FOUND

        except ValidationError as err:
            error_response = AppErrorResponse(code=4040, message=err.messages, status=False)
            response = ResponseEncoder().encode(error_response)
            return json.loads(response), status.HTTP_404_NOT_FOUND

        except Exception as ex:
            print(ex)
            error_response = AppErrorResponse(code=5000, message=str(ex), status=False)
            response = ResponseEncoder().encode(error_response)
            return json.loads(response), status.HTTP_500_INTERNAL_SERVER_ERROR



