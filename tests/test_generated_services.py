from godaddy_python import Client, Config
from godaddy_python.http import HttpResponse
from tests.support import TestTransport

def test_every_service_method_builds_a_request():
    transport = TestTransport()
    client = Client(Config(api_key="key", api_secret="secret", max_retries=0), transport)
    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.abuse().get_tickets('sample', True, 'sample', 'sample', 'sample', 'sample', 1, 1)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.abuse().create_ticket({'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.abuse().get_ticket_info('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.abuse().get_tickets_v2('sample', True, 'sample', 'sample', 'sample', 'sample', 1, 1)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.abuse().create_ticket_v2({'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.abuse().get_ticket_info_v2('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.aftermarket().get_listings('sample', ['sample'], ['sample'], 'sample', 'sample', 1, 1)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.aftermarket().delete_listings(['sample'])
    request = transport.requests[before]
    assert request.method == "DELETE"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.aftermarket().add_expiry_listings(['sample'])
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.agreements().get(['sample'], 'header-value', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.ans().search_ans_name('sample', 'sample', 'sample', 'sample', 1, 1)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.ans().register_agent({'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.ans().resolve_ans_name({'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.ans().get_agent('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.ans().validate_registration('sample')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.ans().verify_dns_records('sample')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.ans().get_agent_identity_certificate_by_agent_id('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.ans().submit_agent_identity_csr_by_agent_id('sample', {'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.ans().get_agent_server_certificate_by_agent_id('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.ans().submit_agent_server_csr_by_agent_id('sample', {'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.ans().get_agent_csr_status_by_agent_id('sample', 'sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.ans().get_agent_events('header-value', 'sample', 'sample', 1)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.auctions().place_bids('sample', {'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_create({'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_validate({'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_get('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_action_retrieve('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_resend_email('sample', 'sample')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_alternate_email_address('sample', ['sample'])
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_resend_email_address('sample', 'sample', ['sample'])
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_email_history('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_callback_delete('sample')
    request = transport.requests[before]
    assert request.method == "DELETE"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_callback_get('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_callback_replace('sample', 'sample')
    request = transport.requests[before]
    assert request.method == "PUT"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_cancel('sample')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_download('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_reissue('sample', {'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_renew('sample', {'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_revoke('sample', {'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_siteseal_get('sample', 'sample', 'sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_verifydomaincontrol('sample')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_get_entitlement('sample', True)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_create_v2({'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().certificate_download_entitlement('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().get_customer_certificates_by_customer_id('sample', 1, 1)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().get_certificate_detail_by_cert_identifier('sample', 'sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().get_domain_information_by_certificate_id('sample', 'sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().get_domain_details_by_domain('sample', 'sample', 'sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().get_acme_external_account_binding('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().retrieve_ssl_by_domain_reseller(1, 1, 'sample', ['sample'], 'sample', 'sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.certificates().retrieve_ssl_by_domain_subscription_reseller('sample', 1, 1, 'sample', ['sample'], 'sample', 'sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.countries().get_countries('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.countries().get_country('sample', 'sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().list('header-value', ['sample'], ['sample'], 1, 'sample', ['sample'], 'sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_agreement(['sample'], True, 'header-value', True)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().available('sample', 'sample', True)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().available_bulk(['sample'], 'sample')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().contacts_validate({'sample': True}, 'header-value', 'sample')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().purchase({'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().schema('sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().validate({'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().suggest('header-value', 'sample', 'sample', 'sample', ['sample'], ['sample'], 1, 1, 1, 1)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().tlds()
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().cancel('sample')
    request = transport.requests[before]
    assert request.method == "DELETE"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get('sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().update('sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "PATCH"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().update_contacts('sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "PATCH"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().cancel_privacy('sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "DELETE"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().purchase_privacy('sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().record_add('sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "PATCH"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().record_replace('sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "PUT"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().record_get('sample', 'sample', 'sample', 'header-value', 1, 1)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().record_replace_type_name('sample', 'sample', 'sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "PUT"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().record_delete_type_name('sample', 'sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "DELETE"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().record_replace_type('sample', 'sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "PUT"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().renew('sample', 'header-value', {'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().transfer_in('sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().verify_email('sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_customers_customer_id_domains_domain('sample', 'sample', 'header-value', ['sample'])
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().delete_v2_customers_customer_id_domains_domain_change_of_registrant('sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "DELETE"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_customers_customer_id_domains_domain_change_of_registrant('sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().patch_v2_customers_customer_id_domains_domain_dnssec_records('sample', 'sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "PATCH"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().delete_v2_customers_customer_id_domains_domain_dnssec_records('sample', 'sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "DELETE"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().put_v2_customers_customer_id_domains_domain_name_servers('sample', 'sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "PUT"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_customers_customer_id_domains_domain_privacy_forwarding('sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().patch_v2_customers_customer_id_domains_domain_privacy_forwarding('sample', 'sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "PATCH"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_domain_redeem('sample', 'sample', 'header-value', {'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_domain_renew('sample', 'sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_domain_transfer('sample', 'sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_customers_customer_id_domains_domain_transfer('sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_domain_transfer_validate('sample', 'sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_domain_transfer_in_accept('sample', 'sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_domain_transfer_in_cancel('sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_domain_transfer_in_restart('sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_domain_transfer_in_retry('sample', 'sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_domain_transfer_out('sample', 'sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_domain_transfer_out_accept('sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_domain_transfer_out_reject('sample', 'sample', 'header-value', 'sample')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().domains_forwards_delete('sample', 'sample')
    request = transport.requests[before]
    assert request.method == "DELETE"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().domains_forwards_get('sample', 'sample', True)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().domains_forwards_put('sample', 'sample', {'sample': True})
    request = transport.requests[before]
    assert request.method == "PUT"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().domains_forwards_post('sample', 'sample', {'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_customers_customer_id_domains_domain_actions('sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().delete_v2_customers_customer_id_domains_domain_actions_type('sample', 'sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "DELETE"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_customers_customer_id_domains_domain_actions_type('sample', 'sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_customers_customer_id_domains_notifications('sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_customers_customer_id_domains_notifications_opt_in('sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().put_v2_customers_customer_id_domains_notifications_opt_in('sample', ['sample'], 'header-value')
    request = transport.requests[before]
    assert request.method == "PUT"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_customers_customer_id_domains_notifications_schemas_type('sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_notifications_notification_id_acknowledge('sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_register('sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_customers_customer_id_domains_register_schema_tld('sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_register_validate('sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_domains_maintenances('header-value', ['sample'], 'sample', 'sample', 1)
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_domains_maintenances_maintenance_id('sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().get_v2_domains_usage_yyyymm('sample', 'header-value', ['sample'])
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().patch_v2_customers_customer_id_domains_domain_contacts('sample', 'sample', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "PATCH"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.domains().post_v2_customers_customer_id_domains_domain_regenerate_auth_code('sample', 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.orders().list('header-value', 'sample', 'sample', 'sample', 'sample', 'sample', 'sample', 1, 1, 'sample', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.orders().get('sample', 'header-value', 'header-value', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.parking().get_metrics('sample', 'sample', 'sample', 1, 1, 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.parking().get_metrics_by_domain('sample', 'sample', 'sample', ['sample'], 'sample', 'sample', 1, 1, 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.shoppers().create_subaccount({'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.shoppers().get({'sample': True}, ['sample'])
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.shoppers().update({'sample': True}, {'sample': True})
    request = transport.requests[before]
    assert request.method == "POST"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.shoppers().delete({'sample': True}, 'sample')
    request = transport.requests[before]
    assert request.method == "DELETE"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.shoppers().get_status({'sample': True}, 'sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.shoppers().change_password({'sample': True}, {'sample': True})
    request = transport.requests[before]
    assert request.method == "PUT"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.subscriptions().list('header-value', 'header-value', 'header-value', ['sample'], ['sample'], 1, 1, 'sample')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.subscriptions().product_groups('header-value', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.subscriptions().cancel({'sample': True}, 'header-value', 'header-value')
    request = transport.requests[before]
    assert request.method == "DELETE"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.subscriptions().get({'sample': True}, 'header-value', 'header-value')
    request = transport.requests[before]
    assert request.method == "GET"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

    transport.push(HttpResponse(200, {"content-type": "application/json"}, "{}"))
    before = len(transport.requests)
    client.subscriptions().update({'sample': True}, 'header-value', {'sample': True}, 'header-value')
    request = transport.requests[before]
    assert request.method == "PATCH"
    assert request.headers["Authorization"] == "sso-key key:secret"
    assert "{" not in request.url

