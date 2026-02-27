from dataclasses import dataclass, field
from typing import Dict, Optional

@dataclass(frozen=True)
class Config:
    api_key: Optional[str] = None
    api_secret: Optional[str] = None
    base_url: Optional[str] = None
    timeout: float = 30.0
    max_retries: int = 2
    retry_delay: float = 0.2
    default_headers: Dict[str, str] = field(default_factory=dict)
    user_agent: str = "community-sdks/godaddy-python"
