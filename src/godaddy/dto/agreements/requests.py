from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class GetRequest:
    x_private_label_id: Optional[int] = None
    x_market_id: Optional[str] = None
    keys: Optional[List[str]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("keys", self.keys),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Private-Label-Id", self.x_private_label_id),
            ("X-Market-Id", self.x_market_id),
        ]

    def to_body(self) -> Any:
        return None
