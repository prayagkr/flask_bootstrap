from flask import Flask
from flask_jwt_extended import JWTManager
from flask_api import status


def register_jwt(app: Flask) -> None:
    
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['PROPAGATE_EXCEPTIONS'] = True

    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def my_expired_token_callback(jwt_header, jwt_payload):
        return {"message": "Session has expired"}, status.HTTP_401_UNAUTHORIZED


