from _typeshed import Incomplete
from wandb import errors as errors
from wandb.sdk.artifacts.artifact import Artifact as Artifact

class ArtifactStatusError(AttributeError):
    """Raised when an artifact is in an invalid state for the requested operation."""
    obj: Incomplete
    name: Incomplete
    def __init__(self, artifact: Artifact | None = None, attr: str | None = None, msg: str = 'Artifact is in an invalid state for the requested operation.') -> None: ...

class ArtifactNotLoggedError(ArtifactStatusError):
    """Raised for Artifact methods or attributes only available after logging."""
    def __init__(self, artifact: Artifact | None = None, attr: str | None = None) -> None: ...

class ArtifactFinalizedError(ArtifactStatusError):
    """Raised for Artifact methods or attributes that can't be changed after logging."""
    def __init__(self, artifact: Artifact | None = None, attr: str | None = None) -> None: ...

class WaitTimeoutError(errors.Error):
    """Raised when wait() timeout occurs before process is finished."""
