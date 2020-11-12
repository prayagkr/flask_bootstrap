from flask_restful import Resource


class Validate(Resource):

    def get(self):
        reseponse = {'status': 'operation successfull'}
        return reseponse, 200