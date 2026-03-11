from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass(frozen=True)
class Config:
    SANDBOX_BASE_URL = "https://api.ote-godaddy.com"
    PRODUCTION_BASE_URL = "https://api.godaddy.com"

    api_key: Optional[str] = None
    api_secret: Optional[str] = None
    base_url: str = SANDBOX_BASE_URL
    service_base_urls: Dict[str, str] = field(default_factory=dict)
    timeout: float = 30.0
    max_retries: int = 2
    retry_delay: float = 0.2
    default_headers: Dict[str, str] = field(default_factory=dict)
    user_agent: str = "community-sdks/godaddy-python"

    @classmethod
    def sandbox(cls, api_key: Optional[str] = None, api_secret: Optional[str] = None, **kwargs):
        return cls(api_key=api_key, api_secret=api_secret, base_url=cls.SANDBOX_BASE_URL, **kwargs)

    @classmethod
    def production(cls, api_key: Optional[str] = None, api_secret: Optional[str] = None, **kwargs):
        return cls(api_key=api_key, api_secret=api_secret, base_url=cls.PRODUCTION_BASE_URL, **kwargs)
