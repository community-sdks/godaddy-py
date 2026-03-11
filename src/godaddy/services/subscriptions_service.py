from godaddy.errors import ApiException
from godaddy.errors import SubscriptionsApiException, SubscriptionsBadRequestException, SubscriptionsConflictException, SubscriptionsForbiddenException, SubscriptionsNotFoundException, SubscriptionsRateLimitException, SubscriptionsServerException, SubscriptionsUnauthorizedException, SubscriptionsUnprocessableEntityException
from godaddy.services.abstract_service import AbstractService
from godaddy.dto.subscriptions.requests import ListRequest, ProductGroupsRequest, GetRequest, UpdateRequest, CancelRequest
from godaddy.dto.subscriptions.responses import ListResponse, ProductGroupsResponse, GetResponse, UpdateResponse, CancelResponse

class SubscriptionsService(AbstractService):
    def __init__(self, client):
        super().__init__(client, "subscriptions")

    def list(self, request: ListRequest | None = None) -> ListResponse:
        request = request or ListRequest()
        response = self._execute(
            "GET",
            "/v1/subscriptions",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return ListResponse.from_mixed(response)

    def product_groups(self, request: ProductGroupsRequest | None = None) -> ProductGroupsResponse:
        request = request or ProductGroupsRequest()
        response = self._execute(
            "GET",
            "/v1/subscriptions/productGroups",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return ProductGroupsResponse.from_mixed(response)

    def get(self, request: GetRequest | None = None) -> GetResponse:
        request = request or GetRequest()
        response = self._execute(
            "GET",
            "/v1/subscriptions/{subscriptionId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetResponse.from_mixed(response)

    def update(self, request: UpdateRequest | None = None) -> UpdateResponse:
        request = request or UpdateRequest()
        response = self._execute(
            "PATCH",
            "/v1/subscriptions/{subscriptionId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return UpdateResponse.from_mixed(response)

    def cancel(self, request: CancelRequest | None = None) -> CancelResponse:
        request = request or CancelRequest()
        response = self._execute(
            "DELETE",
            "/v1/subscriptions/{subscriptionId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CancelResponse.from_mixed(response)

    def _map_exception(self, exception: ApiException) -> ApiException:
        if exception.status_code == 400:
            return SubscriptionsBadRequestException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 401:
            return SubscriptionsUnauthorizedException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 403:
            return SubscriptionsForbiddenException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 404:
            return SubscriptionsNotFoundException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 409:
            return SubscriptionsConflictException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 422:
            return SubscriptionsUnprocessableEntityException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 429:
            return SubscriptionsRateLimitException(*exception.args, error_response=exception.error_response)
        if exception.status_code >= 500:
            return SubscriptionsServerException(*exception.args, error_response=exception.error_response)
        return SubscriptionsApiException(*exception.args, error_response=exception.error_response)