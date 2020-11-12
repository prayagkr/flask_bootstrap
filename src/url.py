from resource.validate import Validate
from resource.math_resource import MathResource


def api_url(api):
    api.add_resource(Validate, '/validate')  
    api.add_resource(MathResource, '/math')