from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass(frozen=True)
class SearchAnsnameResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    agents: Optional[List[Dict[str, Any]]] = None
    has_more: Optional[bool] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    returned_count: Optional[int] = None
    search_criteria: Optional[Dict[str, Any]] = None
    total_count: Optional[int] = None

    @staticmethod
    def from_mixed(data: Any) -> "SearchAnsnameResponse":
        if isinstance(data, dict):
            return SearchAnsnameResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                agents=(data.get("agents") if isinstance(data.get("agents"), list) else None),
                has_more=(data.get("hasMore") if isinstance(data.get("hasMore"), bool) else None),
                limit=(data.get("limit") if isinstance(data.get("limit"), int) and not isinstance(data.get("limit"), bool) else None),
                offset=(data.get("offset") if isinstance(data.get("offset"), int) and not isinstance(data.get("offset"), bool) else None),
                returned_count=(data.get("returnedCount") if isinstance(data.get("returnedCount"), int) and not isinstance(data.get("returnedCount"), bool) else None),
                search_criteria=(data.get("searchCriteria") if isinstance(data.get("searchCriteria"), dict) else None),
                total_count=(data.get("totalCount") if isinstance(data.get("totalCount"), int) and not isinstance(data.get("totalCount"), bool) else None),
            )
        if isinstance(data, list):
            return SearchAnsnameResponse(raw=data, items=data)
        return SearchAnsnameResponse(raw=data)

@dataclass(frozen=True)
class RegisterAgentResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    ans_name: Optional[str] = None
    challenges: Optional[List[Dict[str, Any]]] = None
    dns_records: Optional[List[Dict[str, Any]]] = None
    expires_at: Optional[str] = None
    links: Optional[List[Dict[str, Any]]] = None
    next_steps: Optional[List[Dict[str, Any]]] = None
    status: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "RegisterAgentResponse":
        if isinstance(data, dict):
            return RegisterAgentResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                ans_name=(data.get("ansName") if isinstance(data.get("ansName"), str) else None),
                challenges=(data.get("challenges") if isinstance(data.get("challenges"), list) else None),
                dns_records=(data.get("dnsRecords") if isinstance(data.get("dnsRecords"), list) else None),
                expires_at=(data.get("expiresAt") if isinstance(data.get("expiresAt"), str) else None),
                links=(data.get("links") if isinstance(data.get("links"), list) else None),
                next_steps=(data.get("nextSteps") if isinstance(data.get("nextSteps"), list) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
            )
        if isinstance(data, list):
            return RegisterAgentResponse(raw=data, items=data)
        return RegisterAgentResponse(raw=data)

@dataclass(frozen=True)
class ResolveAnsnameResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    ans_name: Optional[str] = None
    links: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "ResolveAnsnameResponse":
        if isinstance(data, dict):
            return ResolveAnsnameResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                ans_name=(data.get("ansName") if isinstance(data.get("ansName"), str) else None),
                links=(data.get("links") if isinstance(data.get("links"), list) else None),
            )
        if isinstance(data, list):
            return ResolveAnsnameResponse(raw=data, items=data)
        return ResolveAnsnameResponse(raw=data)

@dataclass(frozen=True)
class GetAgentResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    agent_description: Optional[str] = None
    agent_host: Optional[str] = None
    agent_id: Optional[str] = None
    agent_display_name: Optional[str] = None
    agent_status: Optional[str] = None
    ans_name: Optional[str] = None
    endpoints: Optional[List[Dict[str, Any]]] = None
    last_renewal_timestamp: Optional[str] = None
    links: Optional[List[Dict[str, Any]]] = None
    registration_timestamp: Optional[str] = None
    version: Optional[str] = None
    registration_pending: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetAgentResponse":
        if isinstance(data, dict):
            return GetAgentResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                agent_description=(data.get("agentDescription") if isinstance(data.get("agentDescription"), str) else None),
                agent_host=(data.get("agentHost") if isinstance(data.get("agentHost"), str) else None),
                agent_id=(data.get("agentId") if isinstance(data.get("agentId"), str) else None),
                agent_display_name=(data.get("agentDisplayName") if isinstance(data.get("agentDisplayName"), str) else None),
                agent_status=(data.get("agentStatus") if isinstance(data.get("agentStatus"), str) else None),
                ans_name=(data.get("ansName") if isinstance(data.get("ansName"), str) else None),
                endpoints=(data.get("endpoints") if isinstance(data.get("endpoints"), list) else None),
                last_renewal_timestamp=(data.get("lastRenewalTimestamp") if isinstance(data.get("lastRenewalTimestamp"), str) else None),
                links=(data.get("links") if isinstance(data.get("links"), list) else None),
                registration_timestamp=(data.get("registrationTimestamp") if isinstance(data.get("registrationTimestamp"), str) else None),
                version=(data.get("version") if isinstance(data.get("version"), str) else None),
                registration_pending=(data.get("registrationPending") if isinstance(data.get("registrationPending"), dict) else None),
            )
        if isinstance(data, list):
            return GetAgentResponse(raw=data, items=data)
        return GetAgentResponse(raw=data)

@dataclass(frozen=True)
class RevokeAgentResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    agent_id: Optional[str] = None
    ans_name: Optional[str] = None
    status: Optional[str] = None
    revoked_at: Optional[str] = None
    reason: Optional[str] = None
    links: Optional[List[Dict[str, Any]]] = None
    dns_records_to_remove: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "RevokeAgentResponse":
        if isinstance(data, dict):
            return RevokeAgentResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                agent_id=(data.get("agentId") if isinstance(data.get("agentId"), str) else None),
                ans_name=(data.get("ansName") if isinstance(data.get("ansName"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                revoked_at=(data.get("revokedAt") if isinstance(data.get("revokedAt"), str) else None),
                reason=(data.get("reason") if isinstance(data.get("reason"), str) else None),
                links=(data.get("links") if isinstance(data.get("links"), list) else None),
                dns_records_to_remove=(data.get("dnsRecordsToRemove") if isinstance(data.get("dnsRecordsToRemove"), list) else None),
            )
        if isinstance(data, list):
            return RevokeAgentResponse(raw=data, items=data)
        return RevokeAgentResponse(raw=data)

@dataclass(frozen=True)
class ValidateRegistrationResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    completed_steps: Optional[List[str]] = None
    created_at: Optional[str] = None
    expires_at: Optional[str] = None
    pending_steps: Optional[List[str]] = None
    phase: Optional[str] = None
    status: Optional[str] = None
    updated_at: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "ValidateRegistrationResponse":
        if isinstance(data, dict):
            return ValidateRegistrationResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                completed_steps=(data.get("completedSteps") if isinstance(data.get("completedSteps"), list) else None),
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                expires_at=(data.get("expiresAt") if isinstance(data.get("expiresAt"), str) else None),
                pending_steps=(data.get("pendingSteps") if isinstance(data.get("pendingSteps"), list) else None),
                phase=(data.get("phase") if isinstance(data.get("phase"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                updated_at=(data.get("updatedAt") if isinstance(data.get("updatedAt"), str) else None),
            )
        if isinstance(data, list):
            return ValidateRegistrationResponse(raw=data, items=data)
        return ValidateRegistrationResponse(raw=data)

@dataclass(frozen=True)
class VerifyDnsRecordsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    completed_steps: Optional[List[str]] = None
    created_at: Optional[str] = None
    expires_at: Optional[str] = None
    pending_steps: Optional[List[str]] = None
    phase: Optional[str] = None
    status: Optional[str] = None
    updated_at: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "VerifyDnsRecordsResponse":
        if isinstance(data, dict):
            return VerifyDnsRecordsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                completed_steps=(data.get("completedSteps") if isinstance(data.get("completedSteps"), list) else None),
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                expires_at=(data.get("expiresAt") if isinstance(data.get("expiresAt"), str) else None),
                pending_steps=(data.get("pendingSteps") if isinstance(data.get("pendingSteps"), list) else None),
                phase=(data.get("phase") if isinstance(data.get("phase"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                updated_at=(data.get("updatedAt") if isinstance(data.get("updatedAt"), str) else None),
            )
        if isinstance(data, list):
            return VerifyDnsRecordsResponse(raw=data, items=data)
        return VerifyDnsRecordsResponse(raw=data)

@dataclass(frozen=True)
class GetAgentIdentityCertificateByAgentIdResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetAgentIdentityCertificateByAgentIdResponse":
        if isinstance(data, dict):
            return GetAgentIdentityCertificateByAgentIdResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return GetAgentIdentityCertificateByAgentIdResponse(raw=data, items=data, array_items=data)
        return GetAgentIdentityCertificateByAgentIdResponse(raw=data)

@dataclass(frozen=True)
class SubmitAgentIdentityCsrByAgentIdResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    csr_id: Optional[str] = None
    message_field: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "SubmitAgentIdentityCsrByAgentIdResponse":
        if isinstance(data, dict):
            return SubmitAgentIdentityCsrByAgentIdResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                csr_id=(data.get("csrId") if isinstance(data.get("csrId"), str) else None),
                message_field=(data.get("message") if isinstance(data.get("message"), str) else None),
            )
        if isinstance(data, list):
            return SubmitAgentIdentityCsrByAgentIdResponse(raw=data, items=data)
        return SubmitAgentIdentityCsrByAgentIdResponse(raw=data)

@dataclass(frozen=True)
class GetAgentServerCertificateByAgentIdResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetAgentServerCertificateByAgentIdResponse":
        if isinstance(data, dict):
            return GetAgentServerCertificateByAgentIdResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return GetAgentServerCertificateByAgentIdResponse(raw=data, items=data, array_items=data)
        return GetAgentServerCertificateByAgentIdResponse(raw=data)

@dataclass(frozen=True)
class SubmitAgentServerCsrByAgentIdResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    csr_id: Optional[str] = None
    message_field: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "SubmitAgentServerCsrByAgentIdResponse":
        if isinstance(data, dict):
            return SubmitAgentServerCsrByAgentIdResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                csr_id=(data.get("csrId") if isinstance(data.get("csrId"), str) else None),
                message_field=(data.get("message") if isinstance(data.get("message"), str) else None),
            )
        if isinstance(data, list):
            return SubmitAgentServerCsrByAgentIdResponse(raw=data, items=data)
        return SubmitAgentServerCsrByAgentIdResponse(raw=data)

@dataclass(frozen=True)
class GetAgentCsrStatusByAgentIdResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    csr_id: Optional[str] = None
    failure_reason: Optional[str] = None
    status: Optional[str] = None
    submitted_at: Optional[str] = None
    type_value: Optional[str] = None
    updated_at: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetAgentCsrStatusByAgentIdResponse":
        if isinstance(data, dict):
            return GetAgentCsrStatusByAgentIdResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                csr_id=(data.get("csrId") if isinstance(data.get("csrId"), str) else None),
                failure_reason=(data.get("failureReason") if isinstance(data.get("failureReason"), str) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                submitted_at=(data.get("submittedAt") if isinstance(data.get("submittedAt"), str) else None),
                type_value=(data.get("type") if isinstance(data.get("type"), str) else None),
                updated_at=(data.get("updatedAt") if isinstance(data.get("updatedAt"), str) else None),
            )
        if isinstance(data, list):
            return GetAgentCsrStatusByAgentIdResponse(raw=data, items=data)
        return GetAgentCsrStatusByAgentIdResponse(raw=data)

@dataclass(frozen=True)
class GetAgentEventsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    items_field: Optional[List[Dict[str, Any]]] = None
    last_log_id: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetAgentEventsResponse":
        if isinstance(data, dict):
            return GetAgentEventsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                items_field=(data.get("items") if isinstance(data.get("items"), list) else None),
                last_log_id=(data.get("lastLogId") if isinstance(data.get("lastLogId"), str) else None),
            )
        if isinstance(data, list):
            return GetAgentEventsResponse(raw=data, items=data)
        return GetAgentEventsResponse(raw=data)
