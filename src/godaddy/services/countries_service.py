from godaddy.errors import ApiException
from godaddy.errors import CountriesApiException, CountriesBadRequestException, CountriesConflictException, CountriesForbiddenException, CountriesNotFoundException, CountriesRateLimitException, CountriesServerException, CountriesUnauthorizedException, CountriesUnprocessableEntityException
from godaddy.services.abstract_service import AbstractService
from godaddy.dto.countries.requests import GetCountriesRequest, GetCountryRequest
from godaddy.dto.countries.responses import GetCountriesResponse, GetCountryResponse

class CountriesService(AbstractService):
    def __init__(self, client):
        super().__init__(client, "countries")

    def get_countries(self, request: GetCountriesRequest | None = None) -> GetCountriesResponse:
        request = request or GetCountriesRequest()
        response = self._execute(
            "GET",
            "/v1/countries",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetCountriesResponse.from_mixed(response)

    def get_country(self, request: GetCountryRequest | None = None) -> GetCountryResponse:
        request = request or GetCountryRequest()
        response = self._execute(
            "GET",
            "/v1/countries/{countryKey}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetCountryResponse.from_mixed(response)

    def _map_exception(self, exception: ApiException) -> ApiException:
        if exception.status_code == 400:
            return CountriesBadRequestException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 401:
            return CountriesUnauthorizedException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 403:
            return CountriesForbiddenException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 404:
            return CountriesNotFoundException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 409:
            return CountriesConflictException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 422:
            return CountriesUnprocessableEntityException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 429:
            return CountriesRateLimitException(*exception.args, error_response=exception.error_response)
        if exception.status_code >= 500:
            return CountriesServerException(*exception.args, error_response=exception.error_response)
        return CountriesApiException(*exception.args, error_response=exception.error_response)