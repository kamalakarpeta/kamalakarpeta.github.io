from typing import ContextManager, IO, Protocol, Tuple
from wandb import env as env, util as util
from wandb.errors import term as term
from wandb.sdk.lib.filesystem import files_in as files_in
from wandb.sdk.lib.hashutil import B64MD5 as B64MD5, ETag as ETag, b64_to_hex_id as b64_to_hex_id
from wandb.sdk.lib.paths import FilePathStr as FilePathStr, StrPath as StrPath, URIStr as URIStr

class Opener(Protocol):
    def __call__(self, mode: str = ...) -> ContextManager[IO]: ...

class ArtifactsCache:
    def __init__(self, cache_dir: StrPath) -> None: ...
    def check_md5_obj_path(self, b64_md5: B64MD5, size: int) -> Tuple[FilePathStr, bool, 'Opener']: ...
    def check_etag_obj_path(self, url: URIStr, etag: ETag, size: int) -> Tuple[FilePathStr, bool, 'Opener']: ...
    def cleanup(self, target_size: int | None = None, remove_temp: bool = False, target_fraction: float | None = None) -> int:
        """Clean up the cache, removing the least recently used files first.

        Args:
            target_size: The target size of the cache in bytes. If the cache is larger
                than this, we will remove the least recently used files until the cache
                is smaller than this size.
            remove_temp: Whether to remove temporary files. Temporary files are files
                that are currently being written to the cache. If remove_temp is True,
                all temp files will be removed, regardless of the target_size or
                target_fraction.
            target_fraction: The target fraction of the cache to reclaim. If the cache
                is larger than this, we will remove the least recently used files until
                the cache is smaller than this fraction of its current size. It is an
                error to specify both target_size and target_fraction.

        Returns:
            The number of bytes reclaimed.
        """

def get_artifacts_cache() -> ArtifactsCache: ...
