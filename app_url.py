from resource.validate import Validate
from resource.math_resource import MathResource
from resource.test_response import TestResponse


def api_url(api):
    api.add_resource(Validate, '/validate')  
    api.add_resource(MathResource, '/math')
    api.add_resource(TestResponse, '/test-response')