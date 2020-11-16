from flask import request, Flask
from flask_cors import CORS
from flask_restful import Api
from app_url import api_url


app = Flask(__name__)
api = Api(app)
api_url(api)

CORS(app)



if __name__ == '__main__':
    app.run('127.0.0.1', 12000)
