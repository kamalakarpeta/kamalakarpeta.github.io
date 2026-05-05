from typing import Dict
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.lib.capped_dict import CappedDict as CappedDict

artifact_cache: Dict[str, 'Artifact']
