import pytest
from godaddy_python import Client, Config
from godaddy_python.errors import NotFoundException, RateLimitException, ServerException, UnauthorizedException, ValidationException
from godaddy_python.http import HttpResponse
from tests.support import TestTransport

def make_client(transport):
    return Client(Config(api_key="key", api_secret="secret", max_retries=0), transport)

def test_maps_400_to_validation():
    t = TestTransport(); t.push(HttpResponse(400, {"content-type": "application/json"}, "{}"))
    with pytest.raises(ValidationException): make_client(t).abuse().get_tickets()

def test_maps_401_to_unauthorized():
    t = TestTransport(); t.push(HttpResponse(401, {"content-type": "application/json"}, "{}"))
    with pytest.raises(UnauthorizedException): make_client(t).abuse().get_tickets()

def test_maps_404_to_not_found():
    t = TestTransport(); t.push(HttpResponse(404, {"content-type": "application/json"}, "{}"))
    with pytest.raises(NotFoundException): make_client(t).abuse().get_tickets()

def test_maps_429_to_rate_limit():
    t = TestTransport(); t.push(HttpResponse(429, {"content-type": "application/json"}, "{}"))
    with pytest.raises(RateLimitException): make_client(t).abuse().get_tickets()

def test_maps_500_to_server():
    t = TestTransport(); t.push(HttpResponse(500, {"content-type": "application/json"}, "{}"))
    with pytest.raises(ServerException): make_client(t).abuse().get_tickets()
