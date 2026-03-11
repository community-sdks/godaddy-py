# CertificatesService

## Accessor

```python
service = client.certificates()
```

## Method Index

- `certificate_create`: `CertificateCreateResponse`
- `certificate_validate`: `CertificateValidateResponse`
- `certificate_get`: `CertificateGetResponse`
- `certificate_action_retrieve`: `CertificateActionRetrieveResponse`
- `certificate_resend_email`: `CertificateResendEmailResponse`
- `certificate_alternate_email_address`: `CertificateAlternateEmailAddressResponse`
- `certificate_resend_email_address`: `CertificateResendEmailAddressResponse`
- `certificate_email_history`: `CertificateEmailHistoryResponse`
- `certificate_callback_get`: `CertificateCallbackGetResponse`
- `certificate_callback_replace`: `CertificateCallbackReplaceResponse`
- `certificate_callback_delete`: `CertificateCallbackDeleteResponse`
- `certificate_cancel`: `CertificateCancelResponse`
- `certificate_download`: `CertificateDownloadResponse`
- `certificate_reissue`: `CertificateReissueResponse`
- `certificate_renew`: `CertificateRenewResponse`
- `certificate_revoke`: `CertificateRevokeResponse`
- `certificate_siteseal_get`: `CertificateSitesealGetResponse`
- `certificate_verifydomaincontrol`: `CertificateVerifydomaincontrolResponse`
- `certificate_get_entitlement`: `CertificateGetEntitlementResponse`
- `certificate_create`: `CertificateCreateResponse`
- `certificate_download_entitlement`: `CertificateDownloadEntitlementResponse`
- `get_customer_certificates_by_customer_id`: `GetCustomerCertificatesByCustomerIdResponse`
- `get_certificate_detail_by_cert_identifier`: `GetCertificateDetailByCertIdentifierResponse`
- `get_domain_information_by_certificate_id`: `GetDomainInformationByCertificateIdResponse`
- `get_domain_details_by_domain`: `GetDomainDetailsByDomainResponse`
- `get_acme_external_account_binding`: `GetAcmeExternalAccountBindingResponse`
- `retrieve_ssl_by_domain_reseller`: `RetrieveSslByDomainResellerResponse`
- `retrieve_ssl_by_domain_subscription_reseller`: `RetrieveSslByDomainSubscriptionResellerResponse`

### certificate_create

Returns: `CertificateCreateResponse`

```python
from godaddy.dto.certificates.requests import CertificateCreateRequest
request = CertificateCreateRequest(
    x_market_id='abc123',
    certificate_create='value',
)
response = client.certificates().certificate_create(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_validate

Returns: `CertificateValidateResponse`

```python
from godaddy.dto.certificates.requests import CertificateValidateRequest
request = CertificateValidateRequest(
    x_market_id='abc123',
    certificate_create='value',
)
response = client.certificates().certificate_validate(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_get

Returns: `CertificateGetResponse`

```python
from godaddy.dto.certificates.requests import CertificateGetRequest
request = CertificateGetRequest(
    certificate_id='abc123',
)
response = client.certificates().certificate_get(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_action_retrieve

Returns: `CertificateActionRetrieveResponse`

```python
from godaddy.dto.certificates.requests import CertificateActionRetrieveRequest
request = CertificateActionRetrieveRequest(
    certificate_id='abc123',
)
response = client.certificates().certificate_action_retrieve(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_resend_email

Returns: `CertificateResendEmailResponse`

```python
from godaddy.dto.certificates.requests import CertificateResendEmailRequest
request = CertificateResendEmailRequest(
    certificate_id='abc123',
    email_id='admin@example.com',
)
response = client.certificates().certificate_resend_email(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_alternate_email_address

Returns: `CertificateAlternateEmailAddressResponse`

```python
from godaddy.dto.certificates.requests import CertificateAlternateEmailAddressRequest
request = CertificateAlternateEmailAddressRequest(
    certificate_id='abc123',
    email_address='admin@example.com',
)
response = client.certificates().certificate_alternate_email_address(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_resend_email_address

Returns: `CertificateResendEmailAddressResponse`

```python
from godaddy.dto.certificates.requests import CertificateResendEmailAddressRequest
request = CertificateResendEmailAddressRequest(
    certificate_id='abc123',
    email_id='admin@example.com',
    email_address='admin@example.com',
)
response = client.certificates().certificate_resend_email_address(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_email_history

Returns: `CertificateEmailHistoryResponse`

```python
from godaddy.dto.certificates.requests import CertificateEmailHistoryRequest
request = CertificateEmailHistoryRequest(
    certificate_id='abc123',
)
response = client.certificates().certificate_email_history(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_callback_get

Returns: `CertificateCallbackGetResponse`

```python
from godaddy.dto.certificates.requests import CertificateCallbackGetRequest
request = CertificateCallbackGetRequest(
    certificate_id='abc123',
)
response = client.certificates().certificate_callback_get(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_callback_replace

Returns: `CertificateCallbackReplaceResponse`

```python
from godaddy.dto.certificates.requests import CertificateCallbackReplaceRequest
request = CertificateCallbackReplaceRequest(
    certificate_id='abc123',
    callback_url='value',
)
response = client.certificates().certificate_callback_replace(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_callback_delete

Returns: `CertificateCallbackDeleteResponse`

```python
from godaddy.dto.certificates.requests import CertificateCallbackDeleteRequest
request = CertificateCallbackDeleteRequest(
    certificate_id='abc123',
)
response = client.certificates().certificate_callback_delete(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_cancel

Returns: `CertificateCancelResponse`

```python
from godaddy.dto.certificates.requests import CertificateCancelRequest
request = CertificateCancelRequest(
    certificate_id='abc123',
)
response = client.certificates().certificate_cancel(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_download

Returns: `CertificateDownloadResponse`

```python
from godaddy.dto.certificates.requests import CertificateDownloadRequest
request = CertificateDownloadRequest(
    certificate_id='abc123',
)
response = client.certificates().certificate_download(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_reissue

Returns: `CertificateReissueResponse`

```python
from godaddy.dto.certificates.requests import CertificateReissueRequest
request = CertificateReissueRequest(
    certificate_id='abc123',
    reissue_create='value',
)
response = client.certificates().certificate_reissue(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_renew

Returns: `CertificateRenewResponse`

```python
from godaddy.dto.certificates.requests import CertificateRenewRequest
request = CertificateRenewRequest(
    certificate_id='abc123',
    renew_create='value',
)
response = client.certificates().certificate_renew(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_revoke

Returns: `CertificateRevokeResponse`

```python
from godaddy.dto.certificates.requests import CertificateRevokeRequest
request = CertificateRevokeRequest(
    certificate_id='abc123',
    certificate_revoke='value',
)
response = client.certificates().certificate_revoke(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_siteseal_get

Returns: `CertificateSitesealGetResponse`

```python
from godaddy.dto.certificates.requests import CertificateSitesealGetRequest
request = CertificateSitesealGetRequest(
    certificate_id='abc123',
    theme='value',
    locale='value',
)
response = client.certificates().certificate_siteseal_get(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_verifydomaincontrol

Returns: `CertificateVerifydomaincontrolResponse`

```python
from godaddy.dto.certificates.requests import CertificateVerifydomaincontrolRequest
request = CertificateVerifydomaincontrolRequest(
    certificate_id='abc123',
)
response = client.certificates().certificate_verifydomaincontrol(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_get_entitlement

Returns: `CertificateGetEntitlementResponse`

```python
from godaddy.dto.certificates.requests import CertificateGetEntitlementRequest
request = CertificateGetEntitlementRequest(
    entitlement_id='abc123',
    latest=True,
)
response = client.certificates().certificate_get_entitlement(request)
```

```json
[]
```

### certificate_create

Returns: `CertificateCreateResponse`

```python
from godaddy.dto.certificates.requests import CertificateCreateRequest
request = CertificateCreateRequest(
    x_market_id='abc123',
    subscription_certificate_create='value',
)
response = client.certificates().certificate_create(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### certificate_download_entitlement

Returns: `CertificateDownloadEntitlementResponse`

```python
from godaddy.dto.certificates.requests import CertificateDownloadEntitlementRequest
request = CertificateDownloadEntitlementRequest(
    entitlement_id='abc123',
)
response = client.certificates().certificate_download_entitlement(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_customer_certificates_by_customer_id

Returns: `GetCustomerCertificatesByCustomerIdResponse`

```python
from godaddy.dto.certificates.requests import GetCustomerCertificatesByCustomerIdRequest
request = GetCustomerCertificatesByCustomerIdRequest(
    undefined='value',
    undefined='value',
    undefined='value',
)
response = client.certificates().get_customer_certificates_by_customer_id(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_certificate_detail_by_cert_identifier

Returns: `GetCertificateDetailByCertIdentifierResponse`

```python
from godaddy.dto.certificates.requests import GetCertificateDetailByCertIdentifierRequest
request = GetCertificateDetailByCertIdentifierRequest(
    undefined='value',
    undefined='value',
)
response = client.certificates().get_certificate_detail_by_cert_identifier(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_domain_information_by_certificate_id

Returns: `GetDomainInformationByCertificateIdResponse`

```python
from godaddy.dto.certificates.requests import GetDomainInformationByCertificateIdRequest
request = GetDomainInformationByCertificateIdRequest(
    undefined='value',
    undefined='value',
)
response = client.certificates().get_domain_information_by_certificate_id(request)
```

```json
[]
```

### get_domain_details_by_domain

Returns: `GetDomainDetailsByDomainResponse`

```python
from godaddy.dto.certificates.requests import GetDomainDetailsByDomainRequest
request = GetDomainDetailsByDomainRequest(
    undefined='value',
    undefined='value',
    undefined='value',
)
response = client.certificates().get_domain_details_by_domain(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_acme_external_account_binding

Returns: `GetAcmeExternalAccountBindingResponse`

```python
from godaddy.dto.certificates.requests import GetAcmeExternalAccountBindingRequest
request = GetAcmeExternalAccountBindingRequest(
    undefined='value',
)
response = client.certificates().get_acme_external_account_binding(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### retrieve_ssl_by_domain_reseller

Returns: `RetrieveSslByDomainResellerResponse`

```python
from godaddy.dto.certificates.requests import RetrieveSslByDomainResellerRequest
request = RetrieveSslByDomainResellerRequest(
    undefined='value',
    undefined='value',
    undefined='value',
    undefined='value',
)
response = client.certificates().retrieve_ssl_by_domain_reseller(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### retrieve_ssl_by_domain_subscription_reseller

Returns: `RetrieveSslByDomainSubscriptionResellerResponse`

```python
from godaddy.dto.certificates.requests import RetrieveSslByDomainSubscriptionResellerRequest
request = RetrieveSslByDomainSubscriptionResellerRequest(
    undefined='value',
    undefined='value',
    undefined='value',
    undefined='value',
)
response = client.certificates().retrieve_ssl_by_domain_subscription_reseller(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```