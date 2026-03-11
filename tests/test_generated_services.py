import importlib
import inspect

from godaddy import Client, Config
from godaddy.http import HttpResponse
from tests.support import TestTransport

SERVICE_NAMES = ["abuse", "aftermarket", "agreements", "ans", "auctions", "certificates", "countries", "domains", "orders", "parking", "shoppers", "subscriptions"]

def _sample_value(annotation):
    text = str(annotation)
    if "bool" in text:
        return True
    if "int" in text:
        return 1
    if "float" in text:
        return 1.0
    if "List" in text or "list" in text:
        return ["value"]
    if "Dict" in text or "dict" in text or "Any" in text:
        return {"key": "value"}
    return "value"

def _build_request(request_cls):
    if not hasattr(request_cls, "__dataclass_fields__"):
        return request_cls()
    kwargs = {}
    for field_name, field_info in request_cls.__dataclass_fields__.items():
        kwargs[field_name] = _sample_value(field_info.type)
    return request_cls(**kwargs)

def _request_class_name(method_name):
    return "".join(part.capitalize() for part in method_name.split("_")) + "Request"

def test_every_service_method_builds_a_request():
    transport = TestTransport()
    client = Client(Config(api_key="key", api_secret="secret", max_retries=0), transport)

    for service_name in SERVICE_NAMES:
        service = getattr(client, service_name)()
        request_module = importlib.import_module(f"godaddy.dto.{service_name}.requests")
        for name, method in inspect.getmembers(service, predicate=inspect.ismethod):
            if name.startswith("_"):
                continue
            request_cls = getattr(request_module, _request_class_name(name), None)
            assert request_cls is not None
            request_obj = _build_request(request_cls)
            transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
            before = len(transport.requests)
            method(request_obj)
            request = transport.requests[before]
            assert request.headers["Authorization"] == "sso-key key:secret"
            assert "{" not in request.url