from godaddy.errors import ApiException
from godaddy.errors import ParkingApiException, ParkingBadRequestException, ParkingConflictException, ParkingForbiddenException, ParkingNotFoundException, ParkingRateLimitException, ParkingServerException, ParkingUnauthorizedException, ParkingUnprocessableEntityException
from godaddy.services.abstract_service import AbstractService
from godaddy.dto.parking.requests import GetMetricsRequest, GetMetricsByDomainRequest
from godaddy.dto.parking.responses import GetMetricsResponse, GetMetricsByDomainResponse

class ParkingService(AbstractService):
    def __init__(self, client):
        super().__init__(client, "parking")

    def get_metrics(self, request: GetMetricsRequest | None = None) -> GetMetricsResponse:
        request = request or GetMetricsRequest()
        response = self._execute(
            "GET",
            "/v1/customers/{customerId}/parking/metrics",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetMetricsResponse.from_mixed(response)

    def get_metrics_by_domain(self, request: GetMetricsByDomainRequest | None = None) -> GetMetricsByDomainResponse:
        request = request or GetMetricsByDomainRequest()
        response = self._execute(
            "GET",
            "/v1/customers/{customerId}/parking/metricsByDomain",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetMetricsByDomainResponse.from_mixed(response)

    def _map_exception(self, exception: ApiException) -> ApiException:
        if exception.status_code == 400:
            return ParkingBadRequestException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 401:
            return ParkingUnauthorizedException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 403:
            return ParkingForbiddenException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 404:
            return ParkingNotFoundException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 409:
            return ParkingConflictException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 422:
            return ParkingUnprocessableEntityException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 429:
            return ParkingRateLimitException(*exception.args, error_response=exception.error_response)
        if exception.status_code >= 500:
            return ParkingServerException(*exception.args, error_response=exception.error_response)
        return ParkingApiException(*exception.args, error_response=exception.error_response)