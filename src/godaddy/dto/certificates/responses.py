from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass(frozen=True)
class CertificateCreateResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    certificate_id: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateCreateResponse":
        if isinstance(data, dict):
            return CertificateCreateResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                certificate_id=(data.get("certificateId") if isinstance(data.get("certificateId"), str) else None),
            )
        if isinstance(data, list):
            return CertificateCreateResponse(raw=data, items=data)
        return CertificateCreateResponse(raw=data)

@dataclass(frozen=True)
class CertificateValidateResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateValidateResponse":
        if isinstance(data, dict):
            return CertificateValidateResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CertificateValidateResponse(raw=data, items=data)
        return CertificateValidateResponse(raw=data)

@dataclass(frozen=True)
class CertificateGetResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    certificate_id: Optional[str] = None
    common_name: Optional[str] = None
    contact: Optional[Dict[str, Any]] = None
    created_at: Optional[str] = None
    denied_reason: Optional[str] = None
    organization: Optional[Dict[str, Any]] = None
    period: Optional[int] = None
    product_type: Optional[str] = None
    progress: Optional[int] = None
    revoked_at: Optional[str] = None
    root_type: Optional[str] = None
    serial_number: Optional[str] = None
    serial_number_hex: Optional[str] = None
    slot_size: Optional[str] = None
    status: Optional[str] = None
    subject_alternative_names: Optional[List[Dict[str, Any]]] = None
    valid_end: Optional[str] = None
    valid_start: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateGetResponse":
        if isinstance(data, dict):
            return CertificateGetResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                certificate_id=(data.get("certificateId") if isinstance(data.get("certificateId"), str) else None),
                common_name=(data.get("commonName") if isinstance(data.get("commonName"), str) else None),
                contact=(data.get("contact") if isinstance(data.get("contact"), dict) else None),
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                denied_reason=(data.get("deniedReason") if isinstance(data.get("deniedReason"), str) else None),
                organization=(data.get("organization") if isinstance(data.get("organization"), dict) else None),
                period=(data.get("period") if isinstance(data.get("period"), int) and not isinstance(data.get("period"), bool) else None),
                product_type=(data.get("productType") if isinstance(data.get("productType"), str) else None),
                progress=(data.get("progress") if isinstance(data.get("progress"), int) and not isinstance(data.get("progress"), bool) else None),
                revoked_at=(data.get("revokedAt") if isinstance(data.get("revokedAt"), str) else None),
                root_type=(data.get("rootType") if isinstance(data.get("rootType"), str) else None),
                serial_number=(data.get("serialNumber") if isinstance(data.get("serialNumber"), str) else None),
                serial_number_hex=(data.get("serialNumberHex") if isinstance(data.get("serialNumberHex"), str) else None),
                slot_size=(data.get("slotSize") if isinstance(data.get("slotSize"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                subject_alternative_names=(data.get("subjectAlternativeNames") if isinstance(data.get("subjectAlternativeNames"), list) else None),
                valid_end=(data.get("validEnd") if isinstance(data.get("validEnd"), str) else None),
                valid_start=(data.get("validStart") if isinstance(data.get("validStart"), str) else None),
            )
        if isinstance(data, list):
            return CertificateGetResponse(raw=data, items=data)
        return CertificateGetResponse(raw=data)

@dataclass(frozen=True)
class CertificateActionRetrieveResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateActionRetrieveResponse":
        if isinstance(data, dict):
            return CertificateActionRetrieveResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CertificateActionRetrieveResponse(raw=data, items=data, array_items=data)
        return CertificateActionRetrieveResponse(raw=data)

@dataclass(frozen=True)
class CertificateResendEmailResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateResendEmailResponse":
        if isinstance(data, dict):
            return CertificateResendEmailResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CertificateResendEmailResponse(raw=data, items=data)
        return CertificateResendEmailResponse(raw=data)

@dataclass(frozen=True)
class CertificateAlternateEmailAddressResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    id: Optional[int] = None
    account_id: Optional[int] = None
    template_type: Optional[str] = None
    from_type: Optional[str] = None
    recipients: Optional[str] = None
    body: Optional[str] = None
    date_entered: Optional[str] = None
    subject: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateAlternateEmailAddressResponse":
        if isinstance(data, dict):
            return CertificateAlternateEmailAddressResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                id=(data.get("id") if isinstance(data.get("id"), int) and not isinstance(data.get("id"), bool) else None),
                account_id=(data.get("accountId") if isinstance(data.get("accountId"), int) and not isinstance(data.get("accountId"), bool) else None),
                template_type=(data.get("templateType") if isinstance(data.get("templateType"), str) else None),
                from_type=(data.get("fromType") if isinstance(data.get("fromType"), str) else None),
                recipients=(data.get("recipients") if isinstance(data.get("recipients"), str) else None),
                body=(data.get("body") if isinstance(data.get("body"), str) else None),
                date_entered=(data.get("dateEntered") if isinstance(data.get("dateEntered"), str) else None),
                subject=(data.get("subject") if isinstance(data.get("subject"), str) else None),
            )
        if isinstance(data, list):
            return CertificateAlternateEmailAddressResponse(raw=data, items=data)
        return CertificateAlternateEmailAddressResponse(raw=data)

@dataclass(frozen=True)
class CertificateResendEmailAddressResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateResendEmailAddressResponse":
        if isinstance(data, dict):
            return CertificateResendEmailAddressResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CertificateResendEmailAddressResponse(raw=data, items=data)
        return CertificateResendEmailAddressResponse(raw=data)

@dataclass(frozen=True)
class CertificateEmailHistoryResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    id: Optional[int] = None
    account_id: Optional[int] = None
    template_type: Optional[str] = None
    from_type: Optional[str] = None
    recipients: Optional[str] = None
    body: Optional[str] = None
    date_entered: Optional[str] = None
    subject: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateEmailHistoryResponse":
        if isinstance(data, dict):
            return CertificateEmailHistoryResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                id=(data.get("id") if isinstance(data.get("id"), int) and not isinstance(data.get("id"), bool) else None),
                account_id=(data.get("accountId") if isinstance(data.get("accountId"), int) and not isinstance(data.get("accountId"), bool) else None),
                template_type=(data.get("templateType") if isinstance(data.get("templateType"), str) else None),
                from_type=(data.get("fromType") if isinstance(data.get("fromType"), str) else None),
                recipients=(data.get("recipients") if isinstance(data.get("recipients"), str) else None),
                body=(data.get("body") if isinstance(data.get("body"), str) else None),
                date_entered=(data.get("dateEntered") if isinstance(data.get("dateEntered"), str) else None),
                subject=(data.get("subject") if isinstance(data.get("subject"), str) else None),
            )
        if isinstance(data, list):
            return CertificateEmailHistoryResponse(raw=data, items=data)
        return CertificateEmailHistoryResponse(raw=data)

@dataclass(frozen=True)
class CertificateCallbackGetResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    callback_url: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateCallbackGetResponse":
        if isinstance(data, dict):
            return CertificateCallbackGetResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                callback_url=(data.get("callbackUrl") if isinstance(data.get("callbackUrl"), str) else None),
            )
        if isinstance(data, list):
            return CertificateCallbackGetResponse(raw=data, items=data)
        return CertificateCallbackGetResponse(raw=data)

@dataclass(frozen=True)
class CertificateCallbackReplaceResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateCallbackReplaceResponse":
        if isinstance(data, dict):
            return CertificateCallbackReplaceResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CertificateCallbackReplaceResponse(raw=data, items=data)
        return CertificateCallbackReplaceResponse(raw=data)

@dataclass(frozen=True)
class CertificateCallbackDeleteResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateCallbackDeleteResponse":
        if isinstance(data, dict):
            return CertificateCallbackDeleteResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CertificateCallbackDeleteResponse(raw=data, items=data)
        return CertificateCallbackDeleteResponse(raw=data)

@dataclass(frozen=True)
class CertificateCancelResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateCancelResponse":
        if isinstance(data, dict):
            return CertificateCancelResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CertificateCancelResponse(raw=data, items=data)
        return CertificateCancelResponse(raw=data)

@dataclass(frozen=True)
class CertificateDownloadResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    pems: Optional[Dict[str, Any]] = None
    serial_number: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateDownloadResponse":
        if isinstance(data, dict):
            return CertificateDownloadResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                pems=(data.get("pems") if isinstance(data.get("pems"), dict) else None),
                serial_number=(data.get("serialNumber") if isinstance(data.get("serialNumber"), str) else None),
            )
        if isinstance(data, list):
            return CertificateDownloadResponse(raw=data, items=data)
        return CertificateDownloadResponse(raw=data)

@dataclass(frozen=True)
class CertificateReissueResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateReissueResponse":
        if isinstance(data, dict):
            return CertificateReissueResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CertificateReissueResponse(raw=data, items=data)
        return CertificateReissueResponse(raw=data)

@dataclass(frozen=True)
class CertificateRenewResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateRenewResponse":
        if isinstance(data, dict):
            return CertificateRenewResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CertificateRenewResponse(raw=data, items=data)
        return CertificateRenewResponse(raw=data)

@dataclass(frozen=True)
class CertificateRevokeResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateRevokeResponse":
        if isinstance(data, dict):
            return CertificateRevokeResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CertificateRevokeResponse(raw=data, items=data)
        return CertificateRevokeResponse(raw=data)

@dataclass(frozen=True)
class CertificateSitesealGetResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    html: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateSitesealGetResponse":
        if isinstance(data, dict):
            return CertificateSitesealGetResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                html=(data.get("html") if isinstance(data.get("html"), str) else None),
            )
        if isinstance(data, list):
            return CertificateSitesealGetResponse(raw=data, items=data)
        return CertificateSitesealGetResponse(raw=data)

@dataclass(frozen=True)
class CertificateVerifydomaincontrolResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateVerifydomaincontrolResponse":
        if isinstance(data, dict):
            return CertificateVerifydomaincontrolResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CertificateVerifydomaincontrolResponse(raw=data, items=data)
        return CertificateVerifydomaincontrolResponse(raw=data)

@dataclass(frozen=True)
class CertificateGetEntitlementResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateGetEntitlementResponse":
        if isinstance(data, dict):
            return CertificateGetEntitlementResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return CertificateGetEntitlementResponse(raw=data, items=data, array_items=data)
        return CertificateGetEntitlementResponse(raw=data)

@dataclass(frozen=True)
class CertificateCreateResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    certificate_id: Optional[str] = None
    subscription_id: Optional[str] = None
    subscription_created_for_order: Optional[bool] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateCreateResponse":
        if isinstance(data, dict):
            return CertificateCreateResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                certificate_id=(data.get("certificateId") if isinstance(data.get("certificateId"), str) else None),
                subscription_id=(data.get("subscriptionId") if isinstance(data.get("subscriptionId"), str) else None),
                subscription_created_for_order=(data.get("subscriptionCreatedForOrder") if isinstance(data.get("subscriptionCreatedForOrder"), bool) else None),
            )
        if isinstance(data, list):
            return CertificateCreateResponse(raw=data, items=data)
        return CertificateCreateResponse(raw=data)

@dataclass(frozen=True)
class CertificateDownloadEntitlementResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    pems: Optional[Dict[str, Any]] = None
    serial_number: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CertificateDownloadEntitlementResponse":
        if isinstance(data, dict):
            return CertificateDownloadEntitlementResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                pems=(data.get("pems") if isinstance(data.get("pems"), dict) else None),
                serial_number=(data.get("serialNumber") if isinstance(data.get("serialNumber"), str) else None),
            )
        if isinstance(data, list):
            return CertificateDownloadEntitlementResponse(raw=data, items=data)
        return CertificateDownloadEntitlementResponse(raw=data)

@dataclass(frozen=True)
class GetCustomerCertificatesByCustomerIdResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    certificates: Optional[List[Dict[str, Any]]] = None
    pagination: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetCustomerCertificatesByCustomerIdResponse":
        if isinstance(data, dict):
            return GetCustomerCertificatesByCustomerIdResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                certificates=(data.get("certificates") if isinstance(data.get("certificates"), list) else None),
                pagination=(data.get("pagination") if isinstance(data.get("pagination"), dict) else None),
            )
        if isinstance(data, list):
            return GetCustomerCertificatesByCustomerIdResponse(raw=data, items=data)
        return GetCustomerCertificatesByCustomerIdResponse(raw=data)

@dataclass(frozen=True)
class GetCertificateDetailByCertIdentifierResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    certificate_id: Optional[str] = None
    common_name: Optional[str] = None
    period: Optional[int] = None
    type_value: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    completed_at: Optional[str] = None
    valid_end_at: Optional[str] = None
    valid_start_at: Optional[str] = None
    revoked_at: Optional[str] = None
    renewal_available: Optional[bool] = None
    serial_number: Optional[str] = None
    serial_number_hex: Optional[str] = None
    slot_size: Optional[str] = None
    subject_alternative_names: Optional[List[str]] = None
    contact: Optional[Dict[str, Any]] = None
    organization: Optional[Dict[str, Any]] = None
    csr: Optional[str] = None
    root_type: Optional[str] = None
    denied_reason: Optional[str] = None
    progress: Optional[int] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetCertificateDetailByCertIdentifierResponse":
        if isinstance(data, dict):
            return GetCertificateDetailByCertIdentifierResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                certificate_id=(data.get("certificateId") if isinstance(data.get("certificateId"), str) else None),
                common_name=(data.get("commonName") if isinstance(data.get("commonName"), str) else None),
                period=(data.get("period") if isinstance(data.get("period"), int) and not isinstance(data.get("period"), bool) else None),
                type_value=(data.get("type") if isinstance(data.get("type"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                completed_at=(data.get("completedAt") if isinstance(data.get("completedAt"), str) else None),
                valid_end_at=(data.get("validEndAt") if isinstance(data.get("validEndAt"), str) else None),
                valid_start_at=(data.get("validStartAt") if isinstance(data.get("validStartAt"), str) else None),
                revoked_at=(data.get("revokedAt") if isinstance(data.get("revokedAt"), str) else None),
                renewal_available=(data.get("renewalAvailable") if isinstance(data.get("renewalAvailable"), bool) else None),
                serial_number=(data.get("serialNumber") if isinstance(data.get("serialNumber"), str) else None),
                serial_number_hex=(data.get("serialNumberHex") if isinstance(data.get("serialNumberHex"), str) else None),
                slot_size=(data.get("slotSize") if isinstance(data.get("slotSize"), str) else None),
                subject_alternative_names=(data.get("subjectAlternativeNames") if isinstance(data.get("subjectAlternativeNames"), list) else None),
                contact=(data.get("contact") if isinstance(data.get("contact"), dict) else None),
                organization=(data.get("organization") if isinstance(data.get("organization"), dict) else None),
                csr=(data.get("csr") if isinstance(data.get("csr"), str) else None),
                root_type=(data.get("rootType") if isinstance(data.get("rootType"), str) else None),
                denied_reason=(data.get("deniedReason") if isinstance(data.get("deniedReason"), str) else None),
                progress=(data.get("progress") if isinstance(data.get("progress"), int) and not isinstance(data.get("progress"), bool) else None),
            )
        if isinstance(data, list):
            return GetCertificateDetailByCertIdentifierResponse(raw=data, items=data)
        return GetCertificateDetailByCertIdentifierResponse(raw=data)

@dataclass(frozen=True)
class GetDomainInformationByCertificateIdResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetDomainInformationByCertificateIdResponse":
        if isinstance(data, dict):
            return GetDomainInformationByCertificateIdResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return GetDomainInformationByCertificateIdResponse(raw=data, items=data, array_items=data)
        return GetDomainInformationByCertificateIdResponse(raw=data)

@dataclass(frozen=True)
class GetDomainDetailsByDomainResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    domain: Optional[str] = None
    domain_entity_id: Optional[int] = None
    dce_token: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    modified_at: Optional[str] = None
    type_value: Optional[str] = None
    usage: Optional[str] = None
    certificate_authority_authorization: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetDomainDetailsByDomainResponse":
        if isinstance(data, dict):
            return GetDomainDetailsByDomainResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                domain=(data.get("domain") if isinstance(data.get("domain"), str) else None),
                domain_entity_id=(data.get("domainEntityId") if isinstance(data.get("domainEntityId"), int) and not isinstance(data.get("domainEntityId"), bool) else None),
                dce_token=(data.get("dceToken") if isinstance(data.get("dceToken"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                modified_at=(data.get("modifiedAt") if isinstance(data.get("modifiedAt"), str) else None),
                type_value=(data.get("type") if isinstance(data.get("type"), str) else None),
                usage=(data.get("usage") if isinstance(data.get("usage"), str) else None),
                certificate_authority_authorization=(data.get("certificateAuthorityAuthorization") if isinstance(data.get("certificateAuthorityAuthorization"), dict) else None),
            )
        if isinstance(data, list):
            return GetDomainDetailsByDomainResponse(raw=data, items=data)
        return GetDomainDetailsByDomainResponse(raw=data)

@dataclass(frozen=True)
class GetAcmeExternalAccountBindingResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    directory_url: Optional[str] = None
    key_id: Optional[str] = None
    hmac_key: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetAcmeExternalAccountBindingResponse":
        if isinstance(data, dict):
            return GetAcmeExternalAccountBindingResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                directory_url=(data.get("directoryUrl") if isinstance(data.get("directoryUrl"), str) else None),
                key_id=(data.get("keyId") if isinstance(data.get("keyId"), str) else None),
                hmac_key=(data.get("hmacKey") if isinstance(data.get("hmacKey"), str) else None),
            )
        if isinstance(data, list):
            return GetAcmeExternalAccountBindingResponse(raw=data, items=data)
        return GetAcmeExternalAccountBindingResponse(raw=data)

@dataclass(frozen=True)
class RetrieveSslByDomainResellerResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    current_page: Optional[int] = None
    data: Optional[List[Dict[str, Any]]] = None
    page_size: Optional[int] = None
    total: Optional[int] = None

    @staticmethod
    def from_mixed(data: Any) -> "RetrieveSslByDomainResellerResponse":
        if isinstance(data, dict):
            return RetrieveSslByDomainResellerResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                current_page=(data.get("currentPage") if isinstance(data.get("currentPage"), int) and not isinstance(data.get("currentPage"), bool) else None),
                data=(data.get("data") if isinstance(data.get("data"), list) else None),
                page_size=(data.get("pageSize") if isinstance(data.get("pageSize"), int) and not isinstance(data.get("pageSize"), bool) else None),
                total=(data.get("total") if isinstance(data.get("total"), int) and not isinstance(data.get("total"), bool) else None),
            )
        if isinstance(data, list):
            return RetrieveSslByDomainResellerResponse(raw=data, items=data)
        return RetrieveSslByDomainResellerResponse(raw=data)

@dataclass(frozen=True)
class RetrieveSslByDomainSubscriptionResellerResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    allowed_domains: Optional[List[str]] = None
    domain: Optional[str] = None
    guid: Optional[str] = None
    max_domains: Optional[int] = None
    subscription_end_date: Optional[str] = None
    subscription_start_date: Optional[str] = None
    subscription_status: Optional[str] = None
    current_page: Optional[int] = None
    data: Optional[List[Dict[str, Any]]] = None
    page_size: Optional[int] = None
    total: Optional[int] = None

    @staticmethod
    def from_mixed(data: Any) -> "RetrieveSslByDomainSubscriptionResellerResponse":
        if isinstance(data, dict):
            return RetrieveSslByDomainSubscriptionResellerResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                allowed_domains=(data.get("allowedDomains") if isinstance(data.get("allowedDomains"), list) else None),
                domain=(data.get("domain") if isinstance(data.get("domain"), str) else None),
                guid=(data.get("guid") if isinstance(data.get("guid"), str) else None),
                max_domains=(data.get("maxDomains") if isinstance(data.get("maxDomains"), int) and not isinstance(data.get("maxDomains"), bool) else None),
                subscription_end_date=(data.get("subscriptionEndDate") if isinstance(data.get("subscriptionEndDate"), str) else None),
                subscription_start_date=(data.get("subscriptionStartDate") if isinstance(data.get("subscriptionStartDate"), str) else None),
                subscription_status=(data.get("subscriptionStatus") if isinstance(data.get("subscriptionStatus"), str) else None),
                current_page=(data.get("currentPage") if isinstance(data.get("currentPage"), int) and not isinstance(data.get("currentPage"), bool) else None),
                data=(data.get("data") if isinstance(data.get("data"), list) else None),
                page_size=(data.get("pageSize") if isinstance(data.get("pageSize"), int) and not isinstance(data.get("pageSize"), bool) else None),
                total=(data.get("total") if isinstance(data.get("total"), int) and not isinstance(data.get("total"), bool) else None),
            )
        if isinstance(data, list):
            return RetrieveSslByDomainSubscriptionResellerResponse(raw=data, items=data)
        return RetrieveSslByDomainSubscriptionResellerResponse(raw=data)
