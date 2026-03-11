from godaddy.errors import ApiException
from godaddy.errors import AftermarketApiException, AftermarketBadRequestException, AftermarketConflictException, AftermarketForbiddenException, AftermarketNotFoundException, AftermarketRateLimitException, AftermarketServerException, AftermarketUnauthorizedException, AftermarketUnprocessableEntityException
from godaddy.services.abstract_service import AbstractService
from godaddy.dto.aftermarket.requests import GetListingsRequest, DeleteListingsRequest, AddExpiryListingsRequest
from godaddy.dto.aftermarket.responses import GetListingsResponse, DeleteListingsResponse, AddExpiryListingsResponse

class AftermarketService(AbstractService):
    def __init__(self, client):
        super().__init__(client, "aftermarket")

    def get_listings(self, request: GetListingsRequest | None = None) -> GetListingsResponse:
        request = request or GetListingsRequest()
        response = self._execute(
            "GET",
            "/v1/customers/{customerId}/auctions/listings",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetListingsResponse.from_mixed(response)

    def delete_listings(self, request: DeleteListingsRequest | None = None) -> DeleteListingsResponse:
        request = request or DeleteListingsRequest()
        response = self._execute(
            "DELETE",
            "/v1/aftermarket/listings",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return DeleteListingsResponse.from_mixed(response)

    def add_expiry_listings(self, request: AddExpiryListingsRequest | None = None) -> AddExpiryListingsResponse:
        request = request or AddExpiryListingsRequest()
        response = self._execute(
            "POST",
            "/v1/aftermarket/listings/expiry",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return AddExpiryListingsResponse.from_mixed(response)

    def _map_exception(self, exception: ApiException) -> ApiException:
        if exception.status_code == 400:
            return AftermarketBadRequestException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 401:
            return AftermarketUnauthorizedException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 403:
            return AftermarketForbiddenException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 404:
            return AftermarketNotFoundException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 409:
            return AftermarketConflictException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 422:
            return AftermarketUnprocessableEntityException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 429:
            return AftermarketRateLimitException(*exception.args, error_response=exception.error_response)
        if exception.status_code >= 500:
            return AftermarketServerException(*exception.args, error_response=exception.error_response)
        return AftermarketApiException(*exception.args, error_response=exception.error_response)