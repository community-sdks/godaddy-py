from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class GetTicketsRequest:
    type_value: Optional[str] = None
    closed: Optional[bool] = None
    source_domain_or_ip: Optional[str] = None
    target: Optional[str] = None
    created_start: Optional[str] = None
    created_end: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("type", self.type_value),
            ("closed", self.closed),
            ("sourceDomainOrIp", self.source_domain_or_ip),
            ("target", self.target),
            ("createdStart", self.created_start),
            ("createdEnd", self.created_end),
            ("limit", self.limit),
            ("offset", self.offset),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CreateTicketRequest:
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
class GetTicketInfoRequest:
    ticket_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("ticketId", self.ticket_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetTicketsV2Request:
    type_value: Optional[str] = None
    closed: Optional[bool] = None
    source_domain_or_ip: Optional[str] = None
    target: Optional[str] = None
    created_start: Optional[str] = None
    created_end: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("type", self.type_value),
            ("closed", self.closed),
            ("sourceDomainOrIp", self.source_domain_or_ip),
            ("target", self.target),
            ("createdStart", self.created_start),
            ("createdEnd", self.created_end),
            ("limit", self.limit),
            ("offset", self.offset),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class CreateTicketV2Request:
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
class GetTicketInfoV2Request:
    ticket_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("ticketId", self.ticket_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None
