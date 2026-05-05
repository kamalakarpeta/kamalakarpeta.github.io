from typing import Dict, Mapping
from wandb.sdk.artifacts.artifact_manifest import ArtifactManifest as ArtifactManifest
from wandb.sdk.artifacts.artifact_manifest_entry import ArtifactManifestEntry as ArtifactManifestEntry
from wandb.sdk.artifacts.storage_policy import StoragePolicy as StoragePolicy
from wandb.sdk.lib.hashutil import HexMD5 as HexMD5

class ArtifactManifestV1(ArtifactManifest):
    @classmethod
    def version(cls) -> int: ...
    @classmethod
    def from_manifest_json(cls, manifest_json: Dict) -> ArtifactManifestV1: ...
    def __init__(self, storage_policy: StoragePolicy, entries: Mapping[str, ArtifactManifestEntry] | None = None) -> None: ...
    def to_manifest_json(self) -> Dict:
        """This is the JSON that's stored in wandb_manifest.json.

        If include_local is True we also include the local paths to files. This is
        used to represent an artifact that's waiting to be saved on the current
        system. We don't need to include the local paths in the artifact manifest
        contents.
        """
    def digest(self) -> HexMD5: ...
