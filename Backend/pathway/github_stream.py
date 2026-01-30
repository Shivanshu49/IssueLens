from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class GitHubEvent:
    event_type: str
    repository: str
    timestamp: str
    payload: Dict[str, Any]


class GitHubStreamConnector:
    def __init__(self, host: str = "localhost", port: int = 8080):
        self.host = host
        self.port = port
        self._buffer = []
    
    def push_event(self, event: GitHubEvent):
        self._buffer.append(event)
    
    def get_events(self):
        events = self._buffer.copy()
        self._buffer.clear()
        return events
