from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class ListRequest:
    x_shopper_id: Optional[str] = None
    statuses: Optional[List[str]] = None
    status_groups: Optional[List[str]] = None
    limit: Optional[int] = None
    marker: Optional[str] = None
    includes: Optional[List[str]] = None
    modified_date: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("statuses", self.statuses),
            ("statusGroups", self.status_groups),
            ("limit", self.limit),
            ("marker", self.marker),
            ("includes", self.includes),
            ("modifiedDate", self.modified_date),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetAgreementRequest:
    x_market_id: Optional[str] = None
    tlds: Optional[List[str]] = None
    privacy: Optional[bool] = None
    for_transfer: Optional[bool] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("tlds", self.tlds),
            ("privacy", self.privacy),
            ("forTransfer", self.for_transfer),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Market-Id", self.x_market_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class AvailableRequest:
    domain: Optional[str] = None
    check_type: Optional[str] = None
    for_transfer: Optional[bool] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
            ("checkType", self.check_type),
            ("forTransfer", self.for_transfer),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class AvailableBulkRequest:
    domains: Optional[List[str]] = None
    check_type: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("checkType", self.check_type),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.domains

@dataclass(frozen=True)
class ContactsValidateRequest:
    x_private_label_id: Optional[int] = None
    market_id: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("marketId", self.market_id),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Private-Label-Id", self.x_private_label_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class PurchaseRequest:
    x_shopper_id: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class SchemaRequest:
    tld: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("tld", self.tld),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class ValidateRequest:
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class SuggestRequest:
    x_shopper_id: Optional[str] = None
    query: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    sources: Optional[List[str]] = None
    tlds: Optional[List[str]] = None
    length_max: Optional[int] = None
    length_min: Optional[int] = None
    limit: Optional[int] = None
    wait_ms: Optional[int] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("query", self.query),
            ("country", self.country),
            ("city", self.city),
            ("sources", self.sources),
            ("tlds", self.tlds),
            ("lengthMax", self.length_max),
            ("lengthMin", self.length_min),
            ("limit", self.limit),
            ("waitMs", self.wait_ms),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class TldsRequest:
    pass

@dataclass(frozen=True)
class GetRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class UpdateRequest:
    domain: Optional[str] = None
    x_shopper_id: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class CancelRequest:
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class UpdateContactsRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None
    contacts: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return self.contacts

@dataclass(frozen=True)
class CancelPrivacyRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PurchasePrivacyRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class RecordReplaceRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None
    records: Optional[List[Any]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return self.records

@dataclass(frozen=True)
class RecordAddRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None
    records: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return self.records

@dataclass(frozen=True)
class RecordGetRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None
    type_value: Optional[str] = None
    name: Optional[str] = None
    offset: Optional[int] = None
    limit: Optional[int] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
            ("type", self.type_value),
            ("name", self.name),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("offset", self.offset),
            ("limit", self.limit),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class RecordReplaceTypeNameRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None
    type_value: Optional[str] = None
    name: Optional[str] = None
    records: Optional[List[Any]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
            ("type", self.type_value),
            ("name", self.name),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return self.records

@dataclass(frozen=True)
class RecordDeleteTypeNameRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None
    type_value: Optional[str] = None
    name: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
            ("type", self.type_value),
            ("name", self.name),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class RecordReplaceTypeRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None
    type_value: Optional[str] = None
    records: Optional[List[Any]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
            ("type", self.type_value),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return self.records

@dataclass(frozen=True)
class RenewRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class TransferInRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class VerifyEmailRequest:
    x_shopper_id: Optional[str] = None
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsDomainRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    includes: Optional[List[str]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("includes", self.includes),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[List[Any]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[List[Any]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class PutV2CustomersCustomerIdDomainsDomainNameServersRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainRedeemRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainRenewRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsDomainTransferRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferValidateRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferInAcceptRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferInCancelRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferInRestartRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferInRetryRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferOutRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    registrar: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("registrar", self.registrar),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferOutRejectRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    reason: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("reason", self.reason),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class DomainsForwardsGetRequest:
    customer_id: Optional[str] = None
    fqdn: Optional[str] = None
    include_subs: Optional[bool] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("fqdn", self.fqdn),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("includeSubs", self.include_subs),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class DomainsForwardsPostRequest:
    customer_id: Optional[str] = None
    fqdn: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("fqdn", self.fqdn),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class DomainsForwardsPutRequest:
    customer_id: Optional[str] = None
    fqdn: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("fqdn", self.fqdn),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class DomainsForwardsDeleteRequest:
    customer_id: Optional[str] = None
    fqdn: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("fqdn", self.fqdn),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsDomainActionsRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsDomainActionsTypeRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    type_value: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
            ("type", self.type_value),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class DeleteV2CustomersCustomerIdDomainsDomainActionsTypeRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    type_value: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
            ("type", self.type_value),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsNotificationsRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsNotificationsOptInRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PutV2CustomersCustomerIdDomainsNotificationsOptInRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    types: Optional[List[str]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("types", self.types),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    type_value: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("type", self.type_value),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    notification_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("notificationId", self.notification_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsRegisterRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsRegisterSchemaTldRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    tld: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("tld", self.tld),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsRegisterValidateRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class GetV2DomainsMaintenancesRequest:
    x_request_id: Optional[str] = None
    status: Optional[str] = None
    modified_at_after: Optional[str] = None
    starts_at_after: Optional[str] = None
    limit: Optional[int] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("status", self.status),
            ("modifiedAtAfter", self.modified_at_after),
            ("startsAtAfter", self.starts_at_after),
            ("limit", self.limit),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetV2DomainsMaintenancesMaintenanceIdRequest:
    x_request_id: Optional[str] = None
    maintenance_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("maintenanceId", self.maintenance_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetV2DomainsUsageYyyymmRequest:
    x_request_id: Optional[str] = None
    yyyymm: Optional[str] = None
    includes: Optional[List[str]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("yyyymm", self.yyyymm),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("includes", self.includes),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class PatchV2CustomersCustomerIdDomainsDomainContactsRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeRequest:
    x_request_id: Optional[str] = None
    customer_id: Optional[str] = None
    domain: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
            ("domain", self.domain),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None
