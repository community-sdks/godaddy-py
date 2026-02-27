from .abstract_service import AbstractService

class DomainsService(AbstractService):
    BASE_URL = "https://api.ote-godaddy.com"

    def __init__(self, client):
        super().__init__(client, self.BASE_URL)

    def list(self, x_shopper_id=None, statuses=None, status_groups=None, limit=None, marker=None, includes=None, modified_date=None, ):
        return self.call(
            "GET",
            "/v1/domains",
            [],
            [("statuses", statuses), ("statusGroups", status_groups), ("limit", limit), ("marker", marker), ("includes", includes), ("modifiedDate", modified_date)],
            [("X-Shopper-Id", x_shopper_id)],
            None,
        )

    def get_agreement(self, tlds, privacy, x_market_id=None, for_transfer=None, ):
        return self.call(
            "GET",
            "/v1/domains/agreements",
            [],
            [("tlds", tlds), ("privacy", privacy), ("forTransfer", for_transfer)],
            [("X-Market-Id", x_market_id)],
            None,
        )

    def available(self, domain, check_type=None, for_transfer=None, ):
        return self.call(
            "GET",
            "/v1/domains/available",
            [],
            [("domain", domain), ("checkType", check_type), ("forTransfer", for_transfer)],
            [],
            None,
        )

    def available_bulk(self, domains, check_type=None, ):
        return self.call(
            "POST",
            "/v1/domains/available",
            [],
            [("checkType", check_type)],
            [],
            domains,
        )

    def contacts_validate(self, body, x_private_label_id=None, market_id=None, ):
        return self.call(
            "POST",
            "/v1/domains/contacts/validate",
            [],
            [("marketId", market_id)],
            [("X-Private-Label-Id", x_private_label_id)],
            body,
        )

    def purchase(self, body, x_shopper_id=None, ):
        return self.call(
            "POST",
            "/v1/domains/purchase",
            [],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            body,
        )

    def schema(self, tld, ):
        return self.call(
            "GET",
            "/v1/domains/purchase/schema/{tld}",
            [("tld", tld)],
            [],
            [],
            None,
        )

    def validate(self, body, ):
        return self.call(
            "POST",
            "/v1/domains/purchase/validate",
            [],
            [],
            [],
            body,
        )

    def suggest(self, x_shopper_id=None, query=None, country=None, city=None, sources=None, tlds=None, length_max=None, length_min=None, limit=None, wait_ms=None, ):
        return self.call(
            "GET",
            "/v1/domains/suggest",
            [],
            [("query", query), ("country", country), ("city", city), ("sources", sources), ("tlds", tlds), ("lengthMax", length_max), ("lengthMin", length_min), ("limit", limit), ("waitMs", wait_ms)],
            [("X-Shopper-Id", x_shopper_id)],
            None,
        )

    def tlds(self, ):
        return self.call(
            "GET",
            "/v1/domains/tlds",
            [],
            [],
            [],
            None,
        )

    def cancel(self, domain, ):
        return self.call(
            "DELETE",
            "/v1/domains/{domain}",
            [("domain", domain)],
            [],
            [],
            None,
        )

    def get(self, domain, x_shopper_id=None, ):
        return self.call(
            "GET",
            "/v1/domains/{domain}",
            [("domain", domain)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            None,
        )

    def update(self, domain, body, x_shopper_id=None, ):
        return self.call(
            "PATCH",
            "/v1/domains/{domain}",
            [("domain", domain)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            body,
        )

    def update_contacts(self, domain, contacts, x_shopper_id=None, ):
        return self.call(
            "PATCH",
            "/v1/domains/{domain}/contacts",
            [("domain", domain)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            contacts,
        )

    def cancel_privacy(self, domain, x_shopper_id=None, ):
        return self.call(
            "DELETE",
            "/v1/domains/{domain}/privacy",
            [("domain", domain)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            None,
        )

    def purchase_privacy(self, domain, body, x_shopper_id=None, ):
        return self.call(
            "POST",
            "/v1/domains/{domain}/privacy/purchase",
            [("domain", domain)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            body,
        )

    def record_add(self, domain, records, x_shopper_id=None, ):
        return self.call(
            "PATCH",
            "/v1/domains/{domain}/records",
            [("domain", domain)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            records,
        )

    def record_replace(self, domain, records, x_shopper_id=None, ):
        return self.call(
            "PUT",
            "/v1/domains/{domain}/records",
            [("domain", domain)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            records,
        )

    def record_get(self, domain, type, name, x_shopper_id=None, offset=None, limit=None, ):
        return self.call(
            "GET",
            "/v1/domains/{domain}/records/{type}/{name}",
            [("domain", domain), ("type", type), ("name", name)],
            [("offset", offset), ("limit", limit)],
            [("X-Shopper-Id", x_shopper_id)],
            None,
        )

    def record_replace_type_name(self, domain, type, name, records, x_shopper_id=None, ):
        return self.call(
            "PUT",
            "/v1/domains/{domain}/records/{type}/{name}",
            [("domain", domain), ("type", type), ("name", name)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            records,
        )

    def record_delete_type_name(self, domain, type, name, x_shopper_id=None, ):
        return self.call(
            "DELETE",
            "/v1/domains/{domain}/records/{type}/{name}",
            [("domain", domain), ("type", type), ("name", name)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            None,
        )

    def record_replace_type(self, domain, type, records, x_shopper_id=None, ):
        return self.call(
            "PUT",
            "/v1/domains/{domain}/records/{type}",
            [("domain", domain), ("type", type)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            records,
        )

    def renew(self, domain, x_shopper_id=None, body=None, ):
        return self.call(
            "POST",
            "/v1/domains/{domain}/renew",
            [("domain", domain)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            body,
        )

    def transfer_in(self, domain, body, x_shopper_id=None, ):
        return self.call(
            "POST",
            "/v1/domains/{domain}/transfer",
            [("domain", domain)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            body,
        )

    def verify_email(self, domain, x_shopper_id=None, ):
        return self.call(
            "POST",
            "/v1/domains/{domain}/verifyRegistrantEmail",
            [("domain", domain)],
            [],
            [("X-Shopper-Id", x_shopper_id)],
            None,
        )

    def get_v2_customers_customer_id_domains_domain(self, customer_id, domain, x_request_id=None, includes=None, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/domains/{domain}",
            [("customerId", customer_id), ("domain", domain)],
            [("includes", includes)],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def delete_v2_customers_customer_id_domains_domain_change_of_registrant(self, customer_id, domain, x_request_id=None, ):
        return self.call(
            "DELETE",
            "/v2/customers/{customerId}/domains/{domain}/changeOfRegistrant",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def get_v2_customers_customer_id_domains_domain_change_of_registrant(self, customer_id, domain, x_request_id=None, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/domains/{domain}/changeOfRegistrant",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def patch_v2_customers_customer_id_domains_domain_dnssec_records(self, customer_id, domain, body, x_request_id=None, ):
        return self.call(
            "PATCH",
            "/v2/customers/{customerId}/domains/{domain}/dnssecRecords",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def delete_v2_customers_customer_id_domains_domain_dnssec_records(self, customer_id, domain, body, x_request_id=None, ):
        return self.call(
            "DELETE",
            "/v2/customers/{customerId}/domains/{domain}/dnssecRecords",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def put_v2_customers_customer_id_domains_domain_name_servers(self, customer_id, domain, body, x_request_id=None, ):
        return self.call(
            "PUT",
            "/v2/customers/{customerId}/domains/{domain}/nameServers",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def get_v2_customers_customer_id_domains_domain_privacy_forwarding(self, customer_id, domain, x_request_id=None, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/domains/{domain}/privacy/forwarding",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def patch_v2_customers_customer_id_domains_domain_privacy_forwarding(self, customer_id, domain, body, x_request_id=None, ):
        return self.call(
            "PATCH",
            "/v2/customers/{customerId}/domains/{domain}/privacy/forwarding",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def post_v2_customers_customer_id_domains_domain_redeem(self, customer_id, domain, x_request_id=None, body=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/redeem",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def post_v2_customers_customer_id_domains_domain_renew(self, customer_id, domain, body, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/renew",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def post_v2_customers_customer_id_domains_domain_transfer(self, customer_id, domain, body, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transfer",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def get_v2_customers_customer_id_domains_domain_transfer(self, customer_id, domain, x_request_id=None, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/domains/{domain}/transfer",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def post_v2_customers_customer_id_domains_domain_transfer_validate(self, customer_id, domain, body, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transfer/validate",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def post_v2_customers_customer_id_domains_domain_transfer_in_accept(self, customer_id, domain, body, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferInAccept",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def post_v2_customers_customer_id_domains_domain_transfer_in_cancel(self, customer_id, domain, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferInCancel",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def post_v2_customers_customer_id_domains_domain_transfer_in_restart(self, customer_id, domain, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferInRestart",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def post_v2_customers_customer_id_domains_domain_transfer_in_retry(self, customer_id, domain, body, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferInRetry",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def post_v2_customers_customer_id_domains_domain_transfer_out(self, customer_id, domain, registrar, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferOut",
            [("customerId", customer_id), ("domain", domain)],
            [("registrar", registrar)],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def post_v2_customers_customer_id_domains_domain_transfer_out_accept(self, customer_id, domain, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferOutAccept",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def post_v2_customers_customer_id_domains_domain_transfer_out_reject(self, customer_id, domain, x_request_id=None, reason=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/transferOutReject",
            [("customerId", customer_id), ("domain", domain)],
            [("reason", reason)],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def domains_forwards_delete(self, customer_id, fqdn, ):
        return self.call(
            "DELETE",
            "/v2/customers/{customerId}/domains/forwards/{fqdn}",
            [("customerId", customer_id), ("fqdn", fqdn)],
            [],
            [],
            None,
        )

    def domains_forwards_get(self, customer_id, fqdn, include_subs=None, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/domains/forwards/{fqdn}",
            [("customerId", customer_id), ("fqdn", fqdn)],
            [("includeSubs", include_subs)],
            [],
            None,
        )

    def domains_forwards_put(self, customer_id, fqdn, body, ):
        return self.call(
            "PUT",
            "/v2/customers/{customerId}/domains/forwards/{fqdn}",
            [("customerId", customer_id), ("fqdn", fqdn)],
            [],
            [],
            body,
        )

    def domains_forwards_post(self, customer_id, fqdn, body, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/forwards/{fqdn}",
            [("customerId", customer_id), ("fqdn", fqdn)],
            [],
            [],
            body,
        )

    def get_v2_customers_customer_id_domains_domain_actions(self, customer_id, domain, x_request_id=None, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/domains/{domain}/actions",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def delete_v2_customers_customer_id_domains_domain_actions_type(self, customer_id, domain, type, x_request_id=None, ):
        return self.call(
            "DELETE",
            "/v2/customers/{customerId}/domains/{domain}/actions/{type}",
            [("customerId", customer_id), ("domain", domain), ("type", type)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def get_v2_customers_customer_id_domains_domain_actions_type(self, customer_id, domain, type, x_request_id=None, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/domains/{domain}/actions/{type}",
            [("customerId", customer_id), ("domain", domain), ("type", type)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def get_v2_customers_customer_id_domains_notifications(self, customer_id, x_request_id=None, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/domains/notifications",
            [("customerId", customer_id)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def get_v2_customers_customer_id_domains_notifications_opt_in(self, customer_id, x_request_id=None, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/domains/notifications/optIn",
            [("customerId", customer_id)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def put_v2_customers_customer_id_domains_notifications_opt_in(self, customer_id, types, x_request_id=None, ):
        return self.call(
            "PUT",
            "/v2/customers/{customerId}/domains/notifications/optIn",
            [("customerId", customer_id)],
            [("types", types)],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def get_v2_customers_customer_id_domains_notifications_schemas_type(self, customer_id, type, x_request_id=None, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/domains/notifications/schemas/{type}",
            [("customerId", customer_id), ("type", type)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def post_v2_customers_customer_id_domains_notifications_notification_id_acknowledge(self, customer_id, notification_id, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/notifications/{notificationId}/acknowledge",
            [("customerId", customer_id), ("notificationId", notification_id)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def post_v2_customers_customer_id_domains_register(self, customer_id, body, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/register",
            [("customerId", customer_id)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def get_v2_customers_customer_id_domains_register_schema_tld(self, customer_id, tld, x_request_id=None, ):
        return self.call(
            "GET",
            "/v2/customers/{customerId}/domains/register/schema/{tld}",
            [("customerId", customer_id), ("tld", tld)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def post_v2_customers_customer_id_domains_register_validate(self, customer_id, body, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/register/validate",
            [("customerId", customer_id)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def get_v2_domains_maintenances(self, x_request_id=None, status=None, modified_at_after=None, starts_at_after=None, limit=None, ):
        return self.call(
            "GET",
            "/v2/domains/maintenances",
            [],
            [("status", status), ("modifiedAtAfter", modified_at_after), ("startsAtAfter", starts_at_after), ("limit", limit)],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def get_v2_domains_maintenances_maintenance_id(self, maintenance_id, x_request_id=None, ):
        return self.call(
            "GET",
            "/v2/domains/maintenances/{maintenanceId}",
            [("maintenanceId", maintenance_id)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def get_v2_domains_usage_yyyymm(self, yyyymm, x_request_id=None, includes=None, ):
        return self.call(
            "GET",
            "/v2/domains/usage/{yyyymm}",
            [("yyyymm", yyyymm)],
            [("includes", includes)],
            [("X-Request-Id", x_request_id)],
            None,
        )

    def patch_v2_customers_customer_id_domains_domain_contacts(self, customer_id, domain, body, x_request_id=None, ):
        return self.call(
            "PATCH",
            "/v2/customers/{customerId}/domains/{domain}/contacts",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            body,
        )

    def post_v2_customers_customer_id_domains_domain_regenerate_auth_code(self, customer_id, domain, x_request_id=None, ):
        return self.call(
            "POST",
            "/v2/customers/{customerId}/domains/{domain}/regenerateAuthCode",
            [("customerId", customer_id), ("domain", domain)],
            [],
            [("X-Request-Id", x_request_id)],
            None,
        )
