from typing import Dict
from wandb.errors.term import termwarn as termwarn
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.lib import filesystem as filesystem
from wandb.sdk.lib.hashutil import B64MD5 as B64MD5, ETag as ETag, b64_to_hex_id as b64_to_hex_id, hex_to_b64_id as hex_to_b64_id, md5_file_b64 as md5_file_b64
from wandb.sdk.lib.paths import FilePathStr as FilePathStr, LogicalPath as LogicalPath, StrPath as StrPath, URIStr as URIStr

class ArtifactManifestEntry:
    """A single entry in an artifact manifest."""
    path: LogicalPath
    digest: B64MD5 | URIStr | FilePathStr | ETag
    ref: FilePathStr | URIStr | None
    birth_artifact_id: str | None
    size: int | None
    extra: Dict
    local_path: str | None
    def __init__(self, path: StrPath, digest: B64MD5 | URIStr | FilePathStr | ETag, ref: FilePathStr | URIStr | None = None, birth_artifact_id: str | None = None, size: int | None = None, extra: Dict | None = None, local_path: StrPath | None = None) -> None: ...
    def __eq__(self, other: object) -> bool:
        """Strict equality, comparing all public fields.

        ArtifactManifestEntries for the same file may not compare equal if they were
        added in different ways or created for different parent artifacts.
        """
    @property
    def name(self) -> LogicalPath: ...
    def parent_artifact(self) -> Artifact:
        """Get the artifact to which this artifact entry belongs.

        Returns:
            (PublicArtifact): The parent artifact
        """
    def download(self, root: str | None = None) -> FilePathStr:
        """Download this artifact entry to the specified root path.

        Arguments:
            root: (str, optional) The root path in which to download this
                artifact entry. Defaults to the artifact's root.

        Returns:
            (str): The path of the downloaded artifact entry.
        """
    def ref_target(self) -> FilePathStr | URIStr:
        """Get the reference URL that is targeted by this artifact entry.

        Returns:
            (str): The reference URL of this artifact entry.

        Raises:
            ValueError: If this artifact entry was not a reference.
        """
    def ref_url(self) -> str:
        """Get a URL to this artifact entry.

        These URLs can be referenced by another artifact.

        Returns:
            (str): A URL representing this artifact entry.

        Examples:
            Basic usage
            ```
            ref_url = source_artifact.get_path('file.txt').ref_url()
            derived_artifact.add_reference(ref_url)
            ```
        """
