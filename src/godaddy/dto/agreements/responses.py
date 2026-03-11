from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass(frozen=True)
class GetResponse:
    raw: Any = None
    object: Dict[str, Any] = field(default_factory=dict)
    items: List[Any] = field(default_factory=list)
    code: Optional[str] = None
    message: Optional[str] = None
    array_items: Optional[List[Dict[str, Any]]] = None

    @staticmethod
    def from_mixed(data: Any) -> "GetResponse":
        if isinstance(data, dict):
            return GetResponse(
                raw=data,
                object=data,
                items=data.get("items") if isinstance(data.get("items"), list) else [],
                code=data.get("code") if isinstance(data.get("code"), str) else None,
                message=data.get("message") if isinstance(data.get("message"), str) else None,
            )
        if isinstance(data, list):
            return GetResponse(raw=data, items=data, array_items=data)
        return GetResponse(raw=data)
