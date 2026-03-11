from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class GetCountriesRequest:
    market_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("marketId", self.market_id),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetCountryRequest:
    country_key: Optional[str] = None
    market_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("countryKey", self.country_key),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("marketId", self.market_id),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None
