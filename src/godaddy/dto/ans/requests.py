from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class SearchAnsnameRequest:
    agent_display_name: Optional[str] = None
    version: Optional[str] = None
    agent_host: Optional[str] = None
    protocol: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("agentDisplayName", self.agent_display_name),
            ("version", self.version),
            ("agentHost", self.agent_host),
            ("protocol", self.protocol),
            ("limit", self.limit),
            ("offset", self.offset),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class RegisterAgentRequest:
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
class ResolveAnsnameRequest:
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
class GetAgentRequest:
    agent_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("agentId", self.agent_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class RevokeAgentRequest:
    agent_id: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("agentId", self.agent_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class ValidateRegistrationRequest:
    agent_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("agentId", self.agent_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class VerifyDnsRecordsRequest:
    agent_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("agentId", self.agent_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetAgentIdentityCertificateByAgentIdRequest:
    agent_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("agentId", self.agent_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class SubmitAgentIdentityCsrByAgentIdRequest:
    agent_id: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("agentId", self.agent_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class GetAgentServerCertificateByAgentIdRequest:
    agent_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("agentId", self.agent_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class SubmitAgentServerCsrByAgentIdRequest:
    agent_id: Optional[str] = None
    body: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("agentId", self.agent_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.body

@dataclass(frozen=True)
class GetAgentCsrStatusByAgentIdRequest:
    agent_id: Optional[str] = None
    csr_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("agentId", self.agent_id),
            ("csrId", self.csr_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetAgentEventsRequest:
    x_request_id: Optional[str] = None
    provider_id: Optional[str] = None
    last_log_id: Optional[str] = None
    limit: Optional[int] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("providerId", self.provider_id),
            ("lastLogId", self.last_log_id),
            ("limit", self.limit),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None
