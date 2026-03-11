from godaddy.errors import ApiException
from godaddy.errors import CertificatesApiException, CertificatesBadRequestException, CertificatesConflictException, CertificatesForbiddenException, CertificatesNotFoundException, CertificatesRateLimitException, CertificatesServerException, CertificatesUnauthorizedException, CertificatesUnprocessableEntityException
from godaddy.services.abstract_service import AbstractService
from godaddy.dto.certificates.requests import CertificateCreateRequest, CertificateValidateRequest, CertificateGetRequest, CertificateActionRetrieveRequest, CertificateResendEmailRequest, CertificateAlternateEmailAddressRequest, CertificateResendEmailAddressRequest, CertificateEmailHistoryRequest, CertificateCallbackGetRequest, CertificateCallbackReplaceRequest, CertificateCallbackDeleteRequest, CertificateCancelRequest, CertificateDownloadRequest, CertificateReissueRequest, CertificateRenewRequest, CertificateRevokeRequest, CertificateSitesealGetRequest, CertificateVerifydomaincontrolRequest, CertificateGetEntitlementRequest, CertificateCreateRequest, CertificateDownloadEntitlementRequest, GetCustomerCertificatesByCustomerIdRequest, GetCertificateDetailByCertIdentifierRequest, GetDomainInformationByCertificateIdRequest, GetDomainDetailsByDomainRequest, GetAcmeExternalAccountBindingRequest, RetrieveSslByDomainResellerRequest, RetrieveSslByDomainSubscriptionResellerRequest
from godaddy.dto.certificates.responses import CertificateCreateResponse, CertificateValidateResponse, CertificateGetResponse, CertificateActionRetrieveResponse, CertificateResendEmailResponse, CertificateAlternateEmailAddressResponse, CertificateResendEmailAddressResponse, CertificateEmailHistoryResponse, CertificateCallbackGetResponse, CertificateCallbackReplaceResponse, CertificateCallbackDeleteResponse, CertificateCancelResponse, CertificateDownloadResponse, CertificateReissueResponse, CertificateRenewResponse, CertificateRevokeResponse, CertificateSitesealGetResponse, CertificateVerifydomaincontrolResponse, CertificateGetEntitlementResponse, CertificateCreateResponse, CertificateDownloadEntitlementResponse, GetCustomerCertificatesByCustomerIdResponse, GetCertificateDetailByCertIdentifierResponse, GetDomainInformationByCertificateIdResponse, GetDomainDetailsByDomainResponse, GetAcmeExternalAccountBindingResponse, RetrieveSslByDomainResellerResponse, RetrieveSslByDomainSubscriptionResellerResponse

class CertificatesService(AbstractService):
    def __init__(self, client):
        super().__init__(client, "certificates")

    def certificate_create(self, request: CertificateCreateRequest | None = None) -> CertificateCreateResponse:
        request = request or CertificateCreateRequest()
        response = self._execute(
            "POST",
            "/v1/certificates",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateCreateResponse.from_mixed(response)

    def certificate_validate(self, request: CertificateValidateRequest | None = None) -> CertificateValidateResponse:
        request = request or CertificateValidateRequest()
        response = self._execute(
            "POST",
            "/v1/certificates/validate",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateValidateResponse.from_mixed(response)

    def certificate_get(self, request: CertificateGetRequest | None = None) -> CertificateGetResponse:
        request = request or CertificateGetRequest()
        response = self._execute(
            "GET",
            "/v1/certificates/{certificateId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateGetResponse.from_mixed(response)

    def certificate_action_retrieve(self, request: CertificateActionRetrieveRequest | None = None) -> CertificateActionRetrieveResponse:
        request = request or CertificateActionRetrieveRequest()
        response = self._execute(
            "GET",
            "/v1/certificates/{certificateId}/actions",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateActionRetrieveResponse.from_mixed(response)

    def certificate_resend_email(self, request: CertificateResendEmailRequest | None = None) -> CertificateResendEmailResponse:
        request = request or CertificateResendEmailRequest()
        response = self._execute(
            "POST",
            "/v1/certificates/{certificateId}/email/{emailId}/resend",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateResendEmailResponse.from_mixed(response)

    def certificate_alternate_email_address(self, request: CertificateAlternateEmailAddressRequest | None = None) -> CertificateAlternateEmailAddressResponse:
        request = request or CertificateAlternateEmailAddressRequest()
        response = self._execute(
            "POST",
            "/v1/certificates/{certificateId}/email/resend/{emailAddress}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateAlternateEmailAddressResponse.from_mixed(response)

    def certificate_resend_email_address(self, request: CertificateResendEmailAddressRequest | None = None) -> CertificateResendEmailAddressResponse:
        request = request or CertificateResendEmailAddressRequest()
        response = self._execute(
            "POST",
            "/v1/certificates/{certificateId}/email/{emailId}/resend/{emailAddress}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateResendEmailAddressResponse.from_mixed(response)

    def certificate_email_history(self, request: CertificateEmailHistoryRequest | None = None) -> CertificateEmailHistoryResponse:
        request = request or CertificateEmailHistoryRequest()
        response = self._execute(
            "GET",
            "/v1/certificates/{certificateId}/email/history",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateEmailHistoryResponse.from_mixed(response)

    def certificate_callback_get(self, request: CertificateCallbackGetRequest | None = None) -> CertificateCallbackGetResponse:
        request = request or CertificateCallbackGetRequest()
        response = self._execute(
            "GET",
            "/v1/certificates/{certificateId}/callback",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateCallbackGetResponse.from_mixed(response)

    def certificate_callback_replace(self, request: CertificateCallbackReplaceRequest | None = None) -> CertificateCallbackReplaceResponse:
        request = request or CertificateCallbackReplaceRequest()
        response = self._execute(
            "PUT",
            "/v1/certificates/{certificateId}/callback",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateCallbackReplaceResponse.from_mixed(response)

    def certificate_callback_delete(self, request: CertificateCallbackDeleteRequest | None = None) -> CertificateCallbackDeleteResponse:
        request = request or CertificateCallbackDeleteRequest()
        response = self._execute(
            "DELETE",
            "/v1/certificates/{certificateId}/callback",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateCallbackDeleteResponse.from_mixed(response)

    def certificate_cancel(self, request: CertificateCancelRequest | None = None) -> CertificateCancelResponse:
        request = request or CertificateCancelRequest()
        response = self._execute(
            "POST",
            "/v1/certificates/{certificateId}/cancel",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateCancelResponse.from_mixed(response)

    def certificate_download(self, request: CertificateDownloadRequest | None = None) -> CertificateDownloadResponse:
        request = request or CertificateDownloadRequest()
        response = self._execute(
            "GET",
            "/v1/certificates/{certificateId}/download",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateDownloadResponse.from_mixed(response)

    def certificate_reissue(self, request: CertificateReissueRequest | None = None) -> CertificateReissueResponse:
        request = request or CertificateReissueRequest()
        response = self._execute(
            "POST",
            "/v1/certificates/{certificateId}/reissue",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateReissueResponse.from_mixed(response)

    def certificate_renew(self, request: CertificateRenewRequest | None = None) -> CertificateRenewResponse:
        request = request or CertificateRenewRequest()
        response = self._execute(
            "POST",
            "/v1/certificates/{certificateId}/renew",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateRenewResponse.from_mixed(response)

    def certificate_revoke(self, request: CertificateRevokeRequest | None = None) -> CertificateRevokeResponse:
        request = request or CertificateRevokeRequest()
        response = self._execute(
            "POST",
            "/v1/certificates/{certificateId}/revoke",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateRevokeResponse.from_mixed(response)

    def certificate_siteseal_get(self, request: CertificateSitesealGetRequest | None = None) -> CertificateSitesealGetResponse:
        request = request or CertificateSitesealGetRequest()
        response = self._execute(
            "GET",
            "/v1/certificates/{certificateId}/siteSeal",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateSitesealGetResponse.from_mixed(response)

    def certificate_verifydomaincontrol(self, request: CertificateVerifydomaincontrolRequest | None = None) -> CertificateVerifydomaincontrolResponse:
        request = request or CertificateVerifydomaincontrolRequest()
        response = self._execute(
            "POST",
            "/v1/certificates/{certificateId}/verifyDomainControl",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateVerifydomaincontrolResponse.from_mixed(response)

    def certificate_get_entitlement(self, request: CertificateGetEntitlementRequest | None = None) -> CertificateGetEntitlementResponse:
        request = request or CertificateGetEntitlementRequest()
        response = self._execute(
            "GET",
            "/v2/certificates",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateGetEntitlementResponse.from_mixed(response)

    def certificate_create(self, request: CertificateCreateRequest | None = None) -> CertificateCreateResponse:
        request = request or CertificateCreateRequest()
        response = self._execute(
            "POST",
            "/v2/certificates",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateCreateResponse.from_mixed(response)

    def certificate_download_entitlement(self, request: CertificateDownloadEntitlementRequest | None = None) -> CertificateDownloadEntitlementResponse:
        request = request or CertificateDownloadEntitlementRequest()
        response = self._execute(
            "GET",
            "/v2/certificates/download",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CertificateDownloadEntitlementResponse.from_mixed(response)

    def get_customer_certificates_by_customer_id(self, request: GetCustomerCertificatesByCustomerIdRequest | None = None) -> GetCustomerCertificatesByCustomerIdResponse:
        request = request or GetCustomerCertificatesByCustomerIdRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/certificates",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetCustomerCertificatesByCustomerIdResponse.from_mixed(response)

    def get_certificate_detail_by_cert_identifier(self, request: GetCertificateDetailByCertIdentifierRequest | None = None) -> GetCertificateDetailByCertIdentifierResponse:
        request = request or GetCertificateDetailByCertIdentifierRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/certificates/{certificateId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetCertificateDetailByCertIdentifierResponse.from_mixed(response)

    def get_domain_information_by_certificate_id(self, request: GetDomainInformationByCertificateIdRequest | None = None) -> GetDomainInformationByCertificateIdResponse:
        request = request or GetDomainInformationByCertificateIdRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/certificates/{certificateId}/domainVerifications",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetDomainInformationByCertificateIdResponse.from_mixed(response)

    def get_domain_details_by_domain(self, request: GetDomainDetailsByDomainRequest | None = None) -> GetDomainDetailsByDomainResponse:
        request = request or GetDomainDetailsByDomainRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/certificates/{certificateId}/domainVerifications/{domain}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetDomainDetailsByDomainResponse.from_mixed(response)

    def get_acme_external_account_binding(self, request: GetAcmeExternalAccountBindingRequest | None = None) -> GetAcmeExternalAccountBindingResponse:
        request = request or GetAcmeExternalAccountBindingRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/certificates/acme/externalAccountBinding",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetAcmeExternalAccountBindingResponse.from_mixed(response)

    def retrieve_ssl_by_domain_reseller(self, request: RetrieveSslByDomainResellerRequest | None = None) -> RetrieveSslByDomainResellerResponse:
        request = request or RetrieveSslByDomainResellerRequest()
        response = self._execute(
            "GET",
            "/v2/certificates/subscriptions/search",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return RetrieveSslByDomainResellerResponse.from_mixed(response)

    def retrieve_ssl_by_domain_subscription_reseller(self, request: RetrieveSslByDomainSubscriptionResellerRequest | None = None) -> RetrieveSslByDomainSubscriptionResellerResponse:
        request = request or RetrieveSslByDomainSubscriptionResellerRequest()
        response = self._execute(
            "GET",
            "/v2/certificates/subscription/{guid}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return RetrieveSslByDomainSubscriptionResellerResponse.from_mixed(response)

    def _map_exception(self, exception: ApiException) -> ApiException:
        if exception.status_code == 400:
            return CertificatesBadRequestException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 401:
            return CertificatesUnauthorizedException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 403:
            return CertificatesForbiddenException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 404:
            return CertificatesNotFoundException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 409:
            return CertificatesConflictException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 422:
            return CertificatesUnprocessableEntityException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 429:
            return CertificatesRateLimitException(*exception.args, error_response=exception.error_response)
        if exception.status_code >= 500:
            return CertificatesServerException(*exception.args, error_response=exception.error_response)
        return CertificatesApiException(*exception.args, error_response=exception.error_response)