"""Infrastructure layer for taskdog-ui.

This module provides the API client facade and specialized clients
for communicating with the Taskdog server.
"""

from taskdog.infrastructure.api.analytics_client import AnalyticsClient
from taskdog.infrastructure.api.base_client import BaseApiClient
from taskdog.infrastructure.api.lifecycle_client import LifecycleClient
from taskdog.infrastructure.api.notes_client import NotesClient
from taskdog.infrastructure.api.query_client import QueryClient
from taskdog.infrastructure.api.relationship_client import RelationshipClient
from taskdog.infrastructure.api.task_client import TaskClient
from taskdog.infrastructure.api_client import TaskdogApiClient

__all__ = [
    "AnalyticsClient",
    "BaseApiClient",
    "LifecycleClient",
    "NotesClient",
    "QueryClient",
    "RelationshipClient",
    "TaskClient",
    "TaskdogApiClient",
]
