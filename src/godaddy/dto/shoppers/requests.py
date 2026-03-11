from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class CreateSubaccountRequest:
    subaccount: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.subaccount

@dataclass(frozen=True)
class GetRequest:
    shopper_id: Optional[str] = None
    includes: Optional[List[str]] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("shopperId", self.shopper_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("includes", self.includes),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class UpdateRequest:
    shopper_id: Optional[str] = None
    shopper: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("shopperId", self.shopper_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.shopper

@dataclass(frozen=True)
class DeleteRequest:
    shopper_id: Optional[str] = None
    audit_client_ip: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("shopperId", self.shopper_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("auditClientIp", self.audit_client_ip),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class GetStatusRequest:
    shopper_id: Optional[str] = None
    audit_client_ip: Optional[str] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("shopperId", self.shopper_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return [
            ("auditClientIp", self.audit_client_ip),
        ]

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return None

@dataclass(frozen=True)
class ChangePasswordRequest:
    shopper_id: Optional[str] = None
    secret: Optional[Any] = None

    def to_path_params(self) -> List[Tuple[str, Any]]:
        return [
            ("shopperId", self.shopper_id),
        ]

    def to_query_params(self) -> List[Tuple[str, Any]]:
        return []

    def to_headers(self) -> List[Tuple[str, Any]]:
        return []

    def to_body(self) -> Any:
        return self.secret
