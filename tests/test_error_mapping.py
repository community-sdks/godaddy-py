import pytest

from godaddy import Client, Config
from godaddy.dto.abuse.requests import GetTicketsRequest
from godaddy.errors import AbuseBadRequestException, AbuseNotFoundException, AbuseRateLimitException, AbuseServerException, AbuseUnauthorizedException
from godaddy.http import HttpResponse
from tests.support import TestTransport


def make_client(transport):
    return Client(Config(api_key="key", api_secret="secret", max_retries=0), transport)


def test_maps_400_to_service_bad_request():
    t = TestTransport()
    t.push(HttpResponse(400, {"content-type": "application/json"}, "{}"))
    with pytest.raises(AbuseBadRequestException):
        make_client(t).abuse().get_tickets(GetTicketsRequest())


def test_maps_401_to_service_unauthorized():
    t = TestTransport()
    t.push(HttpResponse(401, {"content-type": "application/json"}, "{}"))
    with pytest.raises(AbuseUnauthorizedException):
        make_client(t).abuse().get_tickets(GetTicketsRequest())


def test_maps_404_to_service_not_found():
    t = TestTransport()
    t.push(HttpResponse(404, {"content-type": "application/json"}, "{}"))
    with pytest.raises(AbuseNotFoundException):
        make_client(t).abuse().get_tickets(GetTicketsRequest())


def test_maps_429_to_service_rate_limit():
    t = TestTransport()
    t.push(HttpResponse(429, {"content-type": "application/json"}, "{}"))
    with pytest.raises(AbuseRateLimitException):
        make_client(t).abuse().get_tickets(GetTicketsRequest())


def test_maps_500_to_service_server():
    t = TestTransport()
    t.push(HttpResponse(500, {"content-type": "application/json"}, "{}"))
    with pytest.raises(AbuseServerException):
        make_client(t).abuse().get_tickets(GetTicketsRequest())