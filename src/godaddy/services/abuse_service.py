from godaddy.errors import ApiException
from godaddy.errors import AbuseApiException, AbuseBadRequestException, AbuseConflictException, AbuseForbiddenException, AbuseNotFoundException, AbuseRateLimitException, AbuseServerException, AbuseUnauthorizedException, AbuseUnprocessableEntityException
from godaddy.services.abstract_service import AbstractService
from godaddy.dto.abuse.requests import GetTicketsRequest, CreateTicketRequest, GetTicketInfoRequest, GetTicketsV2Request, CreateTicketV2Request, GetTicketInfoV2Request
from godaddy.dto.abuse.responses import GetTicketsResponse, CreateTicketResponse, GetTicketInfoResponse, GetTicketsV2Response, CreateTicketV2Response, GetTicketInfoV2Response

class AbuseService(AbstractService):
    def __init__(self, client):
        super().__init__(client, "abuse")

    def get_tickets(self, request: GetTicketsRequest | None = None) -> GetTicketsResponse:
        request = request or GetTicketsRequest()
        response = self._execute(
            "GET",
            "/v1/abuse/tickets",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetTicketsResponse.from_mixed(response)

    def create_ticket(self, request: CreateTicketRequest | None = None) -> CreateTicketResponse:
        request = request or CreateTicketRequest()
        response = self._execute(
            "POST",
            "/v1/abuse/tickets",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CreateTicketResponse.from_mixed(response)

    def get_ticket_info(self, request: GetTicketInfoRequest | None = None) -> GetTicketInfoResponse:
        request = request or GetTicketInfoRequest()
        response = self._execute(
            "GET",
            "/v1/abuse/tickets/{ticketId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetTicketInfoResponse.from_mixed(response)

    def get_tickets_v2(self, request: GetTicketsV2Request | None = None) -> GetTicketsV2Response:
        request = request or GetTicketsV2Request()
        response = self._execute(
            "GET",
            "/v2/abuse/tickets",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetTicketsV2Response.from_mixed(response)

    def create_ticket_v2(self, request: CreateTicketV2Request | None = None) -> CreateTicketV2Response:
        request = request or CreateTicketV2Request()
        response = self._execute(
            "POST",
            "/v2/abuse/tickets",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CreateTicketV2Response.from_mixed(response)

    def get_ticket_info_v2(self, request: GetTicketInfoV2Request | None = None) -> GetTicketInfoV2Response:
        request = request or GetTicketInfoV2Request()
        response = self._execute(
            "GET",
            "/v2/abuse/tickets/{ticketId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetTicketInfoV2Response.from_mixed(response)

    def _map_exception(self, exception: ApiException) -> ApiException:
        if exception.status_code == 400:
            return AbuseBadRequestException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 401:
            return AbuseUnauthorizedException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 403:
            return AbuseForbiddenException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 404:
            return AbuseNotFoundException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 409:
            return AbuseConflictException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 422:
            return AbuseUnprocessableEntityException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 429:
            return AbuseRateLimitException(*exception.args, error_response=exception.error_response)
        if exception.status_code >= 500:
            return AbuseServerException(*exception.args, error_response=exception.error_response)
        return AbuseApiException(*exception.args, error_response=exception.error_response)