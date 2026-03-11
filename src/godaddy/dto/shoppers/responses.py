from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass(frozen=True)
class CreateSubaccountResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    customer_id: Optional[str] = None
    shopper_id: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "CreateSubaccountResponse":
        if isinstance(data, dict):
            return CreateSubaccountResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                customer_id=(data.get("customerId") if isinstance(data.get("customerId"), str) else None),
                shopper_id=(data.get("shopperId") if isinstance(data.get("shopperId"), str) else None),
            )
        if isinstance(data, list):
            return CreateSubaccountResponse(raw=data, items=data)
        return CreateSubaccountResponse(raw=data)

@dataclass(frozen=True)
class GetResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    customer_id: Optional[str] = None
    email: Optional[str] = None
    external_id: Optional[int] = None
    market_id: Optional[str] = None
    name_first: Optional[str] = None
    name_last: Optional[str] = None
    shopper_id: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetResponse":
        if isinstance(data, dict):
            return GetResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                customer_id=(data.get("customerId") if isinstance(data.get("customerId"), str) else None),
                email=(data.get("email") if isinstance(data.get("email"), str) else None),
                external_id=(data.get("externalId") if isinstance(data.get("externalId"), int) and not isinstance(data.get("externalId"), bool) else None),
                market_id=(data.get("marketId") if isinstance(data.get("marketId"), str) else None),
                name_first=(data.get("nameFirst") if isinstance(data.get("nameFirst"), str) else None),
                name_last=(data.get("nameLast") if isinstance(data.get("nameLast"), str) else None),
                shopper_id=(data.get("shopperId") if isinstance(data.get("shopperId"), str) else None),
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
    customer_id: Optional[str] = None
    shopper_id: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "UpdateResponse":
        if isinstance(data, dict):
            return UpdateResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                customer_id=(data.get("customerId") if isinstance(data.get("customerId"), str) else None),
                shopper_id=(data.get("shopperId") if isinstance(data.get("shopperId"), str) else None),
            )
        if isinstance(data, list):
            return UpdateResponse(raw=data, items=data)
        return UpdateResponse(raw=data)

@dataclass(frozen=True)
class DeleteResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "DeleteResponse":
        if isinstance(data, dict):
            return DeleteResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return DeleteResponse(raw=data, items=data)
        return DeleteResponse(raw=data)

@dataclass(frozen=True)
class GetStatusResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    billing_state: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetStatusResponse":
        if isinstance(data, dict):
            return GetStatusResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                billing_state=(data.get("billingState") if isinstance(data.get("billingState"), str) else None),
            )
        if isinstance(data, list):
            return GetStatusResponse(raw=data, items=data)
        return GetStatusResponse(raw=data)

@dataclass(frozen=True)
class ChangePasswordResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    customer_id: Optional[str] = None
    shopper_id: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "ChangePasswordResponse":
        if isinstance(data, dict):
            return ChangePasswordResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                customer_id=(data.get("customerId") if isinstance(data.get("customerId"), str) else None),
                shopper_id=(data.get("shopperId") if isinstance(data.get("shopperId"), str) else None),
            )
        if isinstance(data, list):
            return ChangePasswordResponse(raw=data, items=data)
        return ChangePasswordResponse(raw=data)
