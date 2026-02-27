from godaddy.http import HttpResponse

class TestTransport:
    def __init__(self):
        self.requests = []
        self.responses = []

    def push(self, response):
        self.responses.append(response)

    def send(self, request):
        self.requests.append(request)
        if self.responses:
            return self.responses.pop(0)
        return HttpResponse(200, {"content-type": "application/json"}, "{}")
