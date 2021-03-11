from flask import Flask
from jwt.exceptions import ExpiredSignatureError
from flask_api import status


def register_error_handler(app: Flask) -> None:

    @app.errorhandler(ExpiredSignatureError)
    def handle_expired_error(e):
        return {'message': 'Session has expired'}, status.HTTP_401_UNAUTHORIZED

