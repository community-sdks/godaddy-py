from .abstract_service import AbstractService

class CertificatesService(AbstractService):
    BASE_URL = "https://api.ote-godaddy.com"

    def __init__(self, client):
        super().__init__(client, self.BASE_URL)

    def certificate_create(self, certificate_create, x_market_id=None, ):
        return self.call(
            "POST",
            "/v1/certificates",
            [],
            [],
            [("X-Market-Id", x_market_id)],
            certificate_create,
        )

    def certificate_validate(self, certificate_create, x_market_id=None, ):
        return self.call(
            "POST",
            "/v1/certificates/validate",
            [],
            [],
            [("X-Market-Id", x_market_id)],
            certificate_create,
        )

    def certificate_get(self, certificate_id, ):
        return self.call(
            "GET",
            "/v1/certificates/{certificateId}",
            [("certificateId", certificate_id)],
            [],
            [],
            None,
        )

    def certificate_action_retrieve(self, certificate_id, ):
        return self.call(
            "GET",
            "/v1/certificates/{certificateId}/actions",
            [("certificateId", certificate_id)],
            [],
            [],
            None,
        )

    def certificate_resend_email(self, certificate_id, email_id, ):
        return self.call(
            "POST",
            "/v1/certificates/{certificateId}/email/{emailId}/resend",
            [("certificateId", certificate_id), ("emailId", email_id)],
            [],
            [],
            None,
        )

    def certificate_alternate_email_address(self, certificate_id, email_address, ):
        return self.call(
            "POST",
            "/v1/certificates/{certificateId}/email/resend/{emailAddress}",
            [("certificateId", certificate_id), ("emailAddress", email_address)],
            [],
            [],
            None,
        )

    def certificate_resend_email_address(self, certificate_id, email_id, email_address, ):
        return self.call(
            "POST",
            "/v1/certificates/{certificateId}/email/{emailId}/resend/{emailAddress}",
            [("certificateId", certificate_id), ("emailId", email_id), ("emailAddress", email_address)],
            [],
            [],
            None,
        )

    def certificate_email_history(self, certificate_id, ):
        return self.call(
            "GET",
            "/v1/certificates/{certificateId}/email/history",
            [("certificateId", certificate_id)],
            [],
            [],
            None,
        )

    def certificate_callback_delete(self, certificate_id, ):
        return self.call(
            "DELETE",
            "/v1/certificates/{certificateId}/callback",
            [("certificateId", certificate_id)],
            [],
            [],
            None,
        )

    def certificate_callback_get(self, certificate_id, ):
        return self.call(
            "GET",
            "/v1/certificates/{certificateId}/callback",
            [("certificateId", certificate_id)],
            [],
            [],
            None,
        )

    def certificate_callback_replace(self, certificate_id, callback_url, ):
        return self.call(
            "PUT",
            "/v1/certificates/{certificateId}/callback",
            [("certificateId", certificate_id)],
            [("callbackUrl", callback_url)],
            [],
            None,
        )

    def certificate_cancel(self, certificate_id, ):
        return self.call(
            "POST",
            "/v1/certificates/{certificateId}/cancel",
            [("certificateId", certificate_id)],
            [],
            [],
            None,
        )

    def certificate_download(self, certificate_id, ):
        return self.call(
            "GET",
            "/v1/certificates/{certificateId}/download",
            [("certificateId", certificate_id)],
            [],
            [],
            None,
        )

    def certificate_reissue(self, certificate_id, reissue_create, ):
        return self.call(
            "POST",
            "/v1/certificates/{certificateId}/reissue",
            [("certificateId", certificate_id)],
            [],
            [],
            reissue_create,
        )

    def certificate_renew(self, certificate_id, renew_create, ):
        return self.call(
            "POST",
            "/v1/certificates/{certificateId}/renew",
            [("certificateId", certificate_id)],
            [],
            [],
            renew_create,
        )

    def certificate_revoke(self, certificate_id, certificate_revoke, ):
        return self.call(
            "POST",
            "/v1/certificates/{certificateId}/revoke",
            [("certificateId", certificate_id)],
            [],
            [],
            certificate_revoke,
        )

    def certificate_siteseal_get(self, certificate_id, theme=None, locale=None, ):
        return self.call(
            "GET",
            "/v1/certificates/{certificateId}/siteSeal",
            [("certificateId", certificate_id)],
            [("theme", theme), ("locale", locale)],
            [],
            None,
        )

    def certificate_verifydomaincontrol(self, certificate_id, ):
        return self.call(
            "POST",
            "/v1/certificates/{certificateId}/verifyDomainControl",
            [("certificateId", certificate_id)],
            [],
            [],
            None,
        )

    def certificate_get_entitlement(self, entitlement_id, latest=None, ):
        return self.call(
            "GET",
            "/v2/certificates",
            [],
            [("entitlementId", entitlement_id), ("latest", latest)],
            [],
            None,
        )

    def certificate_create_v2(self, subscription_certificate_create, x_market_id=None, ):
        return self.call(
            "POST",
            "/v2/certificates",
            [],
            [],
            [("X-Market-Id", x_market_id)],
            subscription_certificate_create,
        )

    def certificate_download_entitlement(self, entitlement_id, ):
        return self.call(
            "GET",
            "/v2/certificates/download",
            [],
            [("entitlementId", entitlement_id)],
            [],
            None,
        )

    def get_customer_certificates_by_customer_id(self, customer_id, offset=None, limit=None, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/certificates",
            [("customerId", customer_id)],
            [("offset", offset), ("limit", limit)],
            [],
            None,
        )

    def get_certificate_detail_by_cert_identifier(self, customer_id, certificate_id, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/certificates/{certificateId}",
            [("customerId", customer_id), ("certificateId", certificate_id)],
            [],
            [],
            None,
        )

    def get_domain_information_by_certificate_id(self, customer_id, certificate_id, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/certificates/{certificateId}/domainVerifications",
            [("customerId", customer_id), ("certificateId", certificate_id)],
            [],
            [],
            None,
        )

    def get_domain_details_by_domain(self, customer_id, certificate_id, domain, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/certificates/{certificateId}/domainVerifications/{domain}",
            [("customerId", customer_id), ("certificateId", certificate_id), ("domain", domain)],
            [],
            [],
            None,
        )

    def get_acme_external_account_binding(self, customer_id, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/certificates/acme/externalAccountBinding",
            [("customerId", customer_id)],
            [],
            [],
            None,
        )

    def retrieve_ssl_by_domain_reseller(self, page_size=None, page=None, domain=None, status=None, type=None, validation=None, ):
        return self.call(
            "GET",
            "/v2/certificates/subscriptions/search",
            [],
            [("pageSize", page_size), ("page", page), ("domain", domain), ("status", status), ("type", type), ("validation", validation)],
            [],
            None,
        )

    def retrieve_ssl_by_domain_subscription_reseller(self, guid, page_size=None, page=None, domain=None, status=None, type=None, validation=None, ):
        return self.call(
            "GET",
            "/v2/certificates/subscription/{guid}",
            [("guid", guid)],
            [("pageSize", page_size), ("page", page), ("domain", domain), ("status", status), ("type", type), ("validation", validation)],
            [],
            None,
        )
