from typing import Sequence
from urllib.parse import ParseResult as ParseResult
from wandb.errors.term import termwarn as termwarn
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.artifacts.artifact_manifest_entry import ArtifactManifestEntry as ArtifactManifestEntry
from wandb.sdk.artifacts.storage_handler import StorageHandler as StorageHandler
from wandb.sdk.lib.paths import FilePathStr as FilePathStr, StrPath as StrPath, URIStr as URIStr

class TrackingHandler(StorageHandler):
    def __init__(self, scheme: str | None = None) -> None:
        """Track paths with no modification or special processing.

        Useful when paths being tracked are on file systems mounted at a standardized
        location.

        For example, if the data to track is located on an NFS share mounted on
        `/data`, then it is sufficient to just track the paths.
        """
    def can_handle(self, parsed_url: ParseResult) -> bool: ...
    def load_path(self, manifest_entry: ArtifactManifestEntry, local: bool = False) -> URIStr | FilePathStr: ...
    def store_path(self, artifact: Artifact, path: URIStr | FilePathStr, name: StrPath | None = None, checksum: bool = True, max_objects: int | None = None) -> Sequence[ArtifactManifestEntry]: ...
