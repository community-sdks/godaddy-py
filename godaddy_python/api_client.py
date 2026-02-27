import json
import time
from typing import Any, Iterable, List, Optional, Tuple
from .config import Config
from .errors import ApiException, NotFoundException, RateLimitException, ServerException, UnauthorizedException, ValidationException
from .http import HttpRequest, RequestsTransport

class ApiClient:
    def __init__(self, config: Config, transport=None):
        self._config = config
        self._transport = transport or RequestsTransport()

    @staticmethod
    def build_query_pairs(values: Iterable[Tuple[str, Any]]) -> List[Tuple[str, str]]:
        pairs = []
        for key, value in values:
            if value is None:
                continue
            if isinstance(value, (list, tuple)):
                for item in value:
                    if item is not None:
                        pairs.append((key, ApiClient.stringify(item)))
                continue
            pairs.append((key, ApiClient.stringify(value)))
        return pairs

    def request(self, method, service_base_url, path, path_params=None, query_params=None, headers=None, body=None):
        request = HttpRequest(
            method=method,
            url=f"{(self._config.base_url or service_base_url).rstrip('/')}{self.interpolate_path(path, path_params or [])}",
            headers=self.build_headers(headers or [], body),
            query=self.build_query_pairs(query_params or []),
            body=body,
            timeout=self._config.timeout,
        )
        response = self.send_with_retry(request)
        if response.status_code < 200 or response.status_code >= 300:
            raise self.map_exception(request, response)
        return self.decode_response(response)

    def build_headers(self, headers, body):
        resolved = {"Accept": "application/json", "User-Agent": self._config.user_agent, **self._config.default_headers}
        for key, value in headers:
            if value is not None:
                resolved[key] = self.stringify(value)
        if self._config.api_key and self._config.api_secret:
            resolved["Authorization"] = f"sso-key {self._config.api_key}:{self._config.api_secret}"
        if body is not None and "Content-Type" not in resolved:
            resolved["Content-Type"] = "application/json"
        return resolved

    def send_with_retry(self, request):
        attempt = 0
        while True:
            response = self._transport.send(request)
            if not self.should_retry(response.status_code, attempt):
                return response
            time.sleep(self._config.retry_delay * (2 ** attempt))
            attempt += 1

    def should_retry(self, status_code, attempt):
        return attempt < self._config.max_retries and status_code in {408, 429, 500, 502, 503, 504}

    def interpolate_path(self, path, path_params):
        from urllib.parse import quote
        resolved = path
        for key, value in path_params:
            if value is not None:
                resolved = resolved.replace(f"{{{key}}}", quote(self.stringify(value), safe=""))
        return resolved

    def decode_response(self, response):
        if not response.body:
            return None
        content_type = response.headers.get("content-type", response.headers.get("Content-Type", "")).lower()
        trimmed = response.body.lstrip()
        if "json" in content_type or trimmed.startswith("{") or trimmed.startswith("["):
            try:
                return json.loads(response.body)
            except json.JSONDecodeError:
                return response.body
        return response.body

    @staticmethod
    def stringify(value):
        if value is None:
            return ""
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, (dict, list, tuple)):
            return json.dumps(value)
        return str(value)

    def map_exception(self, request, response):
        args = (f"GoDaddy API request failed with status {response.status_code}", response.status_code, response.body, response.headers, request.method, request.full_url())
        if response.status_code == 400: return ValidationException(*args)
        if response.status_code in {401, 403}: return UnauthorizedException(*args)
        if response.status_code == 404: return NotFoundException(*args)
        if response.status_code == 429: return RateLimitException(*args)
        if response.status_code >= 500: return ServerException(*args)
        return ApiException(*args)
