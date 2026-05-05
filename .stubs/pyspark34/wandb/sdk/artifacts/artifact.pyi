import wandb
from _typeshed import Incomplete
from datetime import timedelta
from typing import Any, Dict, Generator, IO, List, Sequence
from wandb import data_types as data_types, env as env, util as util
from wandb.apis.normalize import normalize_exceptions as normalize_exceptions
from wandb.apis.public import ArtifactCollection as ArtifactCollection, ArtifactFiles as ArtifactFiles, RetryingClient as RetryingClient, Run as Run
from wandb.data_types import WBValue as WBValue
from wandb.errors.term import termerror as termerror, termlog as termlog, termwarn as termwarn
from wandb.sdk.artifacts.artifact_cache import artifact_cache as artifact_cache
from wandb.sdk.artifacts.artifact_download_logger import ArtifactDownloadLogger as ArtifactDownloadLogger
from wandb.sdk.artifacts.artifact_manifest import ArtifactManifest as ArtifactManifest
from wandb.sdk.artifacts.artifact_manifest_entry import ArtifactManifestEntry as ArtifactManifestEntry
from wandb.sdk.artifacts.artifact_manifests.artifact_manifest_v1 import ArtifactManifestV1 as ArtifactManifestV1
from wandb.sdk.artifacts.artifact_state import ArtifactState as ArtifactState
from wandb.sdk.artifacts.artifact_ttl import ArtifactTTL as ArtifactTTL
from wandb.sdk.artifacts.exceptions import ArtifactFinalizedError as ArtifactFinalizedError, ArtifactNotLoggedError as ArtifactNotLoggedError, WaitTimeoutError as WaitTimeoutError
from wandb.sdk.artifacts.staging import get_staging_dir as get_staging_dir
from wandb.sdk.artifacts.storage_layout import StorageLayout as StorageLayout
from wandb.sdk.artifacts.storage_policies import WANDB_STORAGE_POLICY as WANDB_STORAGE_POLICY
from wandb.sdk.artifacts.storage_policy import StoragePolicy as StoragePolicy
from wandb.sdk.data_types._dtypes import Type as WBType, TypeRegistry as TypeRegistry
from wandb.sdk.interface.message_future import MessageFuture as MessageFuture
from wandb.sdk.lib import filesystem as filesystem, retry as retry, runid as runid, telemetry as telemetry
from wandb.sdk.lib.hashutil import B64MD5 as B64MD5, b64_to_hex_id as b64_to_hex_id, md5_file_b64 as md5_file_b64
from wandb.sdk.lib.paths import FilePathStr as FilePathStr, LogicalPath as LogicalPath, StrPath as StrPath, URIStr as URIStr

reset_path: Incomplete

class Artifact:
    '''Flexible and lightweight building block for dataset and model versioning.

    Constructs an empty artifact whose contents can be populated using its `add` family
    of functions. Once the artifact has all the desired files, you can call
    `wandb.log_artifact()` to log it.

    Arguments:
        name: A human-readable name for this artifact, which is how you can identify
            this artifact in the UI or reference it in `use_artifact` calls. Names can
            contain letters, numbers, underscores, hyphens, and dots. The name must be
            unique across a project.
        type: The type of the artifact, which is used to organize and differentiate
            artifacts. Common types include `dataset` or `model`, but you can use any
            string containing letters, numbers, underscores, hyphens, and dots.
        description: Free text that offers a description of the artifact. The
            description is markdown rendered in the UI, so this is a good place to place
            tables, links, etc.
        metadata: Structured data associated with the artifact, for example class
            distribution of a dataset. This will eventually be queryable and plottable
            in the UI. There is a hard limit of 100 total keys.

    Returns:
        An `Artifact` object.

    Examples:
        Basic usage:
        ```python
        wandb.init()

        artifact = wandb.Artifact("mnist", type="dataset")
        artifact.add_dir("mnist/")
        wandb.log_artifact(artifact)
        ```
    '''
    def __init__(self, name: str, type: str, description: str | None = None, metadata: Dict[str, Any] | None = None, incremental: bool = False, use_as: str | None = None) -> None: ...
    def new_draft(self) -> Artifact:
        """Create a new draft artifact with the same content as this committed artifact.

        The artifact returned can be extended or modified and logged as a new version.

        Raises:
            ArtifactNotLoggedError: if the artifact has not been logged
        """
    @property
    def id(self) -> str | None:
        """The artifact's ID."""
    @property
    def entity(self) -> str:
        """The name of the entity of the secondary (portfolio) artifact collection."""
    @property
    def project(self) -> str:
        """The name of the project of the secondary (portfolio) artifact collection."""
    @property
    def name(self) -> str:
        """The artifact name and version in its secondary (portfolio) collection.

        A string with the format {collection}:{alias}. Before the artifact is saved,
        contains only the name since the version is not yet known.
        """
    @property
    def qualified_name(self) -> str:
        """The entity/project/name of the secondary (portfolio) collection."""
    @property
    def version(self) -> str:
        """The artifact's version in its secondary (portfolio) collection."""
    @property
    def collection(self) -> ArtifactCollection:
        """The collection this artifact was retrieved from.

        If this artifact was retrieved from a portfolio / linked collection, that
        collection will be returned rather than the source sequence.
        """
    @property
    def source_entity(self) -> str:
        """The name of the entity of the primary (sequence) artifact collection."""
    @property
    def source_project(self) -> str:
        """The name of the project of the primary (sequence) artifact collection."""
    @property
    def source_name(self) -> str:
        """The artifact name and version in its primary (sequence) collection.

        A string with the format {collection}:{alias}. Before the artifact is saved,
        contains only the name since the version is not yet known.
        """
    @property
    def source_qualified_name(self) -> str:
        """The entity/project/name of the primary (sequence) collection."""
    @property
    def source_version(self) -> str:
        '''The artifact\'s version in its primary (sequence) collection.

        A string with the format "v{number}".
        '''
    @property
    def source_collection(self) -> ArtifactCollection:
        """The artifact's primary (sequence) collection."""
    @property
    def type(self) -> str:
        """The artifact's type."""
    @property
    def description(self) -> str | None:
        """The artifact description.

        Free text that offers a user-set description of the artifact.
        """
    @description.setter
    def description(self, description: str | None) -> None:
        """Set the description of the artifact.

        The description is markdown rendered in the UI, so this is a good place to put
        links, etc.

        Arguments:
            desc: Free text that offers a description of the artifact.
        """
    @property
    def metadata(self) -> dict:
        """User-defined artifact metadata.

        Structured data associated with the artifact.
        """
    @metadata.setter
    def metadata(self, metadata: dict) -> None:
        """User-defined artifact metadata.

        Metadata set this way will eventually be queryable and plottable in the UI; e.g.
        the class distribution of a dataset.

        Note: There is currently a limit of 100 total keys.

        Arguments:
            metadata: Structured data associated with the artifact.
        """
    @property
    def ttl(self) -> timedelta | None:
        """Time To Live (TTL).

        The artifact will be deleted shortly after TTL since its creation.
        None means the artifact will never expire.
        If TTL is not set on an artifact, it will inherit the default for its collection.

        Raises:
            ArtifactNotLoggedError: Unable to fetch inherited TTL if the artifact has not been logged or saved
        """
    @ttl.setter
    def ttl(self, ttl: timedelta | ArtifactTTL | None) -> None:
        """Time To Live (TTL).

        The artifact will be deleted shortly after TTL since its creation. None means the artifact will never expire.
        If TTL is not set on an artifact, it will inherit the default TTL rules for its collection.

        Arguments:
            ttl: How long the artifact will remain active from its creation.
                - Timedelta must be positive.
                - `None` means the artifact will never expire.
                - wandb.ArtifactTTL.INHERIT will set the TTL to go back to the default and inherit from collection rules.
        """
    @property
    def aliases(self) -> List[str]:
        """The aliases associated with this artifact.

        The list is mutable and calling `save()` will persist all alias changes.
        """
    @aliases.setter
    def aliases(self, aliases: List[str]) -> None:
        """Set the aliases associated with this artifact."""
    @property
    def distributed_id(self) -> str | None: ...
    @distributed_id.setter
    def distributed_id(self, distributed_id: str | None) -> None: ...
    @property
    def incremental(self) -> bool: ...
    @property
    def use_as(self) -> str | None: ...
    @property
    def state(self) -> str:
        '''The status of the artifact. One of: "PENDING", "COMMITTED", or "DELETED".'''
    @property
    def manifest(self) -> ArtifactManifest:
        """The artifact's manifest.

        The manifest lists all of its contents, and can't be changed once the artifact
        has been logged.
        """
    @property
    def digest(self) -> str:
        """The logical digest of the artifact.

        The digest is the checksum of the artifact's contents. If an artifact has the
        same digest as the current `latest` version, then `log_artifact` is a no-op.
        """
    @property
    def size(self) -> int:
        """The total size of the artifact in bytes.

        Includes any references tracked by this artifact.
        """
    @property
    def commit_hash(self) -> str:
        """The hash returned when this artifact was committed."""
    @property
    def file_count(self) -> int:
        """The number of files (including references)."""
    @property
    def created_at(self) -> str:
        """The time at which the artifact was created."""
    @property
    def updated_at(self) -> str:
        """The time at which the artifact was last updated."""
    def finalize(self) -> None:
        """Mark this artifact as final, disallowing further modifications.

        This happens automatically when calling `log_artifact`.
        """
    def is_draft(self) -> bool:
        """Whether the artifact is a draft, i.e. it hasn't been saved yet."""
    def save(self, project: str | None = None, settings: wandb.wandb_sdk.wandb_settings.Settings | None = None) -> None:
        '''Persist any changes made to the artifact.

        If currently in a run, that run will log this artifact. If not currently in a
        run, a run of type "auto" will be created to track this artifact.

        Arguments:
            project: A project to use for the artifact in the case that a run is not
                already in context
            settings: A settings object to use when initializing an automatic run. Most
                commonly used in testing harness.
        '''
    def wait(self, timeout: int | None = None) -> Artifact:
        """Wait for this artifact to finish logging, if needed.

        Arguments:
            timeout: Wait up to this long.
        """
    def __getitem__(self, name: str) -> data_types.WBValue | None:
        '''Get the WBValue object located at the artifact relative `name`.

        Arguments:
            name: The artifact relative name to get

        Raises:
            ArtifactNotLoggedError: if the artifact isn\'t logged or the run is offline

        Examples:
            Basic usage:
            ```python
            artifact = wandb.Artifact("my_table", type="dataset")
            table = wandb.Table(
                columns=["a", "b", "c"], data=[(i, i * 2, 2**i) for i in range(10)]
            )
            artifact["my_table"] = table

            wandb.log_artifact(artifact)
            ```

            Retrieving an object:
            ```python
            artifact = wandb.use_artifact("my_table:latest")
            table = artifact["my_table"]
            ```
        '''
    def __setitem__(self, name: str, item: data_types.WBValue) -> ArtifactManifestEntry:
        '''Add `item` to the artifact at path `name`.

        Arguments:
            name: The path within the artifact to add the object.
            item: The object to add.

        Returns:
            The added manifest entry

        Raises:
            ArtifactFinalizedError: if the artifact has already been finalized.

        Examples:
            Basic usage:
            ```python
            artifact = wandb.Artifact("my_table", type="dataset")
            table = wandb.Table(
                columns=["a", "b", "c"], data=[(i, i * 2, 2**i) for i in range(10)]
            )
            artifact["my_table"] = table

            wandb.log_artifact(artifact)
            ```

            Retrieving an object:
            ```python
            artifact = wandb.use_artifact("my_table:latest")
            table = artifact["my_table"]
            ```
        '''
    def new_file(self, name: str, mode: str = 'w', encoding: str | None = None) -> Generator[IO, None, None]:
        '''Open a new temporary file that will be automatically added to the artifact.

        Arguments:
            name: The name of the new file being added to the artifact.
            mode: The mode in which to open the new file.
            encoding: The encoding in which to open the new file.

        Returns:
            A new file object that can be written to. Upon closing, the file will be
            automatically added to the artifact.

        Raises:
            ArtifactFinalizedError: if the artifact has already been finalized.

        Examples:
            ```python
            artifact = wandb.Artifact("my_data", type="dataset")
            with artifact.new_file("hello.txt") as f:
                f.write("hello!")
            wandb.log_artifact(artifact)
            ```
        '''
    def add_file(self, local_path: str, name: str | None = None, is_tmp: bool | None = False) -> ArtifactManifestEntry:
        '''Add a local file to the artifact.

        Arguments:
            local_path: The path to the file being added.
            name: The path within the artifact to use for the file being added. Defaults
                to the basename of the file.
            is_tmp: If true, then the file is renamed deterministically to avoid
                collisions.

        Returns:
            The added manifest entry

        Raises:
            ArtifactFinalizedError: if the artifact has already been finalized

        Examples:
            Add a file without an explicit name:
            ```python
            # Add as `file.txt\'
            artifact.add_file("path/to/file.txt")
            ```

            Add a file with an explicit name:
            ```python
            # Add as \'new/path/file.txt\'
            artifact.add_file("path/to/file.txt", name="new/path/file.txt")
            ```
        '''
    def add_dir(self, local_path: str, name: str | None = None) -> None:
        '''Add a local directory to the artifact.

        Arguments:
            local_path: The path to the directory being added.
            name: The path within the artifact to use for the directory being added.
                Defaults to the root of the artifact.

        Raises:
            ArtifactFinalizedError: if the artifact has already been finalized

        Examples:
            Add a directory without an explicit name:
            ```python
            # All files in `my_dir/` are added at the root of the artifact.
            artifact.add_dir("my_dir/")
            ```

            Add a directory and name it explicitly:
            ```python
            # All files in `my_dir/` are added under `destination/`.
            artifact.add_dir("my_dir/", name="destination")
            ```
        '''
    def add_reference(self, uri: ArtifactManifestEntry | str, name: StrPath | None = None, checksum: bool = True, max_objects: int | None = None) -> Sequence[ArtifactManifestEntry]:
        '''Add a reference denoted by a URI to the artifact.

        Unlike adding files or directories, references are NOT uploaded to W&B. However,
        artifact methods such as `download()` can be used regardless of whether the
        artifact contains references or uploaded files.

        By default, W&B offers special handling for the following schemes:

        - http(s): The size and digest of the file will be inferred by the
          `Content-Length` and the `ETag` response headers returned by the server.
        - s3: The checksum and size will be pulled from the object metadata. If bucket
          versioning is enabled, then the version ID is also tracked.
        - gs: The checksum and size will be pulled from the object metadata. If bucket
          versioning is enabled, then the version ID is also tracked.
        - https, domain matching *.blob.core.windows.net (Azure): The checksum and size
          will be pulled from the blob metadata. If storage account versioning is
          enabled, then the version ID is also tracked.
        - file: The checksum and size will be pulled from the file system. This scheme
          is useful if you have an NFS share or other externally mounted volume
          containing files you wish to track but not necessarily upload.

        For any other scheme, the digest is just a hash of the URI and the size is left
        blank.

        Arguments:
            uri: The URI path of the reference to add. Can be an object returned from
                Artifact.get_path to store a reference to another artifact\'s entry.
            name: The path within the artifact to place the contents of this reference
            checksum: Whether or not to checksum the resource(s) located at the
                reference URI. Checksumming is strongly recommended as it enables
                automatic integrity validation, however it can be disabled to speed up
                artifact creation. (default: True)
            max_objects: The maximum number of objects to consider when adding a
                reference that points to directory or bucket store prefix. For S3 and
                GCS, this limit is 10,000 by default but is uncapped for other URI
                schemes. (default: None)

        Returns:
            The added manifest entries.

        Raises:
            ArtifactFinalizedError: if the artifact has already been finalized.

        Examples:
            Add an HTTP link:
            ```python
            # Adds `file.txt` to the root of the artifact as a reference.
            artifact.add_reference("http://myserver.com/file.txt")
            ```

            Add an S3 prefix without an explicit name:
            ```python
            # All objects under `prefix/` will be added at the root of the artifact.
            artifact.add_reference("s3://mybucket/prefix")
            ```

            Add a GCS prefix with an explicit name:
            ```python
            # All objects under `prefix/` will be added under `path/` at the artifact
            # root.
            artifact.add_reference("gs://mybucket/prefix", name="path")
            ```
        '''
    def add(self, obj: data_types.WBValue, name: StrPath) -> ArtifactManifestEntry:
        '''Add wandb.WBValue `obj` to the artifact.

        Arguments:
            obj: The object to add. Currently support one of Bokeh, JoinedTable,
                PartitionedTable, Table, Classes, ImageMask, BoundingBoxes2D, Audio,
                Image, Video, Html, Object3D
            name: The path within the artifact to add the object.

        Returns:
            The added manifest entry

        Raises:
            ArtifactFinalizedError: if the artifact has already been finalized

        Examples:
            Basic usage:
            ```python
            artifact = wandb.Artifact("my_table", type="dataset")
            table = wandb.Table(
                columns=["a", "b", "c"], data=[(i, i * 2, 2**i) for i in range(10)]
            )
            artifact.add(table, "my_table")

            wandb.log_artifact(artifact)
            ```

            Retrieve an object:
            ```python
            artifact = wandb.use_artifact("my_table:latest")
            table = artifact.get("my_table")
            ```
        '''
    def remove(self, item: StrPath | ArtifactManifestEntry) -> None:
        """Remove an item from the artifact.

        Arguments:
            item: the item to remove. Can be a specific manifest entry or the name of an
                artifact-relative path. If the item matches a directory all items in
                that directory will be removed.

        Raises:
            ArtifactFinalizedError: if the artifact has already been finalized.
            FileNotFoundError: if the item isn't found in the artifact.
        """
    def get_path(self, name: StrPath) -> ArtifactManifestEntry:
        '''Get the entry with the given name.

        Arguments:
            name: The artifact relative name to get

        Raises:
            ArtifactNotLoggedError: if the artifact isn\'t logged or the run is offline
            KeyError: if the artifact doesn\'t contain an entry with the given name

        Examples:
            Basic usage:
            ```python
            # Run logging the artifact
            with wandb.init() as r:
                artifact = wandb.Artifact("my_dataset", type="dataset")
                artifact.add_file("path/to/file.txt")
                wandb.log_artifact(artifact)

            # Run using the artifact
            with wandb.init() as r:
                artifact = r.use_artifact("my_dataset:latest")
                path = artifact.get_path("file.txt")

                # Can now download \'file.txt\' directly:
                path.download()
            ```
        '''
    def get(self, name: str) -> data_types.WBValue | None:
        '''Get the WBValue object located at the artifact relative `name`.

        Arguments:
            name: The artifact relative name to get

        Raises:
            ArtifactNotLoggedError: if the artifact isn\'t logged or the run is offline

        Examples:
            Basic usage:
            ```python
            # Run logging the artifact
            with wandb.init() as r:
                artifact = wandb.Artifact("my_dataset", type="dataset")
                table = wandb.Table(
                    columns=["a", "b", "c"], data=[(i, i * 2, 2**i) for i in range(10)]
                )
                artifact.add(table, "my_table")
                wandb.log_artifact(artifact)

            # Run using the artifact
            with wandb.init() as r:
                artifact = r.use_artifact("my_dataset:latest")
                table = artifact.get("my_table")
            ```
        '''
    def get_added_local_path_name(self, local_path: str) -> str | None:
        '''Get the artifact relative name of a file added by a local filesystem path.

        Arguments:
            local_path: The local path to resolve into an artifact relative name.

        Returns:
            The artifact relative name.

        Examples:
            Basic usage:
            ```python
            artifact = wandb.Artifact("my_dataset", type="dataset")
            artifact.add_file("path/to/file.txt", name="artifact/path/file.txt")

            # Returns `artifact/path/file.txt`:
            name = artifact.get_added_local_path_name("path/to/file.txt")
            ```
        '''
    def download(self, root: str | None = None, recursive: bool = False, allow_missing_references: bool = False) -> FilePathStr:
        """Download the contents of the artifact to the specified root directory.

        NOTE: Any existing files at `root` are left untouched. Explicitly delete
        root before calling `download` if you want the contents of `root` to exactly
        match the artifact.

        Arguments:
            root: The directory in which to download this artifact's files.
            recursive: If true, then all dependent artifacts are eagerly downloaded.
                Otherwise, the dependent artifacts are downloaded as needed.

        Returns:
            The path to the downloaded contents.

        Raises:
            ArtifactNotLoggedError: if the artifact has not been logged
        """
    def checkout(self, root: str | None = None) -> str:
        """Replace the specified root directory with the contents of the artifact.

        WARNING: This will DELETE all files in `root` that are not included in the
        artifact.

        Arguments:
            root: The directory to replace with this artifact's files.

        Returns:
           The path to the checked out contents.

        Raises:
            ArtifactNotLoggedError: if the artifact has not been logged
        """
    def verify(self, root: str | None = None) -> None:
        """Verify that the actual contents of an artifact match the manifest.

        All files in the directory are checksummed and the checksums are then
        cross-referenced against the artifact's manifest.

        NOTE: References are not verified.

        Arguments:
            root: The directory to verify. If None artifact will be downloaded to
                './artifacts/self.name/'

        Raises:
            ArtifactNotLoggedError: if the artifact has not been logged
            ValueError: If the verification fails.
        """
    def file(self, root: str | None = None) -> StrPath:
        """Download a single file artifact to dir specified by the root.

        Arguments:
            root: The root directory in which to place the file. Defaults to
                './artifacts/self.name/'.

        Returns:
            The full path of the downloaded file.

        Raises:
            ArtifactNotLoggedError: if the artifact has not been logged
            ValueError: if the artifact contains more than one file
        """
    def files(self, names: List[str] | None = None, per_page: int = 50) -> ArtifactFiles:
        """Iterate over all files stored in this artifact.

        Arguments:
            names: The filename paths relative to the root of the artifact you wish to
                list.
            per_page: The number of files to return per request

        Returns:
            An iterator containing `File` objects

        Raises:
            ArtifactNotLoggedError: if the artifact has not been logged
        """
    def delete(self, delete_aliases: bool = False) -> None:
        '''Delete an artifact and its files.

        Arguments:
            delete_aliases: If true, deletes all aliases associated with the artifact.
                Otherwise, this raises an exception if the artifact has existing
                aliases.

        Raises:
            ArtifactNotLoggedError: if the artifact has not been logged

        Examples:
            Delete all the "model" artifacts a run has logged:
            ```python
            runs = api.runs(path="my_entity/my_project")
            for run in runs:
                for artifact in run.logged_artifacts():
                    if artifact.type == "model":
                        artifact.delete(delete_aliases=True)
            ```
        '''
    def link(self, target_path: str, aliases: List[str] | None = None) -> None:
        """Link this artifact to a portfolio (a promoted collection of artifacts).

        Arguments:
            target_path: The path to the portfolio. It must take the form {portfolio},
                {project}/{portfolio} or {entity}/{project}/{portfolio}.
            aliases: A list of strings which uniquely identifies the artifact inside the
                specified portfolio.

        Raises:
            ArtifactNotLoggedError: if the artifact has not been logged
        """
    def used_by(self) -> List[Run]:
        """Get a list of the runs that have used this artifact.

        Raises:
            ArtifactNotLoggedError: if the artifact has not been logged
        """
    def logged_by(self) -> Run | None:
        """Get the run that first logged this artifact.

        Raises:
            ArtifactNotLoggedError: if the artifact has not been logged
        """
    def json_encode(self) -> Dict[str, Any]: ...

class _ArtifactVersionType(WBType):
    name: str
    types: Incomplete
