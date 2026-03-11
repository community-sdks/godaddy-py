from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass(frozen=True)
class GetMetricsResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    currency_id: Optional[str] = None
    metrics: Optional[List[Dict[str, Any]]] = None
    pagination: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetMetricsResponse":
        if isinstance(data, dict):
            return GetMetricsResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                currency_id=(data.get("currencyId") if isinstance(data.get("currencyId"), str) else None),
                metrics=(data.get("metrics") if isinstance(data.get("metrics"), list) else None),
                pagination=(data.get("pagination") if isinstance(data.get("pagination"), dict) else None),
            )
        if isinstance(data, list):
            return GetMetricsResponse(raw=data, items=data)
        return GetMetricsResponse(raw=data)

@dataclass(frozen=True)
class GetMetricsByDomainResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    currency_id: Optional[str] = None
    metrics: Optional[List[Dict[str, Any]]] = None
    pagination: Optional[Dict[str, Any]] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetMetricsByDomainResponse":
        if isinstance(data, dict):
            return GetMetricsByDomainResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
                currency_id=(data.get("currencyId") if isinstance(data.get("currencyId"), str) else None),
                metrics=(data.get("metrics") if isinstance(data.get("metrics"), list) else None),
                pagination=(data.get("pagination") if isinstance(data.get("pagination"), dict) else None),
                start_date=(data.get("startDate") if isinstance(data.get("startDate"), str) else None),
                end_date=(data.get("endDate") if isinstance(data.get("endDate"), str) else None),
            )
        if isinstance(data, list):
            return GetMetricsByDomainResponse(raw=data, items=data)
        return GetMetricsByDomainResponse(raw=data)
