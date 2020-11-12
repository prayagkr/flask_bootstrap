from flask_restful import Resource
from flask import request

class MathResource(Resource):

    def get(self):
        reseponse = {'status': 'operation successfull'}
        return reseponse, 200

    def post(self):
        data = request.get_json()
        a = data['a']
        b = data['b']
        res = a + b
        
        reseponse = {'result': res}
        return reseponse, 201


