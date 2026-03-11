from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class ListRequest:
    x_app_key: Optional[str] = None
    x_shopper_id: Optional[str] = None
    x_market_id: Optional[str] = None
    product_group_keys: Optional[List[str]] = None
    includes: Optional[List[str]] = None
    offset: Optional[int] = None
    limit: Optional[int] = None
    sort: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("productGroupKeys", self.product_group_keys),
            ("includes", self.includes),
            ("offset", self.offset),
            ("limit", self.limit),
            ("sort", self.sort),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-App-Key", self.x_app_key),
            ("X-Shopper-Id", self.x_shopper_id),
            ("X-Market-Id", self.x_market_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class ProductGroupsRequest:
    x_app_key: Optional[str] = None
    x_shopper_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-App-Key", self.x_app_key),
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetRequest:
    x_app_key: Optional[str] = None
    x_shopper_id: Optional[str] = None
    subscription_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("subscriptionId", self.subscription_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-App-Key", self.x_app_key),
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class UpdateRequest:
    x_app_key: Optional[str] = None
    x_shopper_id: Optional[str] = None
    subscription_id: Optional[str] = None
    subscription: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("subscriptionId", self.subscription_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-App-Key", self.x_app_key),
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return self.subscription

@dataclass(frozen=True)
class CancelRequest:
    x_app_key: Optional[str] = None
    x_shopper_id: Optional[str] = None
    subscription_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("subscriptionId", self.subscription_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-App-Key", self.x_app_key),
            ("X-Shopper-Id", self.x_shopper_id),
        ]

    def to_body(self) -> Any:
        return None
