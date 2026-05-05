from wandb import env as env
from wandb.sdk.lib.filesystem import mkdir_exists_ok as mkdir_exists_ok
from wandb.sdk.lib.paths import FilePathStr as FilePathStr

def get_staging_dir() -> FilePathStr: ...
