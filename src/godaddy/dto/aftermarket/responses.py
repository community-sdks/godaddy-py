from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass(frozen=True)
class GetListingsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    listings: Optional[List[Dict[str, Any]]] = None
    pagination: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetListingsResponse":
        if isinstance(data, dict):
            return GetListingsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                listings=(data.get("listings") if isinstance(data.get("listings"), list) else None),
                pagination=(data.get("pagination") if isinstance(data.get("pagination"), dict) else None),
            )
        if isinstance(data, list):
            return GetListingsResponse(raw=data, items=data)
        return GetListingsResponse(raw=data)

@dataclass(frozen=True)
class DeleteListingsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    listing_action_id: Optional[int] = None

    @staticmethod
    def from_mixed(data: Any) -> "DeleteListingsResponse":
        if isinstance(data, dict):
            return DeleteListingsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                listing_action_id=(data.get("listingActionId") if isinstance(data.get("listingActionId"), int) and not isinstance(data.get("listingActionId"), bool) else None),
            )
        if isinstance(data, list):
            return DeleteListingsResponse(raw=data, items=data)
        return DeleteListingsResponse(raw=data)

@dataclass(frozen=True)
class AddExpiryListingsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    listing_action_id: Optional[int] = None

    @staticmethod
    def from_mixed(data: Any) -> "AddExpiryListingsResponse":
        if isinstance(data, dict):
            return AddExpiryListingsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                listing_action_id=(data.get("listingActionId") if isinstance(data.get("listingActionId"), int) and not isinstance(data.get("listingActionId"), bool) else None),
            )
        if isinstance(data, list):
            return AddExpiryListingsResponse(raw=data, items=data)
        return AddExpiryListingsResponse(raw=data)
