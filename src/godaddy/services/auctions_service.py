from godaddy.errors import ApiException
from godaddy.errors import AuctionsApiException, AuctionsBadRequestException, AuctionsConflictException, AuctionsForbiddenException, AuctionsNotFoundException, AuctionsRateLimitException, AuctionsServerException, AuctionsUnauthorizedException, AuctionsUnprocessableEntityException
from godaddy.services.abstract_service import AbstractService
from godaddy.dto.auctions.requests import PlaceBidsRequest
from godaddy.dto.auctions.responses import PlaceBidsResponse

class AuctionsService(AbstractService):
    def __init__(self, client):
        super().__init__(client, "auctions")

    def place_bids(self, request: PlaceBidsRequest | None = None) -> PlaceBidsResponse:
        request = request or PlaceBidsRequest()
        response = self._execute(
            "POST",
            "/v1/customers/{customerId}/aftermarket/listings/bids",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PlaceBidsResponse.from_mixed(response)

    def _map_exception(self, exception: ApiException) -> ApiException:
        if exception.status_code == 400:
            return AuctionsBadRequestException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 401:
            return AuctionsUnauthorizedException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 403:
            return AuctionsForbiddenException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 404:
            return AuctionsNotFoundException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 409:
            return AuctionsConflictException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 422:
            return AuctionsUnprocessableEntityException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 429:
            return AuctionsRateLimitException(*exception.args, error_response=exception.error_response)
        if exception.status_code >= 500:
            return AuctionsServerException(*exception.args, error_response=exception.error_response)
        return AuctionsApiException(*exception.args, error_response=exception.error_response)