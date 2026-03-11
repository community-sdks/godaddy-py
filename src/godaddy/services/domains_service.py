from godaddy.errors import ApiException
from godaddy.errors import DomainsApiException, DomainsBadRequestException, DomainsConflictException, DomainsForbiddenException, DomainsNotFoundException, DomainsRateLimitException, DomainsServerException, DomainsUnauthorizedException, DomainsUnprocessableEntityException
from godaddy.services.abstract_service import AbstractService
from godaddy.dto.domains.requests import ListRequest, GetAgreementRequest, AvailableRequest, AvailableBulkRequest, ContactsValidateRequest, PurchaseRequest, SchemaRequest, ValidateRequest, SuggestRequest, TldsRequest, GetRequest, UpdateRequest, CancelRequest, UpdateContactsRequest, CancelPrivacyRequest, PurchasePrivacyRequest, RecordReplaceRequest, RecordAddRequest, RecordGetRequest, RecordReplaceTypeNameRequest, RecordDeleteTypeNameRequest, RecordReplaceTypeRequest, RenewRequest, TransferInRequest, VerifyEmailRequest, GetV2CustomersCustomerIdDomainsDomainRequest, GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantRequest, DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantRequest, PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsRequest, DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsRequest, PutV2CustomersCustomerIdDomainsDomainNameServersRequest, GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingRequest, PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingRequest, PostV2CustomersCustomerIdDomainsDomainRedeemRequest, PostV2CustomersCustomerIdDomainsDomainRenewRequest, GetV2CustomersCustomerIdDomainsDomainTransferRequest, PostV2CustomersCustomerIdDomainsDomainTransferRequest, PostV2CustomersCustomerIdDomainsDomainTransferValidateRequest, PostV2CustomersCustomerIdDomainsDomainTransferInAcceptRequest, PostV2CustomersCustomerIdDomainsDomainTransferInCancelRequest, PostV2CustomersCustomerIdDomainsDomainTransferInRestartRequest, PostV2CustomersCustomerIdDomainsDomainTransferInRetryRequest, PostV2CustomersCustomerIdDomainsDomainTransferOutRequest, PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptRequest, PostV2CustomersCustomerIdDomainsDomainTransferOutRejectRequest, DomainsForwardsGetRequest, DomainsForwardsPostRequest, DomainsForwardsPutRequest, DomainsForwardsDeleteRequest, GetV2CustomersCustomerIdDomainsDomainActionsRequest, GetV2CustomersCustomerIdDomainsDomainActionsTypeRequest, DeleteV2CustomersCustomerIdDomainsDomainActionsTypeRequest, GetV2CustomersCustomerIdDomainsNotificationsRequest, GetV2CustomersCustomerIdDomainsNotificationsOptInRequest, PutV2CustomersCustomerIdDomainsNotificationsOptInRequest, GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeRequest, PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeRequest, PostV2CustomersCustomerIdDomainsRegisterRequest, GetV2CustomersCustomerIdDomainsRegisterSchemaTldRequest, PostV2CustomersCustomerIdDomainsRegisterValidateRequest, GetV2DomainsMaintenancesRequest, GetV2DomainsMaintenancesMaintenanceIdRequest, GetV2DomainsUsageYyyymmRequest, PatchV2CustomersCustomerIdDomainsDomainContactsRequest, PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeRequest
from godaddy.dto.domains.responses import ListResponse, GetAgreementResponse, AvailableResponse, AvailableBulkResponse, ContactsValidateResponse, PurchaseResponse, SchemaResponse, ValidateResponse, SuggestResponse, TldsResponse, GetResponse, UpdateResponse, CancelResponse, UpdateContactsResponse, CancelPrivacyResponse, PurchasePrivacyResponse, RecordReplaceResponse, RecordAddResponse, RecordGetResponse, RecordReplaceTypeNameResponse, RecordDeleteTypeNameResponse, RecordReplaceTypeResponse, RenewResponse, TransferInResponse, VerifyEmailResponse, GetV2CustomersCustomerIdDomainsDomainResponse, GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse, DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse, PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse, DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse, PutV2CustomersCustomerIdDomainsDomainNameServersResponse, GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse, PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse, PostV2CustomersCustomerIdDomainsDomainRedeemResponse, PostV2CustomersCustomerIdDomainsDomainRenewResponse, GetV2CustomersCustomerIdDomainsDomainTransferResponse, PostV2CustomersCustomerIdDomainsDomainTransferResponse, PostV2CustomersCustomerIdDomainsDomainTransferValidateResponse, PostV2CustomersCustomerIdDomainsDomainTransferInAcceptResponse, PostV2CustomersCustomerIdDomainsDomainTransferInCancelResponse, PostV2CustomersCustomerIdDomainsDomainTransferInRestartResponse, PostV2CustomersCustomerIdDomainsDomainTransferInRetryResponse, PostV2CustomersCustomerIdDomainsDomainTransferOutResponse, PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptResponse, PostV2CustomersCustomerIdDomainsDomainTransferOutRejectResponse, DomainsForwardsGetResponse, DomainsForwardsPostResponse, DomainsForwardsPutResponse, DomainsForwardsDeleteResponse, GetV2CustomersCustomerIdDomainsDomainActionsResponse, GetV2CustomersCustomerIdDomainsDomainActionsTypeResponse, DeleteV2CustomersCustomerIdDomainsDomainActionsTypeResponse, GetV2CustomersCustomerIdDomainsNotificationsResponse, GetV2CustomersCustomerIdDomainsNotificationsOptInResponse, PutV2CustomersCustomerIdDomainsNotificationsOptInResponse, GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeResponse, PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeResponse, PostV2CustomersCustomerIdDomainsRegisterResponse, GetV2CustomersCustomerIdDomainsRegisterSchemaTldResponse, PostV2CustomersCustomerIdDomainsRegisterValidateResponse, GetV2DomainsMaintenancesResponse, GetV2DomainsMaintenancesMaintenanceIdResponse, GetV2DomainsUsageYyyymmResponse, PatchV2CustomersCustomerIdDomainsDomainContactsResponse, PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeResponse

class DomainsService(AbstractService):
    def __init__(self, client):
        super().__init__(client, "domains")

    def list(self, request: ListRequest | None = None) -> ListResponse:
        request = request or ListRequest()
        response = self._execute(
            "GET",
            "/v1/domains",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return ListResponse.from_mixed(response)

    def get_agreement(self, request: GetAgreementRequest | None = None) -> GetAgreementResponse:
        request = request or GetAgreementRequest()
        response = self._execute(
            "GET",
            "/v1/domains/agreements",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetAgreementResponse.from_mixed(response)

    def available(self, request: AvailableRequest | None = None) -> AvailableResponse:
        request = request or AvailableRequest()
        response = self._execute(
            "GET",
            "/v1/domains/available",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return AvailableResponse.from_mixed(response)

    def available_bulk(self, request: AvailableBulkRequest | None = None) -> AvailableBulkResponse:
        request = request or AvailableBulkRequest()
        response = self._execute(
            "POST",
            "/v1/domains/available",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return AvailableBulkResponse.from_mixed(response)

    def contacts_validate(self, request: ContactsValidateRequest | None = None) -> ContactsValidateResponse:
        request = request or ContactsValidateRequest()
        response = self._execute(
            "POST",
            "/v1/domains/contacts/validate",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return ContactsValidateResponse.from_mixed(response)

    def purchase(self, request: PurchaseRequest | None = None) -> PurchaseResponse:
        request = request or PurchaseRequest()
        response = self._execute(
            "POST",
            "/v1/domains/purchase",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PurchaseResponse.from_mixed(response)

    def schema(self, request: SchemaRequest | None = None) -> SchemaResponse:
        request = request or SchemaRequest()
        response = self._execute(
            "GET",
            "/v1/domains/purchase/schema/{tld}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return SchemaResponse.from_mixed(response)

    def validate(self, request: ValidateRequest | None = None) -> ValidateResponse:
        request = request or ValidateRequest()
        response = self._execute(
            "POST",
            "/v1/domains/purchase/validate",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return ValidateResponse.from_mixed(response)

    def suggest(self, request: SuggestRequest | None = None) -> SuggestResponse:
        request = request or SuggestRequest()
        response = self._execute(
            "GET",
            "/v1/domains/suggest",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return SuggestResponse.from_mixed(response)

    def tlds(self, request: TldsRequest | None = None) -> TldsResponse:
        request = request or TldsRequest()
        response = self._execute(
            "GET",
            "/v1/domains/tlds",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return TldsResponse.from_mixed(response)

    def get(self, request: GetRequest | None = None) -> GetResponse:
        request = request or GetRequest()
        response = self._execute(
            "GET",
            "/v1/domains/{domain}",
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
            "/v1/domains/{domain}",
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
            "/v1/domains/{domain}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CancelResponse.from_mixed(response)

    def update_contacts(self, request: UpdateContactsRequest | None = None) -> UpdateContactsResponse:
        request = request or UpdateContactsRequest()
        response = self._execute(
            "PATCH",
            "/v1/domains/{domain}/contacts",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return UpdateContactsResponse.from_mixed(response)

    def cancel_privacy(self, request: CancelPrivacyRequest | None = None) -> CancelPrivacyResponse:
        request = request or CancelPrivacyRequest()
        response = self._execute(
            "DELETE",
            "/v1/domains/{domain}/privacy",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return CancelPrivacyResponse.from_mixed(response)

    def purchase_privacy(self, request: PurchasePrivacyRequest | None = None) -> PurchasePrivacyResponse:
        request = request or PurchasePrivacyRequest()
        response = self._execute(
            "POST",
            "/v1/domains/{domain}/privacy/purchase",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PurchasePrivacyResponse.from_mixed(response)

    def record_replace(self, request: RecordReplaceRequest | None = None) -> RecordReplaceResponse:
        request = request or RecordReplaceRequest()
        response = self._execute(
            "PUT",
            "/v1/domains/{domain}/records",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return RecordReplaceResponse.from_mixed(response)

    def record_add(self, request: RecordAddRequest | None = None) -> RecordAddResponse:
        request = request or RecordAddRequest()
        response = self._execute(
            "PATCH",
            "/v1/domains/{domain}/records",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return RecordAddResponse.from_mixed(response)

    def record_get(self, request: RecordGetRequest | None = None) -> RecordGetResponse:
        request = request or RecordGetRequest()
        response = self._execute(
            "GET",
            "/v1/domains/{domain}/records/{type}/{name}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return RecordGetResponse.from_mixed(response)

    def record_replace_type_name(self, request: RecordReplaceTypeNameRequest | None = None) -> RecordReplaceTypeNameResponse:
        request = request or RecordReplaceTypeNameRequest()
        response = self._execute(
            "PUT",
            "/v1/domains/{domain}/records/{type}/{name}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return RecordReplaceTypeNameResponse.from_mixed(response)

    def record_delete_type_name(self, request: RecordDeleteTypeNameRequest | None = None) -> RecordDeleteTypeNameResponse:
        request = request or RecordDeleteTypeNameRequest()
        response = self._execute(
            "DELETE",
            "/v1/domains/{domain}/records/{type}/{name}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return RecordDeleteTypeNameResponse.from_mixed(response)

    def record_replace_type(self, request: RecordReplaceTypeRequest | None = None) -> RecordReplaceTypeResponse:
        request = request or RecordReplaceTypeRequest()
        response = self._execute(
            "PUT",
            "/v1/domains/{domain}/records/{type}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return RecordReplaceTypeResponse.from_mixed(response)

    def renew(self, request: RenewRequest | None = None) -> RenewResponse:
        request = request or RenewRequest()
        response = self._execute(
            "POST",
            "/v1/domains/{domain}/renew",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return RenewResponse.from_mixed(response)

    def transfer_in(self, request: TransferInRequest | None = None) -> TransferInResponse:
        request = request or TransferInRequest()
        response = self._execute(
            "POST",
            "/v1/domains/{domain}/transfer",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return TransferInResponse.from_mixed(response)

    def verify_email(self, request: VerifyEmailRequest | None = None) -> VerifyEmailResponse:
        request = request or VerifyEmailRequest()
        response = self._execute(
            "POST",
            "/v1/domains/{domain}/verifyRegistrantEmail",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return VerifyEmailResponse.from_mixed(response)

    def get_v2_customers_customer_id_domains_domain(self, request: GetV2CustomersCustomerIdDomainsDomainRequest | None = None) -> GetV2CustomersCustomerIdDomainsDomainResponse:
        request = request or GetV2CustomersCustomerIdDomainsDomainRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/domains/{domain}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2CustomersCustomerIdDomainsDomainResponse.from_mixed(response)

    def get_v2_customers_customer_id_domains_domain_change_of_registrant(self, request: GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantRequest | None = None) -> GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse:
        request = request or GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/domains/{domain}/changeOfRegistrant",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse.from_mixed(response)

    def delete_v2_customers_customer_id_domains_domain_change_of_registrant(self, request: DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantRequest | None = None) -> DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse:
        request = request or DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantRequest()
        response = self._execute(
            "DELETE",
            "/v2/customers/{customerId}/domains/{domain}/changeOfRegistrant",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse.from_mixed(response)

    def patch_v2_customers_customer_id_domains_domain_dnssec_records(self, request: PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsRequest | None = None) -> PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse:
        request = request or PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsRequest()
        response = self._execute(
            "PATCH",
            "/v2/customers/{customerId}/domains/{domain}/dnssecRecords",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse.from_mixed(response)

    def delete_v2_customers_customer_id_domains_domain_dnssec_records(self, request: DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsRequest | None = None) -> DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse:
        request = request or DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsRequest()
        response = self._execute(
            "DELETE",
            "/v2/customers/{customerId}/domains/{domain}/dnssecRecords",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse.from_mixed(response)

    def put_v2_customers_customer_id_domains_domain_name_servers(self, request: PutV2CustomersCustomerIdDomainsDomainNameServersRequest | None = None) -> PutV2CustomersCustomerIdDomainsDomainNameServersResponse:
        request = request or PutV2CustomersCustomerIdDomainsDomainNameServersRequest()
        response = self._execute(
            "PUT",
            "/v2/customers/{customerId}/domains/{domain}/nameServers",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PutV2CustomersCustomerIdDomainsDomainNameServersResponse.from_mixed(response)

    def get_v2_customers_customer_id_domains_domain_privacy_forwarding(self, request: GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingRequest | None = None) -> GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse:
        request = request or GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/domains/{domain}/privacy/forwarding",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse.from_mixed(response)

    def patch_v2_customers_customer_id_domains_domain_privacy_forwarding(self, request: PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingRequest | None = None) -> PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse:
        request = request or PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingRequest()
        response = self._execute(
            "PATCH",
            "/v2/customers/{customerId}/domains/{domain}/privacy/forwarding",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_domain_redeem(self, request: PostV2CustomersCustomerIdDomainsDomainRedeemRequest | None = None) -> PostV2CustomersCustomerIdDomainsDomainRedeemResponse:
        request = request or PostV2CustomersCustomerIdDomainsDomainRedeemRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/redeem",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsDomainRedeemResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_domain_renew(self, request: PostV2CustomersCustomerIdDomainsDomainRenewRequest | None = None) -> PostV2CustomersCustomerIdDomainsDomainRenewResponse:
        request = request or PostV2CustomersCustomerIdDomainsDomainRenewRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/renew",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsDomainRenewResponse.from_mixed(response)

    def get_v2_customers_customer_id_domains_domain_transfer(self, request: GetV2CustomersCustomerIdDomainsDomainTransferRequest | None = None) -> GetV2CustomersCustomerIdDomainsDomainTransferResponse:
        request = request or GetV2CustomersCustomerIdDomainsDomainTransferRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/domains/{domain}/transfer",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2CustomersCustomerIdDomainsDomainTransferResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_domain_transfer(self, request: PostV2CustomersCustomerIdDomainsDomainTransferRequest | None = None) -> PostV2CustomersCustomerIdDomainsDomainTransferResponse:
        request = request or PostV2CustomersCustomerIdDomainsDomainTransferRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transfer",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsDomainTransferResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_domain_transfer_validate(self, request: PostV2CustomersCustomerIdDomainsDomainTransferValidateRequest | None = None) -> PostV2CustomersCustomerIdDomainsDomainTransferValidateResponse:
        request = request or PostV2CustomersCustomerIdDomainsDomainTransferValidateRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transfer/validate",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsDomainTransferValidateResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_domain_transfer_in_accept(self, request: PostV2CustomersCustomerIdDomainsDomainTransferInAcceptRequest | None = None) -> PostV2CustomersCustomerIdDomainsDomainTransferInAcceptResponse:
        request = request or PostV2CustomersCustomerIdDomainsDomainTransferInAcceptRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferInAccept",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsDomainTransferInAcceptResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_domain_transfer_in_cancel(self, request: PostV2CustomersCustomerIdDomainsDomainTransferInCancelRequest | None = None) -> PostV2CustomersCustomerIdDomainsDomainTransferInCancelResponse:
        request = request or PostV2CustomersCustomerIdDomainsDomainTransferInCancelRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferInCancel",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsDomainTransferInCancelResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_domain_transfer_in_restart(self, request: PostV2CustomersCustomerIdDomainsDomainTransferInRestartRequest | None = None) -> PostV2CustomersCustomerIdDomainsDomainTransferInRestartResponse:
        request = request or PostV2CustomersCustomerIdDomainsDomainTransferInRestartRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferInRestart",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsDomainTransferInRestartResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_domain_transfer_in_retry(self, request: PostV2CustomersCustomerIdDomainsDomainTransferInRetryRequest | None = None) -> PostV2CustomersCustomerIdDomainsDomainTransferInRetryResponse:
        request = request or PostV2CustomersCustomerIdDomainsDomainTransferInRetryRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferInRetry",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsDomainTransferInRetryResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_domain_transfer_out(self, request: PostV2CustomersCustomerIdDomainsDomainTransferOutRequest | None = None) -> PostV2CustomersCustomerIdDomainsDomainTransferOutResponse:
        request = request or PostV2CustomersCustomerIdDomainsDomainTransferOutRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferOut",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsDomainTransferOutResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_domain_transfer_out_accept(self, request: PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptRequest | None = None) -> PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptResponse:
        request = request or PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferOutAccept",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_domain_transfer_out_reject(self, request: PostV2CustomersCustomerIdDomainsDomainTransferOutRejectRequest | None = None) -> PostV2CustomersCustomerIdDomainsDomainTransferOutRejectResponse:
        request = request or PostV2CustomersCustomerIdDomainsDomainTransferOutRejectRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferOutReject",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsDomainTransferOutRejectResponse.from_mixed(response)

    def domains_forwards_get(self, request: DomainsForwardsGetRequest | None = None) -> DomainsForwardsGetResponse:
        request = request or DomainsForwardsGetRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/domains/forwards/{fqdn}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return DomainsForwardsGetResponse.from_mixed(response)

    def domains_forwards_post(self, request: DomainsForwardsPostRequest | None = None) -> DomainsForwardsPostResponse:
        request = request or DomainsForwardsPostRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/forwards/{fqdn}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return DomainsForwardsPostResponse.from_mixed(response)

    def domains_forwards_put(self, request: DomainsForwardsPutRequest | None = None) -> DomainsForwardsPutResponse:
        request = request or DomainsForwardsPutRequest()
        response = self._execute(
            "PUT",
            "/v2/customers/{customerId}/domains/forwards/{fqdn}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return DomainsForwardsPutResponse.from_mixed(response)

    def domains_forwards_delete(self, request: DomainsForwardsDeleteRequest | None = None) -> DomainsForwardsDeleteResponse:
        request = request or DomainsForwardsDeleteRequest()
        response = self._execute(
            "DELETE",
            "/v2/customers/{customerId}/domains/forwards/{fqdn}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return DomainsForwardsDeleteResponse.from_mixed(response)

    def get_v2_customers_customer_id_domains_domain_actions(self, request: GetV2CustomersCustomerIdDomainsDomainActionsRequest | None = None) -> GetV2CustomersCustomerIdDomainsDomainActionsResponse:
        request = request or GetV2CustomersCustomerIdDomainsDomainActionsRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/domains/{domain}/actions",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2CustomersCustomerIdDomainsDomainActionsResponse.from_mixed(response)

    def get_v2_customers_customer_id_domains_domain_actions_type(self, request: GetV2CustomersCustomerIdDomainsDomainActionsTypeRequest | None = None) -> GetV2CustomersCustomerIdDomainsDomainActionsTypeResponse:
        request = request or GetV2CustomersCustomerIdDomainsDomainActionsTypeRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/domains/{domain}/actions/{type}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2CustomersCustomerIdDomainsDomainActionsTypeResponse.from_mixed(response)

    def delete_v2_customers_customer_id_domains_domain_actions_type(self, request: DeleteV2CustomersCustomerIdDomainsDomainActionsTypeRequest | None = None) -> DeleteV2CustomersCustomerIdDomainsDomainActionsTypeResponse:
        request = request or DeleteV2CustomersCustomerIdDomainsDomainActionsTypeRequest()
        response = self._execute(
            "DELETE",
            "/v2/customers/{customerId}/domains/{domain}/actions/{type}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return DeleteV2CustomersCustomerIdDomainsDomainActionsTypeResponse.from_mixed(response)

    def get_v2_customers_customer_id_domains_notifications(self, request: GetV2CustomersCustomerIdDomainsNotificationsRequest | None = None) -> GetV2CustomersCustomerIdDomainsNotificationsResponse:
        request = request or GetV2CustomersCustomerIdDomainsNotificationsRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/domains/notifications",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2CustomersCustomerIdDomainsNotificationsResponse.from_mixed(response)

    def get_v2_customers_customer_id_domains_notifications_opt_in(self, request: GetV2CustomersCustomerIdDomainsNotificationsOptInRequest | None = None) -> GetV2CustomersCustomerIdDomainsNotificationsOptInResponse:
        request = request or GetV2CustomersCustomerIdDomainsNotificationsOptInRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/domains/notifications/optIn",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2CustomersCustomerIdDomainsNotificationsOptInResponse.from_mixed(response)

    def put_v2_customers_customer_id_domains_notifications_opt_in(self, request: PutV2CustomersCustomerIdDomainsNotificationsOptInRequest | None = None) -> PutV2CustomersCustomerIdDomainsNotificationsOptInResponse:
        request = request or PutV2CustomersCustomerIdDomainsNotificationsOptInRequest()
        response = self._execute(
            "PUT",
            "/v2/customers/{customerId}/domains/notifications/optIn",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PutV2CustomersCustomerIdDomainsNotificationsOptInResponse.from_mixed(response)

    def get_v2_customers_customer_id_domains_notifications_schemas_type(self, request: GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeRequest | None = None) -> GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeResponse:
        request = request or GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/domains/notifications/schemas/{type}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_notifications_notification_id_acknowledge(self, request: PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeRequest | None = None) -> PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeResponse:
        request = request or PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/notifications/{notificationId}/acknowledge",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_register(self, request: PostV2CustomersCustomerIdDomainsRegisterRequest | None = None) -> PostV2CustomersCustomerIdDomainsRegisterResponse:
        request = request or PostV2CustomersCustomerIdDomainsRegisterRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/register",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsRegisterResponse.from_mixed(response)

    def get_v2_customers_customer_id_domains_register_schema_tld(self, request: GetV2CustomersCustomerIdDomainsRegisterSchemaTldRequest | None = None) -> GetV2CustomersCustomerIdDomainsRegisterSchemaTldResponse:
        request = request or GetV2CustomersCustomerIdDomainsRegisterSchemaTldRequest()
        response = self._execute(
            "GET",
            "/v2/customers/{customerId}/domains/register/schema/{tld}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2CustomersCustomerIdDomainsRegisterSchemaTldResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_register_validate(self, request: PostV2CustomersCustomerIdDomainsRegisterValidateRequest | None = None) -> PostV2CustomersCustomerIdDomainsRegisterValidateResponse:
        request = request or PostV2CustomersCustomerIdDomainsRegisterValidateRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/register/validate",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsRegisterValidateResponse.from_mixed(response)

    def get_v2_domains_maintenances(self, request: GetV2DomainsMaintenancesRequest | None = None) -> GetV2DomainsMaintenancesResponse:
        request = request or GetV2DomainsMaintenancesRequest()
        response = self._execute(
            "GET",
            "/v2/domains/maintenances",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2DomainsMaintenancesResponse.from_mixed(response)

    def get_v2_domains_maintenances_maintenance_id(self, request: GetV2DomainsMaintenancesMaintenanceIdRequest | None = None) -> GetV2DomainsMaintenancesMaintenanceIdResponse:
        request = request or GetV2DomainsMaintenancesMaintenanceIdRequest()
        response = self._execute(
            "GET",
            "/v2/domains/maintenances/{maintenanceId}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2DomainsMaintenancesMaintenanceIdResponse.from_mixed(response)

    def get_v2_domains_usage_yyyymm(self, request: GetV2DomainsUsageYyyymmRequest | None = None) -> GetV2DomainsUsageYyyymmResponse:
        request = request or GetV2DomainsUsageYyyymmRequest()
        response = self._execute(
            "GET",
            "/v2/domains/usage/{yyyymm}",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return GetV2DomainsUsageYyyymmResponse.from_mixed(response)

    def patch_v2_customers_customer_id_domains_domain_contacts(self, request: PatchV2CustomersCustomerIdDomainsDomainContactsRequest | None = None) -> PatchV2CustomersCustomerIdDomainsDomainContactsResponse:
        request = request or PatchV2CustomersCustomerIdDomainsDomainContactsRequest()
        response = self._execute(
            "PATCH",
            "/v2/customers/{customerId}/domains/{domain}/contacts",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PatchV2CustomersCustomerIdDomainsDomainContactsResponse.from_mixed(response)

    def post_v2_customers_customer_id_domains_domain_regenerate_auth_code(self, request: PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeRequest | None = None) -> PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeResponse:
        request = request or PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeRequest()
        response = self._execute(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/regenerateAuthCode",
            request.to_path_params(),
            request.to_query_params(),
            request.to_headers(),
            request.to_body(),
        )
        return PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeResponse.from_mixed(response)

    def _map_exception(self, exception: ApiException) -> ApiException:
        if exception.status_code == 400:
            return DomainsBadRequestException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 401:
            return DomainsUnauthorizedException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 403:
            return DomainsForbiddenException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 404:
            return DomainsNotFoundException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 409:
            return DomainsConflictException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 422:
            return DomainsUnprocessableEntityException(*exception.args, error_response=exception.error_response)
        if exception.status_code == 429:
            return DomainsRateLimitException(*exception.args, error_response=exception.error_response)
        if exception.status_code >= 500:
            return DomainsServerException(*exception.args, error_response=exception.error_response)
        return DomainsApiException(*exception.args, error_response=exception.error_response)