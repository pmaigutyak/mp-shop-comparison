
from comparison.service import Comparison


class ComparisonMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        request.comparison = Comparison(request.session)

        return self.get_response(request)
