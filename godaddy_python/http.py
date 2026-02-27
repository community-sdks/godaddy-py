import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple
import requests

@dataclass
class HttpRequest:
    method: str
    url: str
    headers: Dict[str, str]
    query: List[Tuple[str, str]] = field(default_factory=list)
    body: Any = None
    timeout: float = 30.0

    def full_url(self):
        if not self.query:
            return self.url
        from urllib.parse import urlencode
        return f"{self.url}?{urlencode(self.query)}"

@dataclass
class HttpResponse:
    status_code: int
    headers: Dict[str, str]
    body: str

class RequestsTransport:
    def __init__(self, session=None):
        self.session = session or requests.Session()

    def send(self, request: HttpRequest):
        response = self.session.request(request.method, request.url, params=request.query, headers=request.headers, json=request.body, timeout=request.timeout)
        return HttpResponse(response.status_code, dict(response.headers), response.text)
