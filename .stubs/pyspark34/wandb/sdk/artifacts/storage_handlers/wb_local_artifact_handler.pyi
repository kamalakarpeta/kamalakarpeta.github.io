from typing import Sequence
from urllib.parse import ParseResult as ParseResult
from wandb import util as util
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.artifacts.artifact_cache import artifact_cache as artifact_cache
from wandb.sdk.artifacts.artifact_manifest_entry import ArtifactManifestEntry as ArtifactManifestEntry
from wandb.sdk.artifacts.storage_handler import StorageHandler as StorageHandler
from wandb.sdk.lib.paths import FilePathStr as FilePathStr, StrPath as StrPath, URIStr as URIStr

class WBLocalArtifactHandler(StorageHandler):
    """Handles loading and storing Artifact reference-type files."""
    def __init__(self) -> None: ...
    def can_handle(self, parsed_url: ParseResult) -> bool: ...
    def load_path(self, manifest_entry: ArtifactManifestEntry, local: bool = False) -> URIStr | FilePathStr: ...
    def store_path(self, artifact: Artifact, path: URIStr | FilePathStr, name: StrPath | None = None, checksum: bool = True, max_objects: int | None = None) -> Sequence[ArtifactManifestEntry]:
        """Store the file or directory at the given path within the specified artifact.

        Arguments:
            artifact: The artifact doing the storing
            path (str): The path to store
            name (str): If specified, the logical name that should map to `path`

        Returns:
            (list[ArtifactManifestEntry]): A list of manifest entries to store within the artifact
        """
