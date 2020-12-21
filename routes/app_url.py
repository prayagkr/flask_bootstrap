from resources.validate import Validate
from resources.math_resource import MathResource
from resources.test_response import TestResponse


def api_url(api):
    api.add_resource(Validate, '/validate')  
    api.add_resource(MathResource, '/math/<id>', '/math')
    api.add_resource(TestResponse, '/test-response')
