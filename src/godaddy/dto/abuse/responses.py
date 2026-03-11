from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass(frozen=True)
class GetTicketsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    pagination: Optional[Dict[str, Any]] = None
    ticket_ids: Optional[List[str]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetTicketsResponse":
        if isinstance(data, dict):
            return GetTicketsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                pagination=(data.get("pagination") if isinstance(data.get("pagination"), dict) else None),
                ticket_ids=(data.get("ticketIds") if isinstance(data.get("ticketIds"), list) else None),
            )
        if isinstance(data, list):
            return GetTicketsResponse(raw=data, items=data)
        return GetTicketsResponse(raw=data)

@dataclass(frozen=True)
class CreateTicketResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    u_number: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CreateTicketResponse":
        if isinstance(data, dict):
            return CreateTicketResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                u_number=(data.get("u_number") if isinstance(data.get("u_number"), str) else None),
            )
        if isinstance(data, list):
            return CreateTicketResponse(raw=data, items=data)
        return CreateTicketResponse(raw=data)

@dataclass(frozen=True)
class GetTicketInfoResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    closed: Optional[bool] = None
    closed_at: Optional[str] = None
    created_at: Optional[str] = None
    domain_ip: Optional[str] = None
    reporter: Optional[str] = None
    source: Optional[str] = None
    target: Optional[str] = None
    ticket_id: Optional[str] = None
    type_value: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetTicketInfoResponse":
        if isinstance(data, dict):
            return GetTicketInfoResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                closed=(data.get("closed") if isinstance(data.get("closed"), bool) else None),
                closed_at=(data.get("closedAt") if isinstance(data.get("closedAt"), str) else None),
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                domain_ip=(data.get("domainIp") if isinstance(data.get("domainIp"), str) else None),
                reporter=(data.get("reporter") if isinstance(data.get("reporter"), str) else None),
                source=(data.get("source") if isinstance(data.get("source"), str) else None),
                target=(data.get("target") if isinstance(data.get("target"), str) else None),
                ticket_id=(data.get("ticketId") if isinstance(data.get("ticketId"), str) else None),
                type_value=(data.get("type") if isinstance(data.get("type"), str) else None),
            )
        if isinstance(data, list):
            return GetTicketInfoResponse(raw=data, items=data)
        return GetTicketInfoResponse(raw=data)

@dataclass(frozen=True)
class GetTicketsV2Response:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    pagination: Optional[Dict[str, Any]] = None
    ticket_ids: Optional[List[str]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetTicketsV2Response":
        if isinstance(data, dict):
            return GetTicketsV2Response(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                pagination=(data.get("pagination") if isinstance(data.get("pagination"), dict) else None),
                ticket_ids=(data.get("ticketIds") if isinstance(data.get("ticketIds"), list) else None),
            )
        if isinstance(data, list):
            return GetTicketsV2Response(raw=data, items=data)
        return GetTicketsV2Response(raw=data)

@dataclass(frozen=True)
class CreateTicketV2Response:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    u_number: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CreateTicketV2Response":
        if isinstance(data, dict):
            return CreateTicketV2Response(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                u_number=(data.get("u_number") if isinstance(data.get("u_number"), str) else None),
            )
        if isinstance(data, list):
            return CreateTicketV2Response(raw=data, items=data)
        return CreateTicketV2Response(raw=data)

@dataclass(frozen=True)
class GetTicketInfoV2Response:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    closed: Optional[bool] = None
    closed_at: Optional[str] = None
    created_at: Optional[str] = None
    domain_ip: Optional[str] = None
    reporter: Optional[str] = None
    source: Optional[str] = None
    target: Optional[str] = None
    ticket_id: Optional[str] = None
    type_value: Optional[str] = None
    close_reason: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetTicketInfoV2Response":
        if isinstance(data, dict):
            return GetTicketInfoV2Response(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                closed=(data.get("closed") if isinstance(data.get("closed"), bool) else None),
                closed_at=(data.get("closedAt") if isinstance(data.get("closedAt"), str) else None),
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                domain_ip=(data.get("domainIp") if isinstance(data.get("domainIp"), str) else None),
                reporter=(data.get("reporter") if isinstance(data.get("reporter"), str) else None),
                source=(data.get("source") if isinstance(data.get("source"), str) else None),
                target=(data.get("target") if isinstance(data.get("target"), str) else None),
                ticket_id=(data.get("ticketId") if isinstance(data.get("ticketId"), str) else None),
                type_value=(data.get("type") if isinstance(data.get("type"), str) else None),
                close_reason=(data.get("closeReason") if isinstance(data.get("closeReason"), str) else None),
            )
        if isinstance(data, list):
            return GetTicketInfoV2Response(raw=data, items=data)
        return GetTicketInfoV2Response(raw=data)
