from typing import Sequence
from urllib.parse import ParseResult as ParseResult
from wandb import util as util
from wandb.apis import PublicApi as PublicApi
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.artifacts.artifact_manifest_entry import ArtifactManifestEntry as ArtifactManifestEntry
from wandb.sdk.artifacts.artifacts_cache import get_artifacts_cache as get_artifacts_cache
from wandb.sdk.artifacts.storage_handler import StorageHandler as StorageHandler
from wandb.sdk.lib.hashutil import B64MD5 as B64MD5, b64_to_hex_id as b64_to_hex_id, hex_to_b64_id as hex_to_b64_id
from wandb.sdk.lib.paths import FilePathStr as FilePathStr, StrPath as StrPath, URIStr as URIStr

class WBArtifactHandler(StorageHandler):
    """Handles loading and storing Artifact reference-type files."""
    def __init__(self) -> None: ...
    def can_handle(self, parsed_url: ParseResult) -> bool: ...
    @property
    def client(self) -> PublicApi: ...
    def load_path(self, manifest_entry: ArtifactManifestEntry, local: bool = False) -> URIStr | FilePathStr:
        """Load the file in the specified artifact given its corresponding entry.

        Download the referenced artifact; create and return a new symlink to the caller.

        Arguments:
            manifest_entry (ArtifactManifestEntry): The index entry to load

        Returns:
            (os.PathLike): A path to the file represented by `index_entry`
        """
    def store_path(self, artifact: Artifact, path: URIStr | FilePathStr, name: StrPath | None = None, checksum: bool = True, max_objects: int | None = None) -> Sequence[ArtifactManifestEntry]:
        """Store the file or directory at the given path into the specified artifact.

        Recursively resolves the reference until the result is a concrete asset.

        Arguments:
            artifact: The artifact doing the storing path (str): The path to store name
            (str): If specified, the logical name that should map to `path`

        Returns:
            (list[ArtifactManifestEntry]): A list of manifest entries to store within
            the artifact
        """
