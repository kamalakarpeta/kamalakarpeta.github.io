from enum import Enum

class ArtifactState(Enum):
    PENDING: str
    COMMITTED: str
    DELETED: str
    GARBAGE_COLLECTED: str
    PENDING_DELETION: str
