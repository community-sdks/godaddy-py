from godaddy.errors import ApiException
from godaddy.errors import AgreementsApiException, AgreementsBadRequestException, AgreementsConflictException, AgreementsForbiddenException, AgreementsNotFoundException, AgreementsRateLimitException, AgreementsServerException, AgreementsUnauthorizedException, AgreementsUnprocessableEntityException
from godaddy.services.abstract_service import AbstractService
from godaddy.dto.agreements.requests import GetRequest
from godaddy.dto.agreements.responses import GetResponse

class AgreementsService(AbstractService):
    def __init__(self, client):
        super().__init__(client, "agreements")

    def get(self, request: GetRequest | None = None) -> GetResponse:
        request = request or GetRequest()
        response = self._execute(
            "GET",
            "/v1/agreements",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetResponse.from_mixed(response)

    def _map_exception(self, exception: ApiException) -> ApiException:
        if exception.status_code == 400:
            return AgreementsBadRequestException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 401:
            return AgreementsUnauthorizedException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 403:
            return AgreementsForbiddenException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 404:
            return AgreementsNotFoundException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 409:
            return AgreementsConflictException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 422:
            return AgreementsUnprocessableEntityException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 429:
            return AgreementsRateLimitException(*exception.args, error_response=exception.error_response)
        if exception.status_code >= 500:
            return AgreementsServerException(*exception.args, error_response=exception.error_response)
        return AgreementsApiException(*exception.args, error_response=exception.error_response)