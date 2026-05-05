from typing import Awaitable, Dict, Protocol, Sequence
from wandb import util as util
from wandb.sdk.artifacts.artifact_manifest import ArtifactManifest as ArtifactManifest
from wandb.sdk.artifacts.artifact_manifest_entry import ArtifactManifestEntry as ArtifactManifestEntry
from wandb.sdk.artifacts.staging import get_staging_dir as get_staging_dir
from wandb.sdk.internal.file_pusher import FilePusher as FilePusher
from wandb.sdk.internal.internal_api import Api as InternalApi
from wandb.sdk.internal.progress import ProgressFn as ProgressFn
from wandb.sdk.lib.hashutil import B64MD5 as B64MD5, b64_to_hex_id as b64_to_hex_id, md5_file_b64 as md5_file_b64
from wandb.sdk.lib.paths import URIStr as URIStr

class SaveFn(Protocol):
    def __call__(self, entry: ArtifactManifestEntry, progress_callback: ProgressFn) -> bool: ...

class SaveFnAsync(Protocol):
    def __call__(self, entry: ArtifactManifestEntry, progress_callback: ProgressFn) -> Awaitable[bool]: ...

class ArtifactSaver:
    def __init__(self, api: InternalApi, digest: str, manifest_json: Dict, file_pusher: FilePusher, is_user_created: bool = False) -> None: ...
    def save(self, type: str, name: str, client_id: str, sequence_client_id: str, distributed_id: str | None = None, finalize: bool = True, metadata: Dict | None = None, ttl_duration_seconds: int | None = None, description: str | None = None, aliases: Sequence[str] | None = None, use_after_commit: bool = False, incremental: bool = False, history_step: int | None = None, base_id: str | None = None) -> Dict | None: ...
