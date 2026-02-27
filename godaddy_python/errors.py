class ApiException(Exception):
    def __init__(self, message, status_code, response_body, headers, request_method, request_url):
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body
        self.headers = dict(headers)
        self.request_method = request_method
        self.request_url = request_url

    def get_request_id(self):
        return self.headers.get("x-request-id") or self.headers.get("X-Request-Id")

class ValidationException(ApiException): pass
class UnauthorizedException(ApiException): pass
class NotFoundException(ApiException): pass
class RateLimitException(ApiException): pass
class ServerException(ApiException): pass
