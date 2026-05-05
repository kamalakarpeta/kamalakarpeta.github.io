from typing import Sequence
from urllib.parse import ParseResult as ParseResult
from wandb import util as util
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.artifacts.artifact_manifest_entry import ArtifactManifestEntry as ArtifactManifestEntry
from wandb.sdk.artifacts.artifacts_cache import get_artifacts_cache as get_artifacts_cache
from wandb.sdk.artifacts.storage_handler import DEFAULT_MAX_OBJECTS as DEFAULT_MAX_OBJECTS, StorageHandler as StorageHandler
from wandb.sdk.lib.hashutil import ETag as ETag
from wandb.sdk.lib.paths import FilePathStr as FilePathStr, LogicalPath as LogicalPath, StrPath as StrPath, URIStr as URIStr

class AzureHandler(StorageHandler):
    def can_handle(self, parsed_url: ParseResult) -> bool: ...
    def load_path(self, manifest_entry: ArtifactManifestEntry, local: bool = False) -> URIStr | FilePathStr: ...
    def store_path(self, artifact: Artifact, path: URIStr | FilePathStr, name: StrPath | None = None, checksum: bool = True, max_objects: int | None = None) -> Sequence['ArtifactManifestEntry']: ...
