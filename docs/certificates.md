# CertificatesService

SSL certificate purchase, validation, lifecycle, and revocation endpoints.

## Accessor

```python
service = client.certificates()
```

## Endpoints

### certificate_create

Calls `POST /v1/certificates`.

```python
response = client.certificates().certificate_create({'sample': True}, 'header-value')
```

```json
{}
```

### certificate_validate

Calls `POST /v1/certificates/validate`.

```python
response = client.certificates().certificate_validate({'sample': True}, 'header-value')
```

```json
{}
```

### certificate_get

Calls `GET /v1/certificates/{certificateId}`.

```python
response = client.certificates().certificate_get('sample')
```

```json
{}
```

### certificate_action_retrieve

Calls `GET /v1/certificates/{certificateId}/actions`.

```python
response = client.certificates().certificate_action_retrieve('sample')
```

```json
{}
```

### certificate_resend_email

Calls `POST /v1/certificates/{certificateId}/email/{emailId}/resend`.

```python
response = client.certificates().certificate_resend_email('sample', 'sample')
```

```json
{}
```

### certificate_alternate_email_address

Calls `POST /v1/certificates/{certificateId}/email/resend/{emailAddress}`.

```python
response = client.certificates().certificate_alternate_email_address('sample', ['sample'])
```

```json
{}
```

### certificate_resend_email_address

Calls `POST /v1/certificates/{certificateId}/email/{emailId}/resend/{emailAddress}`.

```python
response = client.certificates().certificate_resend_email_address('sample', 'sample', ['sample'])
```

```json
{}
```

### certificate_email_history

Calls `GET /v1/certificates/{certificateId}/email/history`.

```python
response = client.certificates().certificate_email_history('sample')
```

```json
{}
```

### certificate_callback_delete

Calls `DELETE /v1/certificates/{certificateId}/callback`.

```python
response = client.certificates().certificate_callback_delete('sample')
```

```json
{}
```

### certificate_callback_get

Calls `GET /v1/certificates/{certificateId}/callback`.

```python
response = client.certificates().certificate_callback_get('sample')
```

```json
{}
```

### certificate_callback_replace

Calls `PUT /v1/certificates/{certificateId}/callback`.

```python
response = client.certificates().certificate_callback_replace('sample', 'sample')
```

```json
{}
```

### certificate_cancel

Calls `POST /v1/certificates/{certificateId}/cancel`.

```python
response = client.certificates().certificate_cancel('sample')
```

```json
{}
```

### certificate_download

Calls `GET /v1/certificates/{certificateId}/download`.

```python
response = client.certificates().certificate_download('sample')
```

```json
{}
```

### certificate_reissue

Calls `POST /v1/certificates/{certificateId}/reissue`.

```python
response = client.certificates().certificate_reissue('sample', {'sample': True})
```

```json
{}
```

### certificate_renew

Calls `POST /v1/certificates/{certificateId}/renew`.

```python
response = client.certificates().certificate_renew('sample', {'sample': True})
```

```json
{}
```

### certificate_revoke

Calls `POST /v1/certificates/{certificateId}/revoke`.

```python
response = client.certificates().certificate_revoke('sample', {'sample': True})
```

```json
{}
```

### certificate_siteseal_get

Calls `GET /v1/certificates/{certificateId}/siteSeal`.

```python
response = client.certificates().certificate_siteseal_get('sample', 'sample', 'sample')
```

```json
{}
```

### certificate_verifydomaincontrol

Calls `POST /v1/certificates/{certificateId}/verifyDomainControl`.

```python
response = client.certificates().certificate_verifydomaincontrol('sample')
```

```json
{}
```

### certificate_get_entitlement

Calls `GET /v2/certificates`.

```python
response = client.certificates().certificate_get_entitlement('sample', True)
```

```json
{}
```

### certificate_create_v2

Calls `POST /v2/certificates`.

```python
response = client.certificates().certificate_create_v2({'sample': True}, 'header-value')
```

```json
{}
```

### certificate_download_entitlement

Calls `GET /v2/certificates/download`.

```python
response = client.certificates().certificate_download_entitlement('sample')
```

```json
{}
```

### get_customer_certificates_by_customer_id

Calls `GET /v2/customers/{customerId}/certificates`.

```python
response = client.certificates().get_customer_certificates_by_customer_id('sample', 1, 1)
```

```json
{}
```

### get_certificate_detail_by_cert_identifier

Calls `GET /v2/customers/{customerId}/certificates/{certificateId}`.

```python
response = client.certificates().get_certificate_detail_by_cert_identifier('sample', 'sample')
```

```json
{}
```

### get_domain_information_by_certificate_id

Calls `GET /v2/customers/{customerId}/certificates/{certificateId}/domainVerifications`.

```python
response = client.certificates().get_domain_information_by_certificate_id('sample', 'sample')
```

```json
{}
```

### get_domain_details_by_domain

Calls `GET /v2/customers/{customerId}/certificates/{certificateId}/domainVerifications/{domain}`.

```python
response = client.certificates().get_domain_details_by_domain('sample', 'sample', 'sample')
```

```json
{}
```

### get_acme_external_account_binding

Calls `GET /v2/customers/{customerId}/certificates/acme/externalAccountBinding`.

```python
response = client.certificates().get_acme_external_account_binding('sample')
```

```json
{}
```

### retrieve_ssl_by_domain_reseller

Calls `GET /v2/certificates/subscriptions/search`.

```python
response = client.certificates().retrieve_ssl_by_domain_reseller(1, 1, 'sample', ['sample'], 'sample', 'sample')
```

```json
{}
```

### retrieve_ssl_by_domain_subscription_reseller

Calls `GET /v2/certificates/subscription/{guid}`.

```python
response = client.certificates().retrieve_ssl_by_domain_subscription_reseller('sample', 1, 1, 'sample', ['sample'], 'sample', 'sample')
```

```json
{}
```

