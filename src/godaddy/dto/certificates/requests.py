from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class CertificateCreateRequest:
    x_market_id: Optional[str] = None
    certificate_create: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Market-Id", self.x_market_id),
        ]

    def to_body(self) -> Any:
        return self.certificate_create

@dataclass(frozen=True)
class CertificateValidateRequest:
    x_market_id: Optional[str] = None
    certificate_create: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Market-Id", self.x_market_id),
        ]

    def to_body(self) -> Any:
        return self.certificate_create

@dataclass(frozen=True)
class CertificateGetRequest:
    certificate_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateActionRetrieveRequest:
    certificate_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateResendEmailRequest:
    certificate_id: Optional[str] = None
    email_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
            ("emailId", self.email_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateAlternateEmailAddressRequest:
    certificate_id: Optional[str] = None
    email_address: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
            ("emailAddress", self.email_address),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateResendEmailAddressRequest:
    certificate_id: Optional[str] = None
    email_id: Optional[str] = None
    email_address: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
            ("emailId", self.email_id),
            ("emailAddress", self.email_address),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateEmailHistoryRequest:
    certificate_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateCallbackGetRequest:
    certificate_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateCallbackReplaceRequest:
    certificate_id: Optional[str] = None
    callback_url: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("callbackUrl", self.callback_url),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateCallbackDeleteRequest:
    certificate_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateCancelRequest:
    certificate_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateDownloadRequest:
    certificate_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateReissueRequest:
    certificate_id: Optional[str] = None
    reissue_create: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.reissue_create

@dataclass(frozen=True)
class CertificateRenewRequest:
    certificate_id: Optional[str] = None
    renew_create: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.renew_create

@dataclass(frozen=True)
class CertificateRevokeRequest:
    certificate_id: Optional[str] = None
    certificate_revoke: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.certificate_revoke

@dataclass(frozen=True)
class CertificateSitesealGetRequest:
    certificate_id: Optional[str] = None
    theme: Optional[str] = None
    locale: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("theme", self.theme),
            ("locale", self.locale),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateVerifydomaincontrolRequest:
    certificate_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("certificateId", self.certificate_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateGetEntitlementRequest:
    entitlement_id: Optional[str] = None
    latest: Optional[bool] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("entitlementId", self.entitlement_id),
            ("latest", self.latest),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CertificateCreateRequest:
    x_market_id: Optional[str] = None
    subscription_certificate_create: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Market-Id", self.x_market_id),
        ]

    def to_body(self) -> Any:
        return self.subscription_certificate_create

@dataclass(frozen=True)
class CertificateDownloadEntitlementRequest:
    entitlement_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("entitlementId", self.entitlement_id),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetCustomerCertificatesByCustomerIdRequest:
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetCertificateDetailByCertIdentifierRequest:
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetDomainInformationByCertificateIdRequest:
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetDomainDetailsByDomainRequest:
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetAcmeExternalAccountBindingRequest:
    undefined: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class RetrieveSslByDomainResellerRequest:
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class RetrieveSslByDomainSubscriptionResellerRequest:
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None
    undefined: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None
