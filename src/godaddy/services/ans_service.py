from godaddy.errors import ApiException
from godaddy.errors import AnsApiException, AnsBadRequestException, AnsConflictException, AnsForbiddenException, AnsNotFoundException, AnsRateLimitException, AnsServerException, AnsUnauthorizedException, AnsUnprocessableEntityException
from godaddy.services.abstract_service import AbstractService
from godaddy.dto.ans.requests import SearchAnsnameRequest, RegisterAgentRequest, ResolveAnsnameRequest, GetAgentRequest, RevokeAgentRequest, ValidateRegistrationRequest, VerifyDnsRecordsRequest, GetAgentIdentityCertificateByAgentIdRequest, SubmitAgentIdentityCsrByAgentIdRequest, GetAgentServerCertificateByAgentIdRequest, SubmitAgentServerCsrByAgentIdRequest, GetAgentCsrStatusByAgentIdRequest, GetAgentEventsRequest
from godaddy.dto.ans.responses import SearchAnsnameResponse, RegisterAgentResponse, ResolveAnsnameResponse, GetAgentResponse, RevokeAgentResponse, ValidateRegistrationResponse, VerifyDnsRecordsResponse, GetAgentIdentityCertificateByAgentIdResponse, SubmitAgentIdentityCsrByAgentIdResponse, GetAgentServerCertificateByAgentIdResponse, SubmitAgentServerCsrByAgentIdResponse, GetAgentCsrStatusByAgentIdResponse, GetAgentEventsResponse

class AnsService(AbstractService):
    def __init__(self, client):
        super().__init__(client, "ans")

    def search_ansname(self, request: SearchAnsnameRequest | None = None) -> SearchAnsnameResponse:
        request = request or SearchAnsnameRequest()
        response = self._execute(
            "GET",
            "/v1/agents",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return SearchAnsnameResponse.from_mixed(response)

    def register_agent(self, request: RegisterAgentRequest | None = None) -> RegisterAgentResponse:
        request = request or RegisterAgentRequest()
        response = self._execute(
            "POST",
            "/v1/agents/register",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return RegisterAgentResponse.from_mixed(response)

    def resolve_ansname(self, request: ResolveAnsnameRequest | None = None) -> ResolveAnsnameResponse:
        request = request or ResolveAnsnameRequest()
        response = self._execute(
            "POST",
            "/v1/agents/resolution",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return ResolveAnsnameResponse.from_mixed(response)

    def get_agent(self, request: GetAgentRequest | None = None) -> GetAgentResponse:
        request = request or GetAgentRequest()
        response = self._execute(
            "GET",
            "/v1/agents/{agentId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetAgentResponse.from_mixed(response)

    def revoke_agent(self, request: RevokeAgentRequest | None = None) -> RevokeAgentResponse:
        request = request or RevokeAgentRequest()
        response = self._execute(
            "POST",
            "/v1/agents/{agentId}/revoke",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return RevokeAgentResponse.from_mixed(response)

    def validate_registration(self, request: ValidateRegistrationRequest | None = None) -> ValidateRegistrationResponse:
        request = request or ValidateRegistrationRequest()
        response = self._execute(
            "POST",
            "/v1/agents/{agentId}/verify-acme",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return ValidateRegistrationResponse.from_mixed(response)

    def verify_dns_records(self, request: VerifyDnsRecordsRequest | None = None) -> VerifyDnsRecordsResponse:
        request = request or VerifyDnsRecordsRequest()
        response = self._execute(
            "POST",
            "/v1/agents/{agentId}/verify-dns",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return VerifyDnsRecordsResponse.from_mixed(response)

    def get_agent_identity_certificate_by_agent_id(self, request: GetAgentIdentityCertificateByAgentIdRequest | None = None) -> GetAgentIdentityCertificateByAgentIdResponse:
        request = request or GetAgentIdentityCertificateByAgentIdRequest()
        response = self._execute(
            "GET",
            "/v1/agents/{agentId}/certificates/identity",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetAgentIdentityCertificateByAgentIdResponse.from_mixed(response)

    def submit_agent_identity_csr_by_agent_id(self, request: SubmitAgentIdentityCsrByAgentIdRequest | None = None) -> SubmitAgentIdentityCsrByAgentIdResponse:
        request = request or SubmitAgentIdentityCsrByAgentIdRequest()
        response = self._execute(
            "POST",
            "/v1/agents/{agentId}/certificates/identity",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return SubmitAgentIdentityCsrByAgentIdResponse.from_mixed(response)

    def get_agent_server_certificate_by_agent_id(self, request: GetAgentServerCertificateByAgentIdRequest | None = None) -> GetAgentServerCertificateByAgentIdResponse:
        request = request or GetAgentServerCertificateByAgentIdRequest()
        response = self._execute(
            "GET",
            "/v1/agents/{agentId}/certificates/server",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetAgentServerCertificateByAgentIdResponse.from_mixed(response)

    def submit_agent_server_csr_by_agent_id(self, request: SubmitAgentServerCsrByAgentIdRequest | None = None) -> SubmitAgentServerCsrByAgentIdResponse:
        request = request or SubmitAgentServerCsrByAgentIdRequest()
        response = self._execute(
            "POST",
            "/v1/agents/{agentId}/certificates/server",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return SubmitAgentServerCsrByAgentIdResponse.from_mixed(response)

    def get_agent_csr_status_by_agent_id(self, request: GetAgentCsrStatusByAgentIdRequest | None = None) -> GetAgentCsrStatusByAgentIdResponse:
        request = request or GetAgentCsrStatusByAgentIdRequest()
        response = self._execute(
            "GET",
            "/v1/agents/{agentId}/csrs/{csrId}/status",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetAgentCsrStatusByAgentIdResponse.from_mixed(response)

    def get_agent_events(self, request: GetAgentEventsRequest | None = None) -> GetAgentEventsResponse:
        request = request or GetAgentEventsRequest()
        response = self._execute(
            "GET",
            "/v1/agents/events",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetAgentEventsResponse.from_mixed(response)

    def _map_exception(self, exception: ApiException) -> ApiException:
        if exception.status_code == 400:
            return AnsBadRequestException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 401:
            return AnsUnauthorizedException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 403:
            return AnsForbiddenException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 404:
            return AnsNotFoundException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 409:
            return AnsConflictException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 422:
            return AnsUnprocessableEntityException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 429:
            return AnsRateLimitException(*exception.args, error_response=exception.error_response)
        if exception.status_code >= 500:
            return AnsServerException(*exception.args, error_response=exception.error_response)
        return AnsApiException(*exception.args, error_response=exception.error_response)