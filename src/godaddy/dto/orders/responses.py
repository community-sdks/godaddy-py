from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass(frozen=True)
class ListResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    orders: Optional[List[Dict[str, Any]]] = None
    pagination: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_mixed(data: Any) -> "ListResponse":
        if isinstance(data, dict):
            return ListResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                orders=(data.get("orders") if isinstance(data.get("orders"), list) else None),
                pagination=(data.get("pagination") if isinstance(data.get("pagination"), dict) else None),
            )
        if isinstance(data, list):
            return ListResponse(raw=data, items=data)
        return ListResponse(raw=data)

@dataclass(frozen=True)
class GetResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    bill_to: Optional[Dict[str, Any]] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    items_field: Optional[List[Dict[str, Any]]] = None
    order_id: Optional[str] = None
    parent_order_id: Optional[str] = None
    payments: Optional[List[Dict[str, Any]]] = None
    pricing: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetResponse":
        if isinstance(data, dict):
            return GetResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                bill_to=(data.get("billTo") if isinstance(data.get("billTo"), dict) else None),
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                currency=(data.get("currency") if isinstance(data.get("currency"), str) else None),
                items_field=(data.get("items") if isinstance(data.get("items"), list) else None),
                order_id=(data.get("orderId") if isinstance(data.get("orderId"), str) else None),
                parent_order_id=(data.get("parentOrderId") if isinstance(data.get("parentOrderId"), str) else None),
                payments=(data.get("payments") if isinstance(data.get("payments"), list) else None),
                pricing=(data.get("pricing") if isinstance(data.get("pricing"), dict) else None),
            )
        if isinstance(data, list):
            return GetResponse(raw=data, items=data)
        return GetResponse(raw=data)
