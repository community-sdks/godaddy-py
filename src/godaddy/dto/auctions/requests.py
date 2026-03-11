from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class PlaceBidsRequest:
    customer_id: Optional[str] = None
    request_body: Optional[List[Any]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.request_body
