from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class GetListingsRequest:
    customer_id: Optional[str] = None
    domains: Optional[str] = None
    listing_status: Optional[str] = None
    transfer_before: Optional[str] = None
    transfer_after: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domains", self.domains),
            ("listingStatus", self.listing_status),
            ("transferBefore", self.transfer_before),
            ("transferAfter", self.transfer_after),
            ("limit", self.limit),
            ("offset", self.offset),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class DeleteListingsRequest:
    domains: Optional[List[str]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("domains", self.domains),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class AddExpiryListingsRequest:
    expiry_listings: Optional[List[Any]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.expiry_listings
