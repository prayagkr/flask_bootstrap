import time
from flask import request, Flask
from flask_restful import Api
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_flask_exporter import RESTfulPrometheusMetrics, PrometheusMetrics

def integreate_prometheus(app: Flask):
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })

def integrate_prometheus_metrics(app: Flask, restful_api: Api):
    # metrics = RESTfulPrometheusMetrics(app, restful_api)
    metrics = PrometheusMetrics(app)
    metrics.info('app_info', 'Application info', version='1.0.3')

    metrics.register_default(
        metrics.summary(
            'by_path_method_time_stamp_summary', 'Request summary by request paths, method, timestamp',
            labels={
                'path': lambda: request.path,
                'method': lambda: request.method,
                'status': lambda r: r.status_code,
                'time_stamp': lambda: time.time()
            }
        )
    )
    
    return metrics