from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass(frozen=True)
class ListResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "ListResponse":
        if isinstance(data, dict):
            return ListResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return ListResponse(raw=data, items=data, array_items=data)
        return ListResponse(raw=data)

@dataclass(frozen=True)
class GetAgreementResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetAgreementResponse":
        if isinstance(data, dict):
            return GetAgreementResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return GetAgreementResponse(raw=data, items=data, array_items=data)
        return GetAgreementResponse(raw=data)

@dataclass(frozen=True)
class AvailableResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    available: Optional[bool] = None
    currency: Optional[str] = None
    definitive: Optional[bool] = None
    domain: Optional[str] = None
    period: Optional[int] = None
    price: Optional[int] = None

    @staticmethod
    def from_mixed(data: Any) -> "AvailableResponse":
        if isinstance(data, dict):
            return AvailableResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                available=(data.get("available") if isinstance(data.get("available"), bool) else None),
                currency=(data.get("currency") if isinstance(data.get("currency"), str) else None),
                definitive=(data.get("definitive") if isinstance(data.get("definitive"), bool) else None),
                domain=(data.get("domain") if isinstance(data.get("domain"), str) else None),
                period=(data.get("period") if isinstance(data.get("period"), int) and not isinstance(data.get("period"), bool) else None),
                price=(data.get("price") if isinstance(data.get("price"), int) and not isinstance(data.get("price"), bool) else None),
            )
        if isinstance(data, list):
            return AvailableResponse(raw=data, items=data)
        return AvailableResponse(raw=data)

@dataclass(frozen=True)
class AvailableBulkResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    domains: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "AvailableBulkResponse":
        if isinstance(data, dict):
            return AvailableBulkResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                domains=(data.get("domains") if isinstance(data.get("domains"), list) else None),
            )
        if isinstance(data, list):
            return AvailableBulkResponse(raw=data, items=data)
        return AvailableBulkResponse(raw=data)

@dataclass(frozen=True)
class ContactsValidateResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "ContactsValidateResponse":
        if isinstance(data, dict):
            return ContactsValidateResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return ContactsValidateResponse(raw=data, items=data)
        return ContactsValidateResponse(raw=data)

@dataclass(frozen=True)
class PurchaseResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    currency: Optional[str] = None
    item_count: Optional[int] = None
    order_id: Optional[int] = None
    total: Optional[int] = None

    @staticmethod
    def from_mixed(data: Any) -> "PurchaseResponse":
        if isinstance(data, dict):
            return PurchaseResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                currency=(data.get("currency") if isinstance(data.get("currency"), str) else None),
                item_count=(data.get("itemCount") if isinstance(data.get("itemCount"), int) and not isinstance(data.get("itemCount"), bool) else None),
                order_id=(data.get("orderId") if isinstance(data.get("orderId"), int) and not isinstance(data.get("orderId"), bool) else None),
                total=(data.get("total") if isinstance(data.get("total"), int) and not isinstance(data.get("total"), bool) else None),
            )
        if isinstance(data, list):
            return PurchaseResponse(raw=data, items=data)
        return PurchaseResponse(raw=data)

@dataclass(frozen=True)
class SchemaResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    id: Optional[str] = None
    models: Optional[Dict[str, Any]] = None
    properties: Optional[Dict[str, Any]] = None
    required: Optional[List[str]] = None

    @staticmethod
    def from_mixed(data: Any) -> "SchemaResponse":
        if isinstance(data, dict):
            return SchemaResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                id=(data.get("id") if isinstance(data.get("id"), str) else None),
                models=(data.get("models") if isinstance(data.get("models"), dict) else None),
                properties=(data.get("properties") if isinstance(data.get("properties"), dict) else None),
                required=(data.get("required") if isinstance(data.get("required"), list) else None),
            )
        if isinstance(data, list):
            return SchemaResponse(raw=data, items=data)
        return SchemaResponse(raw=data)

@dataclass(frozen=True)
class ValidateResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "ValidateResponse":
        if isinstance(data, dict):
            return ValidateResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return ValidateResponse(raw=data, items=data)
        return ValidateResponse(raw=data)

@dataclass(frozen=True)
class SuggestResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "SuggestResponse":
        if isinstance(data, dict):
            return SuggestResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return SuggestResponse(raw=data, items=data, array_items=data)
        return SuggestResponse(raw=data)

@dataclass(frozen=True)
class TldsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "TldsResponse":
        if isinstance(data, dict):
            return TldsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return TldsResponse(raw=data, items=data, array_items=data)
        return TldsResponse(raw=data)

@dataclass(frozen=True)
class GetResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    auth_code: Optional[str] = None
    contact_admin: Optional[Dict[str, Any]] = None
    contact_billing: Optional[Dict[str, Any]] = None
    contact_registrant: Optional[Dict[str, Any]] = None
    contact_tech: Optional[Dict[str, Any]] = None
    created_at: Optional[str] = None
    deleted_at: Optional[str] = None
    transfer_away_eligible_at: Optional[str] = None
    domain: Optional[str] = None
    domain_id: Optional[float] = None
    expiration_protected: Optional[bool] = None
    expires: Optional[str] = None
    expose_registrant_organization: Optional[bool] = None
    expose_whois: Optional[bool] = None
    hold_registrar: Optional[bool] = None
    locked: Optional[bool] = None
    name_servers: Optional[List[str]] = None
    privacy: Optional[bool] = None
    registrar_created_at: Optional[str] = None
    renew_auto: Optional[bool] = None
    renew_deadline: Optional[str] = None
    status: Optional[str] = None
    subaccount_id: Optional[str] = None
    transfer_protected: Optional[bool] = None
    verifications: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetResponse":
        if isinstance(data, dict):
            return GetResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                auth_code=(data.get("authCode") if isinstance(data.get("authCode"), str) else None),
                contact_admin=(data.get("contactAdmin") if isinstance(data.get("contactAdmin"), dict) else None),
                contact_billing=(data.get("contactBilling") if isinstance(data.get("contactBilling"), dict) else None),
                contact_registrant=(data.get("contactRegistrant") if isinstance(data.get("contactRegistrant"), dict) else None),
                contact_tech=(data.get("contactTech") if isinstance(data.get("contactTech"), dict) else None),
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                deleted_at=(data.get("deletedAt") if isinstance(data.get("deletedAt"), str) else None),
                transfer_away_eligible_at=(data.get("transferAwayEligibleAt") if isinstance(data.get("transferAwayEligibleAt"), str) else None),
                domain=(data.get("domain") if isinstance(data.get("domain"), str) else None),
                domain_id=(data.get("domainId") if isinstance(data.get("domainId"), (int, float)) and not isinstance(data.get("domainId"), bool) else None),
                expiration_protected=(data.get("expirationProtected") if isinstance(data.get("expirationProtected"), bool) else None),
                expires=(data.get("expires") if isinstance(data.get("expires"), str) else None),
                expose_registrant_organization=(data.get("exposeRegistrantOrganization") if isinstance(data.get("exposeRegistrantOrganization"), bool) else None),
                expose_whois=(data.get("exposeWhois") if isinstance(data.get("exposeWhois"), bool) else None),
                hold_registrar=(data.get("holdRegistrar") if isinstance(data.get("holdRegistrar"), bool) else None),
                locked=(data.get("locked") if isinstance(data.get("locked"), bool) else None),
                name_servers=(data.get("nameServers") if isinstance(data.get("nameServers"), list) else None),
                privacy=(data.get("privacy") if isinstance(data.get("privacy"), bool) else None),
                registrar_created_at=(data.get("registrarCreatedAt") if isinstance(data.get("registrarCreatedAt"), str) else None),
                renew_auto=(data.get("renewAuto") if isinstance(data.get("renewAuto"), bool) else None),
                renew_deadline=(data.get("renewDeadline") if isinstance(data.get("renewDeadline"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                subaccount_id=(data.get("subaccountId") if isinstance(data.get("subaccountId"), str) else None),
                transfer_protected=(data.get("transferProtected") if isinstance(data.get("transferProtected"), bool) else None),
                verifications=(data.get("verifications") if isinstance(data.get("verifications"), dict) else None),
            )
        if isinstance(data, list):
            return GetResponse(raw=data, items=data)
        return GetResponse(raw=data)

@dataclass(frozen=True)
class UpdateResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "UpdateResponse":
        if isinstance(data, dict):
            return UpdateResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return UpdateResponse(raw=data, items=data)
        return UpdateResponse(raw=data)

@dataclass(frozen=True)
class CancelResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CancelResponse":
        if isinstance(data, dict):
            return CancelResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CancelResponse(raw=data, items=data)
        return CancelResponse(raw=data)

@dataclass(frozen=True)
class UpdateContactsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "UpdateContactsResponse":
        if isinstance(data, dict):
            return UpdateContactsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return UpdateContactsResponse(raw=data, items=data)
        return UpdateContactsResponse(raw=data)

@dataclass(frozen=True)
class CancelPrivacyResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CancelPrivacyResponse":
        if isinstance(data, dict):
            return CancelPrivacyResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CancelPrivacyResponse(raw=data, items=data)
        return CancelPrivacyResponse(raw=data)

@dataclass(frozen=True)
class PurchasePrivacyResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    currency: Optional[str] = None
    item_count: Optional[int] = None
    order_id: Optional[int] = None
    total: Optional[int] = None

    @staticmethod
    def from_mixed(data: Any) -> "PurchasePrivacyResponse":
        if isinstance(data, dict):
            return PurchasePrivacyResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                currency=(data.get("currency") if isinstance(data.get("currency"), str) else None),
                item_count=(data.get("itemCount") if isinstance(data.get("itemCount"), int) and not isinstance(data.get("itemCount"), bool) else None),
                order_id=(data.get("orderId") if isinstance(data.get("orderId"), int) and not isinstance(data.get("orderId"), bool) else None),
                total=(data.get("total") if isinstance(data.get("total"), int) and not isinstance(data.get("total"), bool) else None),
            )
        if isinstance(data, list):
            return PurchasePrivacyResponse(raw=data, items=data)
        return PurchasePrivacyResponse(raw=data)

@dataclass(frozen=True)
class RecordReplaceResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "RecordReplaceResponse":
        if isinstance(data, dict):
            return RecordReplaceResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return RecordReplaceResponse(raw=data, items=data)
        return RecordReplaceResponse(raw=data)

@dataclass(frozen=True)
class RecordAddResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "RecordAddResponse":
        if isinstance(data, dict):
            return RecordAddResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return RecordAddResponse(raw=data, items=data)
        return RecordAddResponse(raw=data)

@dataclass(frozen=True)
class RecordGetResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "RecordGetResponse":
        if isinstance(data, dict):
            return RecordGetResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return RecordGetResponse(raw=data, items=data, array_items=data)
        return RecordGetResponse(raw=data)

@dataclass(frozen=True)
class RecordReplaceTypeNameResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "RecordReplaceTypeNameResponse":
        if isinstance(data, dict):
            return RecordReplaceTypeNameResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return RecordReplaceTypeNameResponse(raw=data, items=data)
        return RecordReplaceTypeNameResponse(raw=data)

@dataclass(frozen=True)
class RecordDeleteTypeNameResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "RecordDeleteTypeNameResponse":
        if isinstance(data, dict):
            return RecordDeleteTypeNameResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return RecordDeleteTypeNameResponse(raw=data, items=data)
        return RecordDeleteTypeNameResponse(raw=data)

@dataclass(frozen=True)
class RecordReplaceTypeResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "RecordReplaceTypeResponse":
        if isinstance(data, dict):
            return RecordReplaceTypeResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return RecordReplaceTypeResponse(raw=data, items=data)
        return RecordReplaceTypeResponse(raw=data)

@dataclass(frozen=True)
class RenewResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    currency: Optional[str] = None
    item_count: Optional[int] = None
    order_id: Optional[int] = None
    total: Optional[int] = None

    @staticmethod
    def from_mixed(data: Any) -> "RenewResponse":
        if isinstance(data, dict):
            return RenewResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                currency=(data.get("currency") if isinstance(data.get("currency"), str) else None),
                item_count=(data.get("itemCount") if isinstance(data.get("itemCount"), int) and not isinstance(data.get("itemCount"), bool) else None),
                order_id=(data.get("orderId") if isinstance(data.get("orderId"), int) and not isinstance(data.get("orderId"), bool) else None),
                total=(data.get("total") if isinstance(data.get("total"), int) and not isinstance(data.get("total"), bool) else None),
            )
        if isinstance(data, list):
            return RenewResponse(raw=data, items=data)
        return RenewResponse(raw=data)

@dataclass(frozen=True)
class TransferInResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    currency: Optional[str] = None
    item_count: Optional[int] = None
    order_id: Optional[int] = None
    total: Optional[int] = None

    @staticmethod
    def from_mixed(data: Any) -> "TransferInResponse":
        if isinstance(data, dict):
            return TransferInResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                currency=(data.get("currency") if isinstance(data.get("currency"), str) else None),
                item_count=(data.get("itemCount") if isinstance(data.get("itemCount"), int) and not isinstance(data.get("itemCount"), bool) else None),
                order_id=(data.get("orderId") if isinstance(data.get("orderId"), int) and not isinstance(data.get("orderId"), bool) else None),
                total=(data.get("total") if isinstance(data.get("total"), int) and not isinstance(data.get("total"), bool) else None),
            )
        if isinstance(data, list):
            return TransferInResponse(raw=data, items=data)
        return TransferInResponse(raw=data)

@dataclass(frozen=True)
class VerifyEmailResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "VerifyEmailResponse":
        if isinstance(data, dict):
            return VerifyEmailResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return VerifyEmailResponse(raw=data, items=data)
        return VerifyEmailResponse(raw=data)

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsDomainResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    domain_id: Optional[str] = None
    domain: Optional[str] = None
    subaccount_id: Optional[str] = None
    status: Optional[str] = None
    expires_at: Optional[str] = None
    expiration_protected: Optional[bool] = None
    hold_registrar: Optional[bool] = None
    locked: Optional[bool] = None
    privacy: Optional[bool] = None
    registrar_created_at: Optional[str] = None
    renew_auto: Optional[bool] = None
    renew_deadline: Optional[str] = None
    transfer_protected: Optional[bool] = None
    created_at: Optional[str] = None
    deleted_at: Optional[str] = None
    modified_at: Optional[str] = None
    transfer_away_eligible_at: Optional[str] = None
    auth_code: Optional[str] = None
    name_servers: Optional[List[str]] = None
    hostnames: Optional[List[str]] = None
    renewal: Optional[Dict[str, Any]] = None
    verifications: Optional[Dict[str, Any]] = None
    contacts: Optional[Dict[str, Any]] = None
    actions: Optional[List[Dict[str, Any]]] = None
    dnssec_records: Optional[List[Dict[str, Any]]] = None
    registry_status_codes: Optional[List[str]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2CustomersCustomerIdDomainsDomainResponse":
        if isinstance(data, dict):
            return GetV2CustomersCustomerIdDomainsDomainResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                domain_id=(data.get("domainId") if isinstance(data.get("domainId"), str) else None),
                domain=(data.get("domain") if isinstance(data.get("domain"), str) else None),
                subaccount_id=(data.get("subaccountId") if isinstance(data.get("subaccountId"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                expires_at=(data.get("expiresAt") if isinstance(data.get("expiresAt"), str) else None),
                expiration_protected=(data.get("expirationProtected") if isinstance(data.get("expirationProtected"), bool) else None),
                hold_registrar=(data.get("holdRegistrar") if isinstance(data.get("holdRegistrar"), bool) else None),
                locked=(data.get("locked") if isinstance(data.get("locked"), bool) else None),
                privacy=(data.get("privacy") if isinstance(data.get("privacy"), bool) else None),
                registrar_created_at=(data.get("registrarCreatedAt") if isinstance(data.get("registrarCreatedAt"), str) else None),
                renew_auto=(data.get("renewAuto") if isinstance(data.get("renewAuto"), bool) else None),
                renew_deadline=(data.get("renewDeadline") if isinstance(data.get("renewDeadline"), str) else None),
                transfer_protected=(data.get("transferProtected") if isinstance(data.get("transferProtected"), bool) else None),
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                deleted_at=(data.get("deletedAt") if isinstance(data.get("deletedAt"), str) else None),
                modified_at=(data.get("modifiedAt") if isinstance(data.get("modifiedAt"), str) else None),
                transfer_away_eligible_at=(data.get("transferAwayEligibleAt") if isinstance(data.get("transferAwayEligibleAt"), str) else None),
                auth_code=(data.get("authCode") if isinstance(data.get("authCode"), str) else None),
                name_servers=(data.get("nameServers") if isinstance(data.get("nameServers"), list) else None),
                hostnames=(data.get("hostnames") if isinstance(data.get("hostnames"), list) else None),
                renewal=(data.get("renewal") if isinstance(data.get("renewal"), dict) else None),
                verifications=(data.get("verifications") if isinstance(data.get("verifications"), dict) else None),
                contacts=(data.get("contacts") if isinstance(data.get("contacts"), dict) else None),
                actions=(data.get("actions") if isinstance(data.get("actions"), list) else None),
                dnssec_records=(data.get("dnssecRecords") if isinstance(data.get("dnssecRecords"), list) else None),
                registry_status_codes=(data.get("registryStatusCodes") if isinstance(data.get("registryStatusCodes"), list) else None),
            )
        if isinstance(data, list):
            return GetV2CustomersCustomerIdDomainsDomainResponse(raw=data, items=data)
        return GetV2CustomersCustomerIdDomainsDomainResponse(raw=data)

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    create_date: Optional[str] = None
    gaining_contact: Optional[Dict[str, Any]] = None
    losing_contact: Optional[Dict[str, Any]] = None
    other_domains_affected: Optional[int] = None
    shopper_email: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse":
        if isinstance(data, dict):
            return GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                create_date=(data.get("createDate") if isinstance(data.get("createDate"), str) else None),
                gaining_contact=(data.get("gainingContact") if isinstance(data.get("gainingContact"), dict) else None),
                losing_contact=(data.get("losingContact") if isinstance(data.get("losingContact"), dict) else None),
                other_domains_affected=(data.get("otherDomainsAffected") if isinstance(data.get("otherDomainsAffected"), int) and not isinstance(data.get("otherDomainsAffected"), bool) else None),
                shopper_email=(data.get("shopperEmail") if isinstance(data.get("shopperEmail"), str) else None),
            )
        if isinstance(data, list):
            return GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse(raw=data, items=data)
        return GetV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse(raw=data)

@dataclass(frozen=True)
class DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse":
        if isinstance(data, dict):
            return DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse(raw=data, items=data)
        return DeleteV2CustomersCustomerIdDomainsDomainChangeOfRegistrantResponse(raw=data)

@dataclass(frozen=True)
class PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse":
        if isinstance(data, dict):
            return PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse(raw=data, items=data)
        return PatchV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse(raw=data)

@dataclass(frozen=True)
class DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse":
        if isinstance(data, dict):
            return DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse(raw=data, items=data)
        return DeleteV2CustomersCustomerIdDomainsDomainDnssecRecordsResponse(raw=data)

@dataclass(frozen=True)
class PutV2CustomersCustomerIdDomainsDomainNameServersResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PutV2CustomersCustomerIdDomainsDomainNameServersResponse":
        if isinstance(data, dict):
            return PutV2CustomersCustomerIdDomainsDomainNameServersResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PutV2CustomersCustomerIdDomainsDomainNameServersResponse(raw=data, items=data)
        return PutV2CustomersCustomerIdDomainsDomainNameServersResponse(raw=data)

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    private_email: Optional[str] = None
    forwarding_email: Optional[str] = None
    email_preference: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse":
        if isinstance(data, dict):
            return GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                private_email=(data.get("privateEmail") if isinstance(data.get("privateEmail"), str) else None),
                forwarding_email=(data.get("forwardingEmail") if isinstance(data.get("forwardingEmail"), str) else None),
                email_preference=(data.get("emailPreference") if isinstance(data.get("emailPreference"), str) else None),
            )
        if isinstance(data, list):
            return GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse(raw=data, items=data)
        return GetV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse(raw=data)

@dataclass(frozen=True)
class PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse":
        if isinstance(data, dict):
            return PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse(raw=data, items=data)
        return PatchV2CustomersCustomerIdDomainsDomainPrivacyForwardingResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainRedeemResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsDomainRedeemResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsDomainRedeemResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsDomainRedeemResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsDomainRedeemResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainRenewResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsDomainRenewResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsDomainRenewResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsDomainRenewResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsDomainRenewResponse(raw=data)

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsDomainTransferResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    transfer_status_codes: Optional[List[str]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2CustomersCustomerIdDomainsDomainTransferResponse":
        if isinstance(data, dict):
            return GetV2CustomersCustomerIdDomainsDomainTransferResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                transfer_status_codes=(data.get("transferStatusCodes") if isinstance(data.get("transferStatusCodes"), list) else None),
            )
        if isinstance(data, list):
            return GetV2CustomersCustomerIdDomainsDomainTransferResponse(raw=data, items=data)
        return GetV2CustomersCustomerIdDomainsDomainTransferResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsDomainTransferResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsDomainTransferResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsDomainTransferResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsDomainTransferResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferValidateResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsDomainTransferValidateResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsDomainTransferValidateResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsDomainTransferValidateResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsDomainTransferValidateResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferInAcceptResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsDomainTransferInAcceptResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsDomainTransferInAcceptResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsDomainTransferInAcceptResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsDomainTransferInAcceptResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferInCancelResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsDomainTransferInCancelResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsDomainTransferInCancelResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsDomainTransferInCancelResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsDomainTransferInCancelResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferInRestartResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsDomainTransferInRestartResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsDomainTransferInRestartResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsDomainTransferInRestartResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsDomainTransferInRestartResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferInRetryResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsDomainTransferInRetryResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsDomainTransferInRetryResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsDomainTransferInRetryResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsDomainTransferInRetryResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferOutResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsDomainTransferOutResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsDomainTransferOutResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsDomainTransferOutResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsDomainTransferOutResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsDomainTransferOutAcceptResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainTransferOutRejectResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsDomainTransferOutRejectResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsDomainTransferOutRejectResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsDomainTransferOutRejectResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsDomainTransferOutRejectResponse(raw=data)

@dataclass(frozen=True)
class DomainsForwardsGetResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "DomainsForwardsGetResponse":
        if isinstance(data, dict):
            return DomainsForwardsGetResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return DomainsForwardsGetResponse(raw=data, items=data, array_items=data)
        return DomainsForwardsGetResponse(raw=data)

@dataclass(frozen=True)
class DomainsForwardsPostResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "DomainsForwardsPostResponse":
        if isinstance(data, dict):
            return DomainsForwardsPostResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return DomainsForwardsPostResponse(raw=data, items=data)
        return DomainsForwardsPostResponse(raw=data)

@dataclass(frozen=True)
class DomainsForwardsPutResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "DomainsForwardsPutResponse":
        if isinstance(data, dict):
            return DomainsForwardsPutResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return DomainsForwardsPutResponse(raw=data, items=data)
        return DomainsForwardsPutResponse(raw=data)

@dataclass(frozen=True)
class DomainsForwardsDeleteResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "DomainsForwardsDeleteResponse":
        if isinstance(data, dict):
            return DomainsForwardsDeleteResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return DomainsForwardsDeleteResponse(raw=data, items=data)
        return DomainsForwardsDeleteResponse(raw=data)

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsDomainActionsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2CustomersCustomerIdDomainsDomainActionsResponse":
        if isinstance(data, dict):
            return GetV2CustomersCustomerIdDomainsDomainActionsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return GetV2CustomersCustomerIdDomainsDomainActionsResponse(raw=data, items=data, array_items=data)
        return GetV2CustomersCustomerIdDomainsDomainActionsResponse(raw=data)

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsDomainActionsTypeResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    type_value: Optional[str] = None
    origination: Optional[str] = None
    created_at: Optional[str] = None
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    modified_at: Optional[str] = None
    status: Optional[str] = None
    reason: Optional[Dict[str, Any]] = None
    request_id: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2CustomersCustomerIdDomainsDomainActionsTypeResponse":
        if isinstance(data, dict):
            return GetV2CustomersCustomerIdDomainsDomainActionsTypeResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                type_value=(data.get("type") if isinstance(data.get("type"), str) else None),
                origination=(data.get("origination") if isinstance(data.get("origination"), str) else None),
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                started_at=(data.get("startedAt") if isinstance(data.get("startedAt"), str) else None),
                completed_at=(data.get("completedAt") if isinstance(data.get("completedAt"), str) else None),
                modified_at=(data.get("modifiedAt") if isinstance(data.get("modifiedAt"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                reason=(data.get("reason") if isinstance(data.get("reason"), dict) else None),
                request_id=(data.get("requestId") if isinstance(data.get("requestId"), str) else None),
            )
        if isinstance(data, list):
            return GetV2CustomersCustomerIdDomainsDomainActionsTypeResponse(raw=data, items=data)
        return GetV2CustomersCustomerIdDomainsDomainActionsTypeResponse(raw=data)

@dataclass(frozen=True)
class DeleteV2CustomersCustomerIdDomainsDomainActionsTypeResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "DeleteV2CustomersCustomerIdDomainsDomainActionsTypeResponse":
        if isinstance(data, dict):
            return DeleteV2CustomersCustomerIdDomainsDomainActionsTypeResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return DeleteV2CustomersCustomerIdDomainsDomainActionsTypeResponse(raw=data, items=data)
        return DeleteV2CustomersCustomerIdDomainsDomainActionsTypeResponse(raw=data)

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsNotificationsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    notification_id: Optional[str] = None
    type_value: Optional[str] = None
    resource: Optional[str] = None
    resource_type: Optional[str] = None
    status: Optional[str] = None
    added_at: Optional[str] = None
    request_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2CustomersCustomerIdDomainsNotificationsResponse":
        if isinstance(data, dict):
            return GetV2CustomersCustomerIdDomainsNotificationsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                notification_id=(data.get("notificationId") if isinstance(data.get("notificationId"), str) else None),
                type_value=(data.get("type") if isinstance(data.get("type"), str) else None),
                resource=(data.get("resource") if isinstance(data.get("resource"), str) else None),
                resource_type=(data.get("resourceType") if isinstance(data.get("resourceType"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                added_at=(data.get("addedAt") if isinstance(data.get("addedAt"), str) else None),
                request_id=(data.get("requestId") if isinstance(data.get("requestId"), str) else None),
                metadata=(data.get("metadata") if isinstance(data.get("metadata"), dict) else None),
            )
        if isinstance(data, list):
            return GetV2CustomersCustomerIdDomainsNotificationsResponse(raw=data, items=data)
        return GetV2CustomersCustomerIdDomainsNotificationsResponse(raw=data)

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsNotificationsOptInResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2CustomersCustomerIdDomainsNotificationsOptInResponse":
        if isinstance(data, dict):
            return GetV2CustomersCustomerIdDomainsNotificationsOptInResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return GetV2CustomersCustomerIdDomainsNotificationsOptInResponse(raw=data, items=data, array_items=data)
        return GetV2CustomersCustomerIdDomainsNotificationsOptInResponse(raw=data)

@dataclass(frozen=True)
class PutV2CustomersCustomerIdDomainsNotificationsOptInResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PutV2CustomersCustomerIdDomainsNotificationsOptInResponse":
        if isinstance(data, dict):
            return PutV2CustomersCustomerIdDomainsNotificationsOptInResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PutV2CustomersCustomerIdDomainsNotificationsOptInResponse(raw=data, items=data)
        return PutV2CustomersCustomerIdDomainsNotificationsOptInResponse(raw=data)

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    id: Optional[str] = None
    models: Optional[Dict[str, Any]] = None
    properties: Optional[Dict[str, Any]] = None
    required: Optional[List[str]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeResponse":
        if isinstance(data, dict):
            return GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                id=(data.get("id") if isinstance(data.get("id"), str) else None),
                models=(data.get("models") if isinstance(data.get("models"), dict) else None),
                properties=(data.get("properties") if isinstance(data.get("properties"), dict) else None),
                required=(data.get("required") if isinstance(data.get("required"), list) else None),
            )
        if isinstance(data, list):
            return GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeResponse(raw=data, items=data)
        return GetV2CustomersCustomerIdDomainsNotificationsSchemasTypeResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsNotificationsNotificationIdAcknowledgeResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsRegisterResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsRegisterResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsRegisterResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsRegisterResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsRegisterResponse(raw=data)

@dataclass(frozen=True)
class GetV2CustomersCustomerIdDomainsRegisterSchemaTldResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    id: Optional[str] = None
    models: Optional[Dict[str, Any]] = None
    properties: Optional[Dict[str, Any]] = None
    required: Optional[List[str]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2CustomersCustomerIdDomainsRegisterSchemaTldResponse":
        if isinstance(data, dict):
            return GetV2CustomersCustomerIdDomainsRegisterSchemaTldResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                id=(data.get("id") if isinstance(data.get("id"), str) else None),
                models=(data.get("models") if isinstance(data.get("models"), dict) else None),
                properties=(data.get("properties") if isinstance(data.get("properties"), dict) else None),
                required=(data.get("required") if isinstance(data.get("required"), list) else None),
            )
        if isinstance(data, list):
            return GetV2CustomersCustomerIdDomainsRegisterSchemaTldResponse(raw=data, items=data)
        return GetV2CustomersCustomerIdDomainsRegisterSchemaTldResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsRegisterValidateResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsRegisterValidateResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsRegisterValidateResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsRegisterValidateResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsRegisterValidateResponse(raw=data)

@dataclass(frozen=True)
class GetV2DomainsMaintenancesResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    ends_at: Optional[str] = None
    environment: Optional[str] = None
    maintenance_id: Optional[str] = None
    modified_at: Optional[str] = None
    reason: Optional[str] = None
    starts_at: Optional[str] = None
    status: Optional[str] = None
    summary: Optional[str] = None
    tlds: Optional[List[str]] = None
    type_value: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2DomainsMaintenancesResponse":
        if isinstance(data, dict):
            return GetV2DomainsMaintenancesResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                ends_at=(data.get("endsAt") if isinstance(data.get("endsAt"), str) else None),
                environment=(data.get("environment") if isinstance(data.get("environment"), str) else None),
                maintenance_id=(data.get("maintenanceId") if isinstance(data.get("maintenanceId"), str) else None),
                modified_at=(data.get("modifiedAt") if isinstance(data.get("modifiedAt"), str) else None),
                reason=(data.get("reason") if isinstance(data.get("reason"), str) else None),
                starts_at=(data.get("startsAt") if isinstance(data.get("startsAt"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                summary=(data.get("summary") if isinstance(data.get("summary"), str) else None),
                tlds=(data.get("tlds") if isinstance(data.get("tlds"), list) else None),
                type_value=(data.get("type") if isinstance(data.get("type"), str) else None),
            )
        if isinstance(data, list):
            return GetV2DomainsMaintenancesResponse(raw=data, items=data)
        return GetV2DomainsMaintenancesResponse(raw=data)

@dataclass(frozen=True)
class GetV2DomainsMaintenancesMaintenanceIdResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    ends_at: Optional[str] = None
    environment: Optional[str] = None
    maintenance_id: Optional[str] = None
    modified_at: Optional[str] = None
    reason: Optional[str] = None
    starts_at: Optional[str] = None
    status: Optional[str] = None
    summary: Optional[str] = None
    systems: Optional[List[Dict[str, Any]]] = None
    tlds: Optional[List[str]] = None
    type_value: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2DomainsMaintenancesMaintenanceIdResponse":
        if isinstance(data, dict):
            return GetV2DomainsMaintenancesMaintenanceIdResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                ends_at=(data.get("endsAt") if isinstance(data.get("endsAt"), str) else None),
                environment=(data.get("environment") if isinstance(data.get("environment"), str) else None),
                maintenance_id=(data.get("maintenanceId") if isinstance(data.get("maintenanceId"), str) else None),
                modified_at=(data.get("modifiedAt") if isinstance(data.get("modifiedAt"), str) else None),
                reason=(data.get("reason") if isinstance(data.get("reason"), str) else None),
                starts_at=(data.get("startsAt") if isinstance(data.get("startsAt"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                summary=(data.get("summary") if isinstance(data.get("summary"), str) else None),
                systems=(data.get("systems") if isinstance(data.get("systems"), list) else None),
                tlds=(data.get("tlds") if isinstance(data.get("tlds"), list) else None),
                type_value=(data.get("type") if isinstance(data.get("type"), str) else None),
            )
        if isinstance(data, list):
            return GetV2DomainsMaintenancesMaintenanceIdResponse(raw=data, items=data)
        return GetV2DomainsMaintenancesMaintenanceIdResponse(raw=data)

@dataclass(frozen=True)
class GetV2DomainsUsageYyyymmResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    details: Optional[List[Dict[str, Any]]] = None
    quota: Optional[int] = None
    total: Optional[int] = None
    yyyymm: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetV2DomainsUsageYyyymmResponse":
        if isinstance(data, dict):
            return GetV2DomainsUsageYyyymmResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                details=(data.get("details") if isinstance(data.get("details"), list) else None),
                quota=(data.get("quota") if isinstance(data.get("quota"), int) and not isinstance(data.get("quota"), bool) else None),
                total=(data.get("total") if isinstance(data.get("total"), int) and not isinstance(data.get("total"), bool) else None),
                yyyymm=(data.get("yyyymm") if isinstance(data.get("yyyymm"), str) else None),
            )
        if isinstance(data, list):
            return GetV2DomainsUsageYyyymmResponse(raw=data, items=data)
        return GetV2DomainsUsageYyyymmResponse(raw=data)

@dataclass(frozen=True)
class PatchV2CustomersCustomerIdDomainsDomainContactsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PatchV2CustomersCustomerIdDomainsDomainContactsResponse":
        if isinstance(data, dict):
            return PatchV2CustomersCustomerIdDomainsDomainContactsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PatchV2CustomersCustomerIdDomainsDomainContactsResponse(raw=data, items=data)
        return PatchV2CustomersCustomerIdDomainsDomainContactsResponse(raw=data)

@dataclass(frozen=True)
class PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeResponse":
        if isinstance(data, dict):
            return PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeResponse(raw=data, items=data)
        return PostV2CustomersCustomerIdDomainsDomainRegenerateAuthCodeResponse(raw=data)
