from godaddy.errors import ApiException
from godaddy.errors import OrdersApiException, OrdersBadRequestException, OrdersConflictException, OrdersForbiddenException, OrdersNotFoundException, OrdersRateLimitException, OrdersServerException, OrdersUnauthorizedException, OrdersUnprocessableEntityException
from godaddy.services.abstract_service import AbstractService
from godaddy.dto.orders.requests import ListRequest, GetRequest
from godaddy.dto.orders.responses import ListResponse, GetResponse

class OrdersService(AbstractService):
    def __init__(self, client):
        super().__init__(client, "orders")

    def list(self, request: ListRequest | None = None) -> ListResponse:
        request = request or ListRequest()
        response = self._execute(
            "GET",
            "/v1/orders",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return ListResponse.from_mixed(response)

    def get(self, request: GetRequest | None = None) -> GetResponse:
        request = request or GetRequest()
        response = self._execute(
            "GET",
            "/v1/orders/{orderId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetResponse.from_mixed(response)

    def _map_exception(self, exception: ApiException) -> ApiException:
        if exception.status_code == 400:
            return OrdersBadRequestException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 401:
            return OrdersUnauthorizedException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 403:
            return OrdersForbiddenException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 404:
            return OrdersNotFoundException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 409:
            return OrdersConflictException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 422:
            return OrdersUnprocessableEntityException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 429:
            return OrdersRateLimitException(*exception.args, error_response=exception.error_response)
        if exception.status_code >= 500:
            return OrdersServerException(*exception.args, error_response=exception.error_response)
        return OrdersApiException(*exception.args, error_response=exception.error_response)