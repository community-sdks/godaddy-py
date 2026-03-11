# DomainsService

## Accessor

```python
service = client.domains()
```

## Method Index

- `list`: `ListResponse`
- `get_agreement`: `GetAgreementResponse`
- `available`: `AvailableResponse`
- `available_bulk`: `AvailableBulkResponse`
- `contacts_validate`: `ContactsValidateResponse`
- `purchase`: `PurchaseResponse`
- `schema`: `SchemaResponse`
- `validate`: `ValidateResponse`
- `suggest`: `SuggestResponse`
- `tlds`: `TldsResponse`
- `get`: `GetResponse`
- `update`: `UpdateResponse`
- `cancel`: `CancelResponse`
- `update_contacts`: `UpdateContactsResponse`
- `cancel_privacy`: `CancelPrivacyResponse`
- `purchase_privacy`: `PurchasePrivacyResponse`
- `record_replace`: `RecordReplaceResponse`
- `record_add`: `RecordAddResponse`
- `record_get`: `RecordGetResponse`
- `record_replace_type_name`: `RecordReplaceTypeNameResponse`
- `record_delete_type_name`: `RecordDeleteTypeNameResponse`
- `record_replace_type`: `RecordReplaceTypeResponse`
- `renew`: `RenewResponse`
- `transfer_in`: `TransferInResponse`
- `verify_email`: `VerifyEmailResponse`
- `get_v2_customers_customer_id_domains_domain`: `GetV2CustomersCustomerIdDomainsDomainResponse`
- `get_v2_customers_customer_id_domains_domain_change_of_registrant`: `GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse`
- `delete_v2_customers_customer_id_domains_domain_change_of_registrant`: `DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse`
- `patch_v2_customers_customer_id_domains_domain_dnssec_records`: `PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse`
- `delete_v2_customers_customer_id_domains_domain_dnssec_records`: `DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse`
- `put_v2_customers_customer_id_domains_domain_name_servers`: `PutV2CustomersCustomerIdDomainsDomainNameServersResponse`
- `get_v2_customers_customer_id_domains_domain_privacy_forwarding`: `GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse`
- `patch_v2_customers_customer_id_domains_domain_privacy_forwarding`: `PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse`
- `post_v2_customers_customer_id_domains_domain_redeem`: `PostV2CustomersCustomerIdDomainsDomainRedeemResponse`
- `post_v2_customers_customer_id_domains_domain_renew`: `PostV2CustomersCustomerIdDomainsDomainRenewResponse`
- `get_v2_customers_customer_id_domains_domain_transfer`: `GetV2CustomersCustomerIdDomainsDomainTransferResponse`
- `post_v2_customers_customer_id_domains_domain_transfer`: `PostV2CustomersCustomerIdDomainsDomainTransferResponse`
- `post_v2_customers_customer_id_domains_domain_transfer_validate`: `PostV2CustomersCustomerIdDomainsDomainTransferValidateResponse`
- `post_v2_customers_customer_id_domains_domain_transfer_in_accept`: `PostV2CustomersCustomerIdDomainsDomainTransferInAcceptResponse`
- `post_v2_customers_customer_id_domains_domain_transfer_in_cancel`: `PostV2CustomersCustomerIdDomainsDomainTransferInCancelResponse`
- `post_v2_customers_customer_id_domains_domain_transfer_in_restart`: `PostV2CustomersCustomerIdDomainsDomainTransferInRestartResponse`
- `post_v2_customers_customer_id_domains_domain_transfer_in_retry`: `PostV2CustomersCustomerIdDomainsDomainTransferInRetryResponse`
- `post_v2_customers_customer_id_domains_domain_transfer_out`: `PostV2CustomersCustomerIdDomainsDomainTransferOutResponse`
- `post_v2_customers_customer_id_domains_domain_transfer_out_accept`: `PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptResponse`
- `post_v2_customers_customer_id_domains_domain_transfer_out_reject`: `PostV2CustomersCustomerIdDomainsDomainTransferOutRejectResponse`
- `domains_forwards_get`: `DomainsForwardsGetResponse`
- `domains_forwards_post`: `DomainsForwardsPostResponse`
- `domains_forwards_put`: `DomainsForwardsPutResponse`
- `domains_forwards_delete`: `DomainsForwardsDeleteResponse`
- `get_v2_customers_customer_id_domains_domain_actions`: `GetV2CustomersCustomerIdDomainsDomainActionsResponse`
- `get_v2_customers_customer_id_domains_domain_actions_type`: `GetV2CustomersCustomerIdDomainsDomainActionsTypeResponse`
- `delete_v2_customers_customer_id_domains_domain_actions_type`: `DeleteV2CustomersCustomerIdDomainsDomainActionsTypeResponse`
- `get_v2_customers_customer_id_domains_notifications`: `GetV2CustomersCustomerIdDomainsNotificationsResponse`
- `get_v2_customers_customer_id_domains_notifications_opt_in`: `GetV2CustomersCustomerIdDomainsNotificationsOptInResponse`
- `put_v2_customers_customer_id_domains_notifications_opt_in`: `PutV2CustomersCustomerIdDomainsNotificationsOptInResponse`
- `get_v2_customers_customer_id_domains_notifications_schemas_type`: `GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeResponse`
- `post_v2_customers_customer_id_domains_notifications_notification_id_acknowledge`: `PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeResponse`
- `post_v2_customers_customer_id_domains_register`: `PostV2CustomersCustomerIdDomainsRegisterResponse`
- `get_v2_customers_customer_id_domains_register_schema_tld`: `GetV2CustomersCustomerIdDomainsRegisterSchemaTldResponse`
- `post_v2_customers_customer_id_domains_register_validate`: `PostV2CustomersCustomerIdDomainsRegisterValidateResponse`
- `get_v2_domains_maintenances`: `GetV2DomainsMaintenancesResponse`
- `get_v2_domains_maintenances_maintenance_id`: `GetV2DomainsMaintenancesMaintenanceIdResponse`
- `get_v2_domains_usage_yyyymm`: `GetV2DomainsUsageYyyymmResponse`
- `patch_v2_customers_customer_id_domains_domain_contacts`: `PatchV2CustomersCustomerIdDomainsDomainContactsResponse`
- `post_v2_customers_customer_id_domains_domain_regenerate_auth_code`: `PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeResponse`

### list

Returns: `ListResponse`

```python
from godaddy.dto.domains.requests import ListRequest
request = ListRequest(
    x_shopper_id='987654',
    statuses=["ACTIVE"],
    status_groups=["ACTIVE"],
    limit=1,
)
response = client.domains().list(request)
```

```json
[]
```

### get_agreement

Returns: `GetAgreementResponse`

```python
from godaddy.dto.domains.requests import GetAgreementRequest
request = GetAgreementRequest(
    x_market_id='abc123',
    tlds=["value"],
    privacy=True,
    for_transfer=True,
)
response = client.domains().get_agreement(request)
```

```json
[]
```

### available

Returns: `AvailableResponse`

```python
from godaddy.dto.domains.requests import AvailableRequest
request = AvailableRequest(
    domain='example.com',
    check_type='value',
    for_transfer=True,
)
response = client.domains().available(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### available_bulk

Returns: `AvailableBulkResponse`

```python
from godaddy.dto.domains.requests import AvailableBulkRequest
request = AvailableBulkRequest(
    domains=["example.com"],
    check_type='value',
)
response = client.domains().available_bulk(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### contacts_validate

Returns: `ContactsValidateResponse`

```python
from godaddy.dto.domains.requests import ContactsValidateRequest
request = ContactsValidateRequest(
    x_private_label_id=1,
    market_id='abc123',
    body={"key": "value"},
)
response = client.domains().contacts_validate(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### purchase

Returns: `PurchaseResponse`

```python
from godaddy.dto.domains.requests import PurchaseRequest
request = PurchaseRequest(
    x_shopper_id='987654',
    body={"key": "value"},
)
response = client.domains().purchase(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### schema

Returns: `SchemaResponse`

```python
from godaddy.dto.domains.requests import SchemaRequest
request = SchemaRequest(
    tld='value',
)
response = client.domains().schema(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### validate

Returns: `ValidateResponse`

```python
from godaddy.dto.domains.requests import ValidateRequest
request = ValidateRequest(
    body={"key": "value"},
)
response = client.domains().validate(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### suggest

Returns: `SuggestResponse`

```python
from godaddy.dto.domains.requests import SuggestRequest
request = SuggestRequest(
    x_shopper_id='987654',
    query='value',
    country='value',
    city='value',
)
response = client.domains().suggest(request)
```

```json
[]
```

### tlds

Returns: `TldsResponse`

```python
from godaddy.dto.domains.requests import TldsRequest
response = client.domains().tlds(TldsRequest())
```

```json
[]
```

### get

Returns: `GetResponse`

```python
from godaddy.dto.domains.requests import GetRequest
request = GetRequest(
    x_shopper_id='987654',
    domain='example.com',
)
response = client.domains().get(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### update

Returns: `UpdateResponse`

```python
from godaddy.dto.domains.requests import UpdateRequest
request = UpdateRequest(
    domain='example.com',
    x_shopper_id='987654',
    body={"key": "value"},
)
response = client.domains().update(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### cancel

Returns: `CancelResponse`

```python
from godaddy.dto.domains.requests import CancelRequest
request = CancelRequest(
    domain='example.com',
)
response = client.domains().cancel(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### update_contacts

Returns: `UpdateContactsResponse`

```python
from godaddy.dto.domains.requests import UpdateContactsRequest
request = UpdateContactsRequest(
    x_shopper_id='987654',
    domain='example.com',
    contacts='value',
)
response = client.domains().update_contacts(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### cancel_privacy

Returns: `CancelPrivacyResponse`

```python
from godaddy.dto.domains.requests import CancelPrivacyRequest
request = CancelPrivacyRequest(
    x_shopper_id='987654',
    domain='example.com',
)
response = client.domains().cancel_privacy(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### purchase_privacy

Returns: `PurchasePrivacyResponse`

```python
from godaddy.dto.domains.requests import PurchasePrivacyRequest
request = PurchasePrivacyRequest(
    x_shopper_id='987654',
    domain='example.com',
    body={"key": "value"},
)
response = client.domains().purchase_privacy(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### record_replace

Returns: `RecordReplaceResponse`

```python
from godaddy.dto.domains.requests import RecordReplaceRequest
request = RecordReplaceRequest(
    x_shopper_id='987654',
    domain='example.com',
    records=["value"],
)
response = client.domains().record_replace(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### record_add

Returns: `RecordAddResponse`

```python
from godaddy.dto.domains.requests import RecordAddRequest
request = RecordAddRequest(
    x_shopper_id='987654',
    domain='example.com',
    records='value',
)
response = client.domains().record_add(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### record_get

Returns: `RecordGetResponse`

```python
from godaddy.dto.domains.requests import RecordGetRequest
request = RecordGetRequest(
    x_shopper_id='987654',
    domain='example.com',
    type_value='value',
    name='value',
)
response = client.domains().record_get(request)
```

```json
[]
```

### record_replace_type_name

Returns: `RecordReplaceTypeNameResponse`

```python
from godaddy.dto.domains.requests import RecordReplaceTypeNameRequest
request = RecordReplaceTypeNameRequest(
    x_shopper_id='987654',
    domain='example.com',
    type_value='value',
    name='value',
)
response = client.domains().record_replace_type_name(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### record_delete_type_name

Returns: `RecordDeleteTypeNameResponse`

```python
from godaddy.dto.domains.requests import RecordDeleteTypeNameRequest
request = RecordDeleteTypeNameRequest(
    x_shopper_id='987654',
    domain='example.com',
    type_value='value',
    name='value',
)
response = client.domains().record_delete_type_name(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### record_replace_type

Returns: `RecordReplaceTypeResponse`

```python
from godaddy.dto.domains.requests import RecordReplaceTypeRequest
request = RecordReplaceTypeRequest(
    x_shopper_id='987654',
    domain='example.com',
    type_value='value',
    records=["value"],
)
response = client.domains().record_replace_type(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### renew

Returns: `RenewResponse`

```python
from godaddy.dto.domains.requests import RenewRequest
request = RenewRequest(
    x_shopper_id='987654',
    domain='example.com',
    body={"key": "value"},
)
response = client.domains().renew(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### transfer_in

Returns: `TransferInResponse`

```python
from godaddy.dto.domains.requests import TransferInRequest
request = TransferInRequest(
    x_shopper_id='987654',
    domain='example.com',
    body={"key": "value"},
)
response = client.domains().transfer_in(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### verify_email

Returns: `VerifyEmailResponse`

```python
from godaddy.dto.domains.requests import VerifyEmailRequest
request = VerifyEmailRequest(
    x_shopper_id='987654',
    domain='example.com',
)
response = client.domains().verify_email(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_v2_customers_customer_id_domains_domain

Returns: `GetV2CustomersCustomerIdDomainsDomainResponse`

```python
from godaddy.dto.domains.requests import GetV2CustomersCustomerIdDomainsDomainRequest
request = GetV2CustomersCustomerIdDomainsDomainRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    includes=["value"],
)
response = client.domains().get_v2_customers_customer_id_domains_domain(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_v2_customers_customer_id_domains_domain_change_of_registrant

Returns: `GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse`

```python
from godaddy.dto.domains.requests import GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantRequest
request = GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
)
response = client.domains().get_v2_customers_customer_id_domains_domain_change_of_registrant(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### delete_v2_customers_customer_id_domains_domain_change_of_registrant

Returns: `DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse`

```python
from godaddy.dto.domains.requests import DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantRequest
request = DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
)
response = client.domains().delete_v2_customers_customer_id_domains_domain_change_of_registrant(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### patch_v2_customers_customer_id_domains_domain_dnssec_records

Returns: `PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse`

```python
from godaddy.dto.domains.requests import PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsRequest
request = PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    body=["value"],
)
response = client.domains().patch_v2_customers_customer_id_domains_domain_dnssec_records(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### delete_v2_customers_customer_id_domains_domain_dnssec_records

Returns: `DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse`

```python
from godaddy.dto.domains.requests import DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsRequest
request = DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    body=["value"],
)
response = client.domains().delete_v2_customers_customer_id_domains_domain_dnssec_records(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### put_v2_customers_customer_id_domains_domain_name_servers

Returns: `PutV2CustomersCustomerIdDomainsDomainNameServersResponse`

```python
from godaddy.dto.domains.requests import PutV2CustomersCustomerIdDomainsDomainNameServersRequest
request = PutV2CustomersCustomerIdDomainsDomainNameServersRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    body={"key": "value"},
)
response = client.domains().put_v2_customers_customer_id_domains_domain_name_servers(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_v2_customers_customer_id_domains_domain_privacy_forwarding

Returns: `GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse`

```python
from godaddy.dto.domains.requests import GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingRequest
request = GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
)
response = client.domains().get_v2_customers_customer_id_domains_domain_privacy_forwarding(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### patch_v2_customers_customer_id_domains_domain_privacy_forwarding

Returns: `PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse`

```python
from godaddy.dto.domains.requests import PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingRequest
request = PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    body={"key": "value"},
)
response = client.domains().patch_v2_customers_customer_id_domains_domain_privacy_forwarding(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_domain_redeem

Returns: `PostV2CustomersCustomerIdDomainsDomainRedeemResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsDomainRedeemRequest
request = PostV2CustomersCustomerIdDomainsDomainRedeemRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    body={"key": "value"},
)
response = client.domains().post_v2_customers_customer_id_domains_domain_redeem(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_domain_renew

Returns: `PostV2CustomersCustomerIdDomainsDomainRenewResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsDomainRenewRequest
request = PostV2CustomersCustomerIdDomainsDomainRenewRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    body={"key": "value"},
)
response = client.domains().post_v2_customers_customer_id_domains_domain_renew(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_v2_customers_customer_id_domains_domain_transfer

Returns: `GetV2CustomersCustomerIdDomainsDomainTransferResponse`

```python
from godaddy.dto.domains.requests import GetV2CustomersCustomerIdDomainsDomainTransferRequest
request = GetV2CustomersCustomerIdDomainsDomainTransferRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
)
response = client.domains().get_v2_customers_customer_id_domains_domain_transfer(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_domain_transfer

Returns: `PostV2CustomersCustomerIdDomainsDomainTransferResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsDomainTransferRequest
request = PostV2CustomersCustomerIdDomainsDomainTransferRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    body={"key": "value"},
)
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_domain_transfer_validate

Returns: `PostV2CustomersCustomerIdDomainsDomainTransferValidateResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsDomainTransferValidateRequest
request = PostV2CustomersCustomerIdDomainsDomainTransferValidateRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    body={"key": "value"},
)
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_validate(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_domain_transfer_in_accept

Returns: `PostV2CustomersCustomerIdDomainsDomainTransferInAcceptResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsDomainTransferInAcceptRequest
request = PostV2CustomersCustomerIdDomainsDomainTransferInAcceptRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    body={"key": "value"},
)
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_in_accept(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_domain_transfer_in_cancel

Returns: `PostV2CustomersCustomerIdDomainsDomainTransferInCancelResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsDomainTransferInCancelRequest
request = PostV2CustomersCustomerIdDomainsDomainTransferInCancelRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
)
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_in_cancel(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_domain_transfer_in_restart

Returns: `PostV2CustomersCustomerIdDomainsDomainTransferInRestartResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsDomainTransferInRestartRequest
request = PostV2CustomersCustomerIdDomainsDomainTransferInRestartRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
)
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_in_restart(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_domain_transfer_in_retry

Returns: `PostV2CustomersCustomerIdDomainsDomainTransferInRetryResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsDomainTransferInRetryRequest
request = PostV2CustomersCustomerIdDomainsDomainTransferInRetryRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    body={"key": "value"},
)
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_in_retry(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_domain_transfer_out

Returns: `PostV2CustomersCustomerIdDomainsDomainTransferOutResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsDomainTransferOutRequest
request = PostV2CustomersCustomerIdDomainsDomainTransferOutRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    registrar='value',
)
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_out(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_domain_transfer_out_accept

Returns: `PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptRequest
request = PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
)
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_out_accept(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_domain_transfer_out_reject

Returns: `PostV2CustomersCustomerIdDomainsDomainTransferOutRejectResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsDomainTransferOutRejectRequest
request = PostV2CustomersCustomerIdDomainsDomainTransferOutRejectRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    reason='value',
)
response = client.domains().post_v2_customers_customer_id_domains_domain_transfer_out_reject(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### domains_forwards_get

Returns: `DomainsForwardsGetResponse`

```python
from godaddy.dto.domains.requests import DomainsForwardsGetRequest
request = DomainsForwardsGetRequest(
    customer_id='123456',
    fqdn='value',
    include_subs=True,
)
response = client.domains().domains_forwards_get(request)
```

```json
[]
```

### domains_forwards_post

Returns: `DomainsForwardsPostResponse`

```python
from godaddy.dto.domains.requests import DomainsForwardsPostRequest
request = DomainsForwardsPostRequest(
    customer_id='123456',
    fqdn='value',
    body={"key": "value"},
)
response = client.domains().domains_forwards_post(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### domains_forwards_put

Returns: `DomainsForwardsPutResponse`

```python
from godaddy.dto.domains.requests import DomainsForwardsPutRequest
request = DomainsForwardsPutRequest(
    customer_id='123456',
    fqdn='value',
    body={"key": "value"},
)
response = client.domains().domains_forwards_put(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### domains_forwards_delete

Returns: `DomainsForwardsDeleteResponse`

```python
from godaddy.dto.domains.requests import DomainsForwardsDeleteRequest
request = DomainsForwardsDeleteRequest(
    customer_id='123456',
    fqdn='value',
)
response = client.domains().domains_forwards_delete(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_v2_customers_customer_id_domains_domain_actions

Returns: `GetV2CustomersCustomerIdDomainsDomainActionsResponse`

```python
from godaddy.dto.domains.requests import GetV2CustomersCustomerIdDomainsDomainActionsRequest
request = GetV2CustomersCustomerIdDomainsDomainActionsRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
)
response = client.domains().get_v2_customers_customer_id_domains_domain_actions(request)
```

```json
[]
```

### get_v2_customers_customer_id_domains_domain_actions_type

Returns: `GetV2CustomersCustomerIdDomainsDomainActionsTypeResponse`

```python
from godaddy.dto.domains.requests import GetV2CustomersCustomerIdDomainsDomainActionsTypeRequest
request = GetV2CustomersCustomerIdDomainsDomainActionsTypeRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    type_value='value',
)
response = client.domains().get_v2_customers_customer_id_domains_domain_actions_type(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### delete_v2_customers_customer_id_domains_domain_actions_type

Returns: `DeleteV2CustomersCustomerIdDomainsDomainActionsTypeResponse`

```python
from godaddy.dto.domains.requests import DeleteV2CustomersCustomerIdDomainsDomainActionsTypeRequest
request = DeleteV2CustomersCustomerIdDomainsDomainActionsTypeRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    type_value='value',
)
response = client.domains().delete_v2_customers_customer_id_domains_domain_actions_type(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_v2_customers_customer_id_domains_notifications

Returns: `GetV2CustomersCustomerIdDomainsNotificationsResponse`

```python
from godaddy.dto.domains.requests import GetV2CustomersCustomerIdDomainsNotificationsRequest
request = GetV2CustomersCustomerIdDomainsNotificationsRequest(
    x_request_id='abc123',
    customer_id='123456',
)
response = client.domains().get_v2_customers_customer_id_domains_notifications(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_v2_customers_customer_id_domains_notifications_opt_in

Returns: `GetV2CustomersCustomerIdDomainsNotificationsOptInResponse`

```python
from godaddy.dto.domains.requests import GetV2CustomersCustomerIdDomainsNotificationsOptInRequest
request = GetV2CustomersCustomerIdDomainsNotificationsOptInRequest(
    x_request_id='abc123',
    customer_id='123456',
)
response = client.domains().get_v2_customers_customer_id_domains_notifications_opt_in(request)
```

```json
[]
```

### put_v2_customers_customer_id_domains_notifications_opt_in

Returns: `PutV2CustomersCustomerIdDomainsNotificationsOptInResponse`

```python
from godaddy.dto.domains.requests import PutV2CustomersCustomerIdDomainsNotificationsOptInRequest
request = PutV2CustomersCustomerIdDomainsNotificationsOptInRequest(
    x_request_id='abc123',
    customer_id='123456',
    types=["value"],
)
response = client.domains().put_v2_customers_customer_id_domains_notifications_opt_in(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_v2_customers_customer_id_domains_notifications_schemas_type

Returns: `GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeResponse`

```python
from godaddy.dto.domains.requests import GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeRequest
request = GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeRequest(
    x_request_id='abc123',
    customer_id='123456',
    type_value='value',
)
response = client.domains().get_v2_customers_customer_id_domains_notifications_schemas_type(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_notifications_notification_id_acknowledge

Returns: `PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeRequest
request = PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeRequest(
    x_request_id='abc123',
    customer_id='123456',
    notification_id='abc123',
)
response = client.domains().post_v2_customers_customer_id_domains_notifications_notification_id_acknowledge(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_register

Returns: `PostV2CustomersCustomerIdDomainsRegisterResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsRegisterRequest
request = PostV2CustomersCustomerIdDomainsRegisterRequest(
    x_request_id='abc123',
    customer_id='123456',
    body={"key": "value"},
)
response = client.domains().post_v2_customers_customer_id_domains_register(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_v2_customers_customer_id_domains_register_schema_tld

Returns: `GetV2CustomersCustomerIdDomainsRegisterSchemaTldResponse`

```python
from godaddy.dto.domains.requests import GetV2CustomersCustomerIdDomainsRegisterSchemaTldRequest
request = GetV2CustomersCustomerIdDomainsRegisterSchemaTldRequest(
    x_request_id='abc123',
    customer_id='123456',
    tld='value',
)
response = client.domains().get_v2_customers_customer_id_domains_register_schema_tld(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_register_validate

Returns: `PostV2CustomersCustomerIdDomainsRegisterValidateResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsRegisterValidateRequest
request = PostV2CustomersCustomerIdDomainsRegisterValidateRequest(
    x_request_id='abc123',
    customer_id='123456',
    body={"key": "value"},
)
response = client.domains().post_v2_customers_customer_id_domains_register_validate(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_v2_domains_maintenances

Returns: `GetV2DomainsMaintenancesResponse`

```python
from godaddy.dto.domains.requests import GetV2DomainsMaintenancesRequest
request = GetV2DomainsMaintenancesRequest(
    x_request_id='abc123',
    status='ACTIVE',
    modified_at_after='value',
    starts_at_after='value',
)
response = client.domains().get_v2_domains_maintenances(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_v2_domains_maintenances_maintenance_id

Returns: `GetV2DomainsMaintenancesMaintenanceIdResponse`

```python
from godaddy.dto.domains.requests import GetV2DomainsMaintenancesMaintenanceIdRequest
request = GetV2DomainsMaintenancesMaintenanceIdRequest(
    x_request_id='abc123',
    maintenance_id='abc123',
)
response = client.domains().get_v2_domains_maintenances_maintenance_id(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### get_v2_domains_usage_yyyymm

Returns: `GetV2DomainsUsageYyyymmResponse`

```python
from godaddy.dto.domains.requests import GetV2DomainsUsageYyyymmRequest
request = GetV2DomainsUsageYyyymmRequest(
    x_request_id='abc123',
    yyyymm='value',
    includes=["value"],
)
response = client.domains().get_v2_domains_usage_yyyymm(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### patch_v2_customers_customer_id_domains_domain_contacts

Returns: `PatchV2CustomersCustomerIdDomainsDomainContactsResponse`

```python
from godaddy.dto.domains.requests import PatchV2CustomersCustomerIdDomainsDomainContactsRequest
request = PatchV2CustomersCustomerIdDomainsDomainContactsRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
    body={"key": "value"},
)
response = client.domains().patch_v2_customers_customer_id_domains_domain_contacts(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```

### post_v2_customers_customer_id_domains_domain_regenerate_auth_code

Returns: `PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeResponse`

```python
from godaddy.dto.domains.requests import PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeRequest
request = PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeRequest(
    x_request_id='abc123',
    customer_id='123456',
    domain='example.com',
)
response = client.domains().post_v2_customers_customer_id_domains_domain_regenerate_auth_code(request)
```

```json
{
  "message": "Request completed successfully",
  "code": "SUCCESS"
}
```