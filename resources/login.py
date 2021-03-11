import json
from flask_restful import Resource
from flask import request
from flask_api import status
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt
import db
from model.app_response import AppResponse, ResponseEncoder, AppErrorResponse
from datetime import timedelta, datetime


class Login(Resource):

    def post(self):
        data = request.get_json()
        user = db.authenticate(data['username'], data['password']).__dict__
        del user['password']
        
        access_token = create_access_token(identity=user, expires_delta=timedelta(seconds=10))

        return {'access_token': access_token}, 200

class Protected(Resource):

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        claims = get_jwt()
        return { 'user': current_user, 'exp': claims['exp']}, 200