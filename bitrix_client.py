import os
import requests
from typing import List, Dict, Any

class BitrixClient:
    """Simple wrapper for Bitrix24 REST webhook calls."""

    def __init__(self, webhook_url: str | None = None) -> None:
        self.webhook_base = webhook_url or os.getenv('WEBHOOK_URL')
        if not self.webhook_base:
            raise RuntimeError('WEBHOOK_URL not provided')
        self.webhook_base = self.webhook_base.rstrip('/')

    def call(self, method: str, payload: List[Any] | Dict[str, Any]) -> dict:
        """Call a REST method and return the response JSON."""
        url = f"{self.webhook_base}/{method}.json"
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()
