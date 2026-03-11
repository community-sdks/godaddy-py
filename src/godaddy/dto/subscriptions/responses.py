from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass(frozen=True)
class ListResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    pagination: Optional[Dict[str, Any]] = None
    subscriptions: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "ListResponse":
        if isinstance(data, dict):
            return ListResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                pagination=(data.get("pagination") if isinstance(data.get("pagination"), dict) else None),
                subscriptions=(data.get("subscriptions") if isinstance(data.get("subscriptions"), list) else None),
            )
        if isinstance(data, list):
            return ListResponse(raw=data, items=data)
        return ListResponse(raw=data)

@dataclass(frozen=True)
class ProductGroupsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "ProductGroupsResponse":
        if isinstance(data, dict):
            return ProductGroupsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return ProductGroupsResponse(raw=data, items=data, array_items=data)
        return ProductGroupsResponse(raw=data)

@dataclass(frozen=True)
class GetResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    addons: Optional[List[Dict[str, Any]]] = None
    billing: Optional[Dict[str, Any]] = None
    cancelable: Optional[bool] = None
    created_at: Optional[str] = None
    expires_at: Optional[str] = None
    label: Optional[str] = None
    launch_url: Optional[str] = None
    payment_profile_id: Optional[int] = None
    price_locked: Optional[bool] = None
    product: Optional[Dict[str, Any]] = None
    relations: Optional[Dict[str, Any]] = None
    renew_auto: Optional[bool] = None
    renewable: Optional[bool] = None
    status: Optional[str] = None
    subscription_id: Optional[str] = None
    upgradeable: Optional[bool] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetResponse":
        if isinstance(data, dict):
            return GetResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                addons=(data.get("addons") if isinstance(data.get("addons"), list) else None),
                billing=(data.get("billing") if isinstance(data.get("billing"), dict) else None),
                cancelable=(data.get("cancelable") if isinstance(data.get("cancelable"), bool) else None),
                created_at=(data.get("createdAt") if isinstance(data.get("createdAt"), str) else None),
                expires_at=(data.get("expiresAt") if isinstance(data.get("expiresAt"), str) else None),
                label=(data.get("label") if isinstance(data.get("label"), str) else None),
                launch_url=(data.get("launchUrl") if isinstance(data.get("launchUrl"), str) else None),
                payment_profile_id=(data.get("paymentProfileId") if isinstance(data.get("paymentProfileId"), int) and not isinstance(data.get("paymentProfileId"), bool) else None),
                price_locked=(data.get("priceLocked") if isinstance(data.get("priceLocked"), bool) else None),
                product=(data.get("product") if isinstance(data.get("product"), dict) else None),
                relations=(data.get("relations") if isinstance(data.get("relations"), dict) else None),
                renew_auto=(data.get("renewAuto") if isinstance(data.get("renewAuto"), bool) else None),
                renewable=(data.get("renewable") if isinstance(data.get("renewable"), bool) else None),
                status=(data.get("status") if isinstance(data.get("status"), str) else None),
                subscription_id=(data.get("subscriptionId") if isinstance(data.get("subscriptionId"), str) else None),
                upgradeable=(data.get("upgradeable") if isinstance(data.get("upgradeable"), bool) else None),
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
