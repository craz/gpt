import os
import requests
from typing import List, Any

class BitrixClient:
main
    def __init__(self, webhook_url: str | None = None) -> None:
        self.webhook_base = webhook_url or os.getenv('WEBHOOK_URL')
        if not self.webhook_base:
            raise RuntimeError('WEBHOOK_URL not provided')
        self.webhook_base = self.webhook_base.rstrip('/')


    def call(self, method: str, payload: List[Any] | Dict[str, Any]) -> dict:
        """Call a REST method and return the response JSON."""

    def call(self, method: str, payload: List[Any]) -> dict:

