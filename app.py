from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from routes.app_url import api_url
# import prometheus


app = Flask(__name__)
api = Api(app)
api_url(api)

CORS(app)

# metrics = prometheus.integrate_prometheus_metrics(app, api)


if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
