import json
import urllib.request
import urllib.error
from datetime import datetime
from typing import Optional, Any, Dict


class Client:
    def __init__(self, url: str = "http://localhost:8000/"):
        self.url = url

    def _payload(self, topic: str, key: str, value: Any) -> Dict[str, Any]:
        return {
            "topic": topic,
            "key": key,
            "value": value,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        }

    def post(self, topic: str, key: str, value: Any, dry_run: bool = False) -> Optional[int]:
        """Prepare and send the JSON payload.

        If `dry_run` is True, returns the prepared payload dict instead of sending.
        Otherwise returns the HTTP status code (int) on success or HTTPError code on HTTP errors.
        Raises urllib.error.URLError on transport errors.
        """
        payload = self._payload(topic, key, value)
        if dry_run:
            return payload  # type: ignore[return-value]

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            self.url,
            data=data,
            headers={"content-type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(req) as resp:
                return resp.getcode()
        except urllib.error.HTTPError as e:
            return e.code
