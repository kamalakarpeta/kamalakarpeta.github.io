from _typeshed import Incomplete
from typing import Any, Dict, List, Sequence
from wandb.apis import InternalApi as InternalApi
from wandb.errors.term import termwarn as termwarn
from wandb.filesync.step_prepare import StepPrepare as StepPrepare
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.artifacts.artifact_manifest_entry import ArtifactManifestEntry as ArtifactManifestEntry
from wandb.sdk.artifacts.artifacts_cache import ArtifactsCache as ArtifactsCache, get_artifacts_cache as get_artifacts_cache
from wandb.sdk.artifacts.storage_handlers.azure_handler import AzureHandler as AzureHandler
from wandb.sdk.artifacts.storage_handlers.gcs_handler import GCSHandler as GCSHandler
from wandb.sdk.artifacts.storage_handlers.http_handler import HTTPHandler as HTTPHandler
from wandb.sdk.artifacts.storage_handlers.local_file_handler import LocalFileHandler as LocalFileHandler
from wandb.sdk.artifacts.storage_handlers.multi_handler import MultiHandler as MultiHandler
from wandb.sdk.artifacts.storage_handlers.s3_handler import S3Handler as S3Handler
from wandb.sdk.artifacts.storage_handlers.tracking_handler import TrackingHandler as TrackingHandler
from wandb.sdk.artifacts.storage_handlers.wb_artifact_handler import WBArtifactHandler as WBArtifactHandler
from wandb.sdk.artifacts.storage_handlers.wb_local_artifact_handler import WBLocalArtifactHandler as WBLocalArtifactHandler
from wandb.sdk.artifacts.storage_layout import StorageLayout as StorageLayout
from wandb.sdk.artifacts.storage_policies.register import WANDB_STORAGE_POLICY as WANDB_STORAGE_POLICY
from wandb.sdk.artifacts.storage_policy import StoragePolicy as StoragePolicy
from wandb.sdk.internal import progress as progress
from wandb.sdk.lib.hashutil import B64MD5 as B64MD5, b64_to_hex_id as b64_to_hex_id, hex_to_b64_id as hex_to_b64_id
from wandb.sdk.lib.paths import FilePathStr as FilePathStr, URIStr as URIStr

S3_MAX_PART_NUMBERS: int
S3_MIN_MULTI_UPLOAD_SIZE: Incomplete
S3_MAX_MULTI_UPLOAD_SIZE: Incomplete

class WandbStoragePolicy(StoragePolicy):
    @classmethod
    def name(cls) -> str: ...
    @classmethod
    def from_config(cls, config: Dict) -> WandbStoragePolicy: ...
    def __init__(self, config: Dict | None = None, cache: ArtifactsCache | None = None, api: InternalApi | None = None) -> None: ...
    def config(self) -> Dict: ...
    def load_file(self, artifact: Artifact, manifest_entry: ArtifactManifestEntry) -> FilePathStr: ...
    def store_reference(self, artifact: Artifact, path: URIStr | FilePathStr, name: str | None = None, checksum: bool = True, max_objects: int | None = None) -> Sequence['ArtifactManifestEntry']: ...
    def load_reference(self, manifest_entry: ArtifactManifestEntry, local: bool = False) -> FilePathStr | URIStr: ...
    def s3_multipart_file_upload(self, file_path: str, chunk_size: int, hex_digests: Dict[int, str], multipart_urls: Dict[int, str], extra_headers: Dict[str, str]) -> List[Dict[str, Any]]: ...
    def default_file_upload(self, upload_url: str, file_path: str, extra_headers: Dict[str, Any], progress_callback: progress.ProgressFn | None = None) -> None:
        """Upload a file to the artifact store and write to cache."""
    def calc_chunk_size(self, file_size: int) -> int: ...
    def store_file_sync(self, artifact_id: str, artifact_manifest_id: str, entry: ArtifactManifestEntry, preparer: StepPrepare, progress_callback: progress.ProgressFn | None = None) -> bool:
        """Upload a file to the artifact store.

        Returns:
            True if the file was a duplicate (did not need to be uploaded),
            False if it needed to be uploaded or was a reference (nothing to dedupe).
        """
    async def store_file_async(self, artifact_id: str, artifact_manifest_id: str, entry: ArtifactManifestEntry, preparer: StepPrepare, progress_callback: progress.ProgressFn | None = None) -> bool:
        """Async equivalent to `store_file_sync`."""
