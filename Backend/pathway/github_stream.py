"""GitHub event stream connector for Pathway."""

from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class GitHubEvent:
    """Base GitHub event structure."""
    event_type: str
    repository: str
    timestamp: str
    payload: Dict[str, Any]


class GitHubStreamConnector:
    """Custom Pathway connector for GitHub events.
    
    This connector receives events from the FastAPI webhook endpoint
    and feeds them into the Pathway pipeline.
    """
    
    def __init__(self, host: str = "localhost", port: int = 8080):
        self.host = host
        self.port = port
        self._buffer = []
    
    def push_event(self, event: GitHubEvent):
        """Push a new event to the stream."""
        # TODO: Implement proper Pathway connector logic
        self._buffer.append(event)
    
    def get_events(self):
        """Get buffered events (for testing)."""
        events = self._buffer.copy()
        self._buffer.clear()
        return events


# TODO: Implement proper Pathway input connector
# class PathwayGitHubConnector(pw.io.ConnectorSubject):
#     def __init__(self):
#         super().__init__()
#         self._event_queue = asyncio.Queue()
#     
#     async def run(self):
#         while True:
#             event = await self._event_queue.get()
#             self.next(event)
#     
#     def push_event(self, event: dict):
#         self._event_queue.put_nowait(event)
