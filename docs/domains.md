# DomainsService

Domain availability, purchase, management, transfer, and DNS endpoints.

## Accessor

```python
service = client.domains()
```

## Endpoints

### list

Calls `GET /v1/domains`.

```python
response = client.domains().list('header-value', ['sample'], ['sample'], 1, 'sample', ['sample'], 'sample')
```

```json
{}
```

### get_agreement

Calls `GET /v1/domains/agreements`.

```python
response = client.domains().get_agreement(['sample'], True, 'header-value', True)
```

```json
{}
```

### available

Calls `GET /v1/domains/available`.

```python
response = client.domains().available('sample', 'sample', True)
```

```json
{}
```

### available_bulk

Calls `POST /v1/domains/available`.

```python
response = client.domains().available_bulk(['sample'], 'sample')
```

```json
{}
```

### contacts_validate

Calls `POST /v1/domains/contacts/validate`.

```python
response = client.domains().contacts_validate({'sample': True}, 'header-value', 'sample')
```

```json
{}
```

### purchase

Calls `POST /v1/domains/purchase`.

```python
response = client.domains().purchase({'sample': True}, 'header-value')
```

```json
{}
```

### schema

Calls `GET /v1/domains/purchase/schema/{tld}`.

```python
response = client.domains().schema('sample')
```

```json
{}
```

### validate

Calls `POST /v1/domains/purchase/validate`.

```python
response = client.domains().validate({'sample': True})
```

```json
{}
```

### suggest

Calls `GET /v1/domains/suggest`.

```python
response = client.domains().suggest('header-value', 'sample', 'sample', 'sample', ['sample'], ['sample'], 1, 1, 1, 1)
```

```json
{}
```

### tlds

Calls `GET /v1/domains/tlds`.

```python
response = client.domains().tlds()
```

```json
{}
```

### cancel

Calls `DELETE /v1/domains/{domain}`.

```python
response = client.domains().cancel('sample')
```

```json
{}
```

### get

Calls `GET /v1/domains/{domain}`.

```python
response = client.domains().get('sample', 'header-value')
```

```json
{}
```

### update

Calls `PATCH /v1/domains/{domain}`.

```python
response = client.domains().update('sample', {'sample': True}, 'header-value')
```

```json
{}
```

### update_contacts

Calls `PATCH /v1/domains/{domain}/contacts`.

```python
response = client.domains().update_contacts('sample', {'sample': True}, 'header-value')
```

```json
{}
```

### cancel_privacy

Calls `DELETE /v1/domains/{domain}/privacy`.

```python
response = client.domains().cancel_privacy('sample', 'header-value')
```

```json
{}
```

### purchase_privacy

Calls `POST /v1/domains/{domain}/privacy/purchase`.

```python
response = client.domains().purchase_privacy('sample', {'sample': True}, 'header-value')
```

```json
{}
```

### record_add

Calls `PATCH /v1/domains/{domain}/records`.

```python
response = client.domains().record_add('sample', {'sample': True}, 'header-value')
```

```json
{}
```

### record_replace

Calls `PUT /v1/domains/{domain}/records`.

```python
response = client.domains().record_replace('sample', {'sample': True}, 'header-value')
```

```json
{}
```

### record_get

Calls `GET /v1/domains/{domain}/records/{type}/{name}`.

```python
response = client.domains().record_get('sample', 'sample', 'sample', 'header-value', 1, 1)
```

```json
{}
```

### record_replace_type_name

Calls `PUT /v1/domains/{domain}/records/{type}/{name}`.

```python
response = client.domains().record_replace_type_name('sample', 'sample', 'sample', {'sample': True}, 'header-value')
```

```json
{}
```

### record_delete_type_name

Calls `DELETE /v1/domains/{domain}/records/{type}/{name}`.

```python
response = client.domains().record_delete_type_name('sample', 'sample', 'sample', 'header-value')
```

```json
{}
```

### record_replace_type

Calls `PUT /v1/domains/{domain}/records/{type}`.

```python
response = client.domains().record_replace_type('sample', 'sample', {'sample': True}, 'header-value')
```

```json
{}
```

### renew

Calls `POST /v1/domains/{domain}/renew`.

```python
response = client.domains().renew('sample', 'header-value', {'sample': True})
```

```json
{}
```

### transfer_in

Calls `POST /v1/domains/{domain}/transfer`.

```python
response = client.domains().transfer_in('sample', {'sample': True}, 'header-value')
```

```json
{}
```

### verify_email

Calls `POST /v1/domains/{domain}/verifyRegistrantEmail`.

```python
response = client.domains().verify_email('sample', 'header-value')
```

```json
{}
```

### get_v2_customers_customer_id_domains_domain

Calls `GET /v2/customers/{customerId}/domains/{domain}`.

```python
response = client.domains().get_v2_customers_customer_id_domains_domain('sample', 'sample', 'header-value', ['sample'])
```

```json
{}
```

### delete_v2_customers_customer_id_domains_domain_change_of_registrant

Calls `DELETE /v2/customers/{customerId}/domains/{domain}/changeOfRegistrant`.

```python
response = client.domains().delete_v2_customers_customer_id_domains_domain_change_of_registrant('sample', 'sample', 'header-value')
```

```json
{}
```

### get_v2_customers_customer_id_domains_domain_change_of_registrant

Calls `GET /v2/customers/{customerId}/domains/{domain}/changeOfRegistrant`.

```python
response = client.domains().get_v2_customers_customer_id_domains_domain_change_of_registrant('sample', 'sample', 'header-value')
```

```json
{}
```

### patch_v2_customers_customer_id_domains_domain_dnssec_records

Calls `PATCH /v2/customers/{customerId}/domains/{domain}/dnssecRecords`.

```python
response = client.domains().patch_v2_customers_customer_id_domains_domain_dnssec_records('sample', 'sample', {'sample': True}, 'header-value')
```

```json
{}
```

### delete_v2_customers_customer_id_domains_domain_dnssec_records

Calls `DELETE /v2/customers/{customerId}/domains/{domain}/dnssecRecords`.

```python
response = client.domains().delete_v2_customers_customer_id_domains_domain_dnssec_records('sample', 'sample', {'sample': True}, 'header-value')
```

```json
{}
```

### put_v2_customers_customer_id_domains_domain_name_servers

Calls `PUT /v2/customers/{customerId}/domains/{domain}/nameServers`.

```python
response = client.domains().put_v2_customers_customer_id_domains_domain_name_servers('sample', 'sample', {'sample': True}, 'header-value')
```

```json
{}
```

### get_v2_customers_customer_id_domains_domain_privacy_forwarding

Calls `GET /v2/customers/{customerId}/domains/{domain}/privacy/forwarding`.

```python
response = client.domains().get_v2_customers_customer_id_domains_domain_privacy_forwarding('sample', 'sample', 'header-value')
```

```json
{}
```

### patch_v2_customers_customer_id_domains_domain_privacy_forwarding

Calls `PATCH /v2/customers/{customerId}/domains/{domain}/privacy/forwarding`.

```python
response = client.domains().patch_v2_customers_customer_id_domains_domain_privacy_forwarding('sample', 'sample', {'sample': True}, 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_domain_redeem

Calls `POST /v2/customers/{customerId}/domains/{domain}/redeem`.

```python
response = client.domains().post_v2_customers_customer_id_domains_domain_redeem('sample', 'sample', 'header-value', {'sample': True})
```

```json
{}
```

### post_v2_customers_customer_id_domains_domain_renew

Calls `POST /v2/customers/{customerId}/domains/{domain}/renew`.

```python
response = client.domains().post_v2_customers_customer_id_domains_domain_renew('sample', 'sample', {'sample': True}, 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_domain_transfer

Calls `POST /v2/customers/{customerId}/domains/{domain}/transfer`.

```python
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer('sample', 'sample', {'sample': True}, 'header-value')
```

```json
{}
```

### get_v2_customers_customer_id_domains_domain_transfer

Calls `GET /v2/customers/{customerId}/domains/{domain}/transfer`.

```python
response = client.domains().get_v2_customers_customer_id_domains_domain_transfer('sample', 'sample', 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_domain_transfer_validate

Calls `POST /v2/customers/{customerId}/domains/{domain}/transfer/validate`.

```python
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_validate('sample', 'sample', {'sample': True}, 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_domain_transfer_in_accept

Calls `POST /v2/customers/{customerId}/domains/{domain}/transferInAccept`.

```python
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_in_accept('sample', 'sample', {'sample': True}, 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_domain_transfer_in_cancel

Calls `POST /v2/customers/{customerId}/domains/{domain}/transferInCancel`.

```python
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_in_cancel('sample', 'sample', 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_domain_transfer_in_restart

Calls `POST /v2/customers/{customerId}/domains/{domain}/transferInRestart`.

```python
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_in_restart('sample', 'sample', 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_domain_transfer_in_retry

Calls `POST /v2/customers/{customerId}/domains/{domain}/transferInRetry`.

```python
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_in_retry('sample', 'sample', {'sample': True}, 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_domain_transfer_out

Calls `POST /v2/customers/{customerId}/domains/{domain}/transferOut`.

```python
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_out('sample', 'sample', 'sample', 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_domain_transfer_out_accept

Calls `POST /v2/customers/{customerId}/domains/{domain}/transferOutAccept`.

```python
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_out_accept('sample', 'sample', 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_domain_transfer_out_reject

Calls `POST /v2/customers/{customerId}/domains/{domain}/transferOutReject`.

```python
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_out_reject('sample', 'sample', 'header-value', 'sample')
```

```json
{}
```

### domains_forwards_delete

Calls `DELETE /v2/customers/{customerId}/domains/forwards/{fqdn}`.

```python
response = client.domains().domains_forwards_delete('sample', 'sample')
```

```json
{}
```

### domains_forwards_get

Calls `GET /v2/customers/{customerId}/domains/forwards/{fqdn}`.

```python
response = client.domains().domains_forwards_get('sample', 'sample', True)
```

```json
{}
```

### domains_forwards_put

Calls `PUT /v2/customers/{customerId}/domains/forwards/{fqdn}`.

```python
response = client.domains().domains_forwards_put('sample', 'sample', {'sample': True})
```

```json
{}
```

### domains_forwards_post

Calls `POST /v2/customers/{customerId}/domains/forwards/{fqdn}`.

```python
response = client.domains().domains_forwards_post('sample', 'sample', {'sample': True})
```

```json
{}
```

### get_v2_customers_customer_id_domains_domain_actions

Calls `GET /v2/customers/{customerId}/domains/{domain}/actions`.

```python
response = client.domains().get_v2_customers_customer_id_domains_domain_actions('sample', 'sample', 'header-value')
```

```json
{}
```

### delete_v2_customers_customer_id_domains_domain_actions_type

Calls `DELETE /v2/customers/{customerId}/domains/{domain}/actions/{type}`.

```python
response = client.domains().delete_v2_customers_customer_id_domains_domain_actions_type('sample', 'sample', 'sample', 'header-value')
```

```json
{}
```

### get_v2_customers_customer_id_domains_domain_actions_type

Calls `GET /v2/customers/{customerId}/domains/{domain}/actions/{type}`.

```python
response = client.domains().get_v2_customers_customer_id_domains_domain_actions_type('sample', 'sample', 'sample', 'header-value')
```

```json
{}
```

### get_v2_customers_customer_id_domains_notifications

Calls `GET /v2/customers/{customerId}/domains/notifications`.

```python
response = client.domains().get_v2_customers_customer_id_domains_notifications('sample', 'header-value')
```

```json
{}
```

### get_v2_customers_customer_id_domains_notifications_opt_in

Calls `GET /v2/customers/{customerId}/domains/notifications/optIn`.

```python
response = client.domains().get_v2_customers_customer_id_domains_notifications_opt_in('sample', 'header-value')
```

```json
{}
```

### put_v2_customers_customer_id_domains_notifications_opt_in

Calls `PUT /v2/customers/{customerId}/domains/notifications/optIn`.

```python
response = client.domains().put_v2_customers_customer_id_domains_notifications_opt_in('sample', ['sample'], 'header-value')
```

```json
{}
```

### get_v2_customers_customer_id_domains_notifications_schemas_type

Calls `GET /v2/customers/{customerId}/domains/notifications/schemas/{type}`.

```python
response = client.domains().get_v2_customers_customer_id_domains_notifications_schemas_type('sample', 'sample', 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_notifications_notification_id_acknowledge

Calls `POST /v2/customers/{customerId}/domains/notifications/{notificationId}/acknowledge`.

```python
response = client.domains().post_v2_customers_customer_id_domains_notifications_notification_id_acknowledge('sample', 'sample', 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_register

Calls `POST /v2/customers/{customerId}/domains/register`.

```python
response = client.domains().post_v2_customers_customer_id_domains_register('sample', {'sample': True}, 'header-value')
```

```json
{}
```

### get_v2_customers_customer_id_domains_register_schema_tld

Calls `GET /v2/customers/{customerId}/domains/register/schema/{tld}`.

```python
response = client.domains().get_v2_customers_customer_id_domains_register_schema_tld('sample', 'sample', 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_register_validate

Calls `POST /v2/customers/{customerId}/domains/register/validate`.

```python
response = client.domains().post_v2_customers_customer_id_domains_register_validate('sample', {'sample': True}, 'header-value')
```

```json
{}
```

### get_v2_domains_maintenances

Calls `GET /v2/domains/maintenances`.

```python
response = client.domains().get_v2_domains_maintenances('header-value', ['sample'], 'sample', 'sample', 1)
```

```json
{}
```

### get_v2_domains_maintenances_maintenance_id

Calls `GET /v2/domains/maintenances/{maintenanceId}`.

```python
response = client.domains().get_v2_domains_maintenances_maintenance_id('sample', 'header-value')
```

```json
{}
```

### get_v2_domains_usage_yyyymm

Calls `GET /v2/domains/usage/{yyyymm}`.

```python
response = client.domains().get_v2_domains_usage_yyyymm('sample', 'header-value', ['sample'])
```

```json
{}
```

### patch_v2_customers_customer_id_domains_domain_contacts

Calls `PATCH /v2/customers/{customerId}/domains/{domain}/contacts`.

```python
response = client.domains().patch_v2_customers_customer_id_domains_domain_contacts('sample', 'sample', {'sample': True}, 'header-value')
```

```json
{}
```

### post_v2_customers_customer_id_domains_domain_regenerate_auth_code

Calls `POST /v2/customers/{customerId}/domains/{domain}/regenerateAuthCode`.

```python
response = client.domains().post_v2_customers_customer_id_domains_domain_regenerate_auth_code('sample', 'sample', 'header-value')
```

```json
{}
```

