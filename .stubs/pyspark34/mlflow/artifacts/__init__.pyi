from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import BAD_REQUEST as BAD_REQUEST, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.tracking.artifact_utils import add_databricks_profile_info_to_artifact_uri as add_databricks_profile_info_to_artifact_uri, get_artifact_repository as get_artifact_repository

def download_artifacts(artifact_uri: str | None = None, run_id: str | None = None, artifact_path: str | None = None, dst_path: str | None = None, tracking_uri: str | None = None) -> str:
    '''
    Download an artifact file or directory to a local directory.

    :param artifact_uri: URI pointing to the artifacts, such as
                         ``"runs:/500cf58bee2b40a4a82861cc31a617b1/my_model.pkl"``,
                         ``"models:/my_model/Production"``, or ``"s3://my_bucket/my/file.txt"``.
                         Exactly one of ``artifact_uri`` or ``run_id`` must be specified.
    :param run_id: ID of the MLflow Run containing the artifacts. Exactly one of ``run_id`` or
                   ``artifact_uri`` must be specified.
    :param artifact_path: (For use with ``run_id``) If specified, a path relative to the MLflow
                          Run\'s root directory containing the artifacts to download.
    :param dst_path: Path of the local filesystem destination directory to which to download the
                     specified artifacts. If the directory does not exist, it is created. If
                     unspecified, the artifacts are downloaded to a new uniquely-named directory on
                     the local filesystem, unless the artifacts already exist on the local
                     filesystem, in which case their local path is returned directly.
    :param tracking_uri: The tracking URI to be used when downloading artifacts.
    :return: The location of the artifact file or directory on the local filesystem.
    '''
def load_text(artifact_uri: str) -> str:
    '''
    Loads the artifact contents as a string.

    :param artifact_uri: artifact location
    :return: str

    .. code-block:: python
        :caption: Example

        import mlflow

        with mlflow.start_run() as run:
            artifact_uri = run.info.artifact_uri
            mlflow.log_text("This is a sentence", "file.txt")
            file_content = mlflow.artifacts.load_text(artifact_uri + "/file.txt")
            print(file_content)

    .. code-block:: text
        :caption: Output

        This is a sentence
    '''
def load_dict(artifact_uri: str) -> dict:
    '''
    Loads the artifact contents as a dictionary.

    :param artifact_uri: artifact location
    :return: dict

    .. code-block:: python
        :caption: Example

        import mlflow

        with mlflow.start_run() as run:
            artifact_uri = run.info.artifact_uri
            mlflow.log_dict({"mlflow-version": "0.28", "n_cores": "10"}, "config.json")
            config_json = mlflow.artifacts.load_dict(artifact_uri + "/config.json")
            print(config_json)

    .. code-block:: text
        :caption: Output

        {\'mlflow-version\': \'0.28\', \'n_cores\': \'10\'}
    '''
def load_image(artifact_uri: str):
    '''
    Loads artifact contents as a ``PIL.Image.Image`` object

    :param artifact_uri: artifact location
    :return: PIL.Image

    .. code-block:: python
        :caption: Example

        import mlflow
        from PIL import Image

        with mlflow.start_run() as run:
            image = Image.new("RGB", (100, 100))
            artifact_uri = run.info.artifact_uri
            mlflow.log_image(image, "image.png")
            image = mlflow.artifacts.load_image(artifact_uri + "/image.png")
            print(image)

    .. code-block:: text
        :caption: Output

        <PIL.PngImagePlugin.PngImageFile image mode=RGB size=100x100 at 0x11D2FA3D0>
    '''
