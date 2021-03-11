from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from routes.app_url import api_url
# import prometheus
from flask_jwt_extended import create_access_token, get_jwt_identity, get_jwt, set_access_cookies
from datetime import datetime, timezone, timedelta
from flask_jwt.jwt_manager import register_jwt
from exception.register_error_handler import register_error_handler


app = Flask(__name__)
api = Api(app)
api_url(api)

CORS(app)

register_jwt(app)
register_error_handler(app)



# @app.after_request
# def refresh_expiring_jwts(response):
#     try:
#         exp_timestamp = get_jwt()["exp"]
#         now = datetime.now(timezone.utc)
#         target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
#         if target_timestamp > exp_timestamp:
#             access_token = create_access_token(identity=get_jwt_identity(), expires_delta=timedelta(seconds=10))
#             set_access_cookies(response, access_token)
#         return response
#     except (RuntimeError, KeyError):
#         # Case where there is not a valid JWT. Just return the original respone
#         return response

if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
