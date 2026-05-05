from typing import List, Sequence
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.artifacts.artifact_manifest_entry import ArtifactManifestEntry as ArtifactManifestEntry
from wandb.sdk.artifacts.storage_handler import StorageHandler as StorageHandler
from wandb.sdk.lib.paths import FilePathStr as FilePathStr, URIStr as URIStr

class MultiHandler(StorageHandler):
    def __init__(self, handlers: List[StorageHandler] | None = None, default_handler: StorageHandler | None = None) -> None: ...
    def load_path(self, manifest_entry: ArtifactManifestEntry, local: bool = False) -> URIStr | FilePathStr: ...
    def store_path(self, artifact: Artifact, path: URIStr | FilePathStr, name: str | None = None, checksum: bool = True, max_objects: int | None = None) -> Sequence['ArtifactManifestEntry']: ...
