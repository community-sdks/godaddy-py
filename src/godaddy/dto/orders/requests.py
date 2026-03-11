from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class ListRequest:
    period_start: Optional[str] = None
    period_end: Optional[str] = None
    domain: Optional[str] = None
    product_group_id: Optional[int] = None
    payment_profile_id: Optional[int] = None
    parent_order_id: Optional[str] = None
    offset: Optional[int] = None
    limit: Optional[int] = None
    sort: Optional[str] = None
    x_shopper_id: Optional[str] = None
    x_app_key: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("periodStart", self.period_start),
            ("periodEnd", self.period_end),
            ("domain", self.domain),
            ("productGroupId", self.product_group_id),
            ("paymentProfileId", self.payment_profile_id),
            ("parentOrderId", self.parent_order_id),
            ("offset", self.offset),
            ("limit", self.limit),
            ("sort", self.sort),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
            ("X-App-Key", self.x_app_key),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetRequest:
    order_id: Optional[str] = None
    x_shopper_id: Optional[str] = None
    x_market_id: Optional[str] = None
    x_app_key: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("orderId", self.order_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Shopper-Id", self.x_shopper_id),
            ("X-Market-Id", self.x_market_id),
            ("X-App-Key", self.x_app_key),
        ]

    def to_body(self) -> Any:
        return None
