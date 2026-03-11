from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class GetMetricsRequest:
    customer_id: Optional[str] = None
    period_start_ptz: Optional[str] = None
    period_end_ptz: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    x_request_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("periodStartPtz", self.period_start_ptz),
            ("periodEndPtz", self.period_end_ptz),
            ("limit", self.limit),
            ("offset", self.offset),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetMetricsByDomainRequest:
    customer_id: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    domains: Optional[str] = None
    domain_like: Optional[str] = None
    portfolio_id: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    x_request_id: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("customerId", self.customer_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("startDate", self.start_date),
            ("endDate", self.end_date),
            ("domains", self.domains),
            ("domainLike", self.domain_like),
            ("portfolioId", self.portfolio_id),
            ("limit", self.limit),
            ("offset", self.offset),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return [
            ("X-Request-Id", self.x_request_id),
        ]

    def to_body(self) -> Any:
        return None
