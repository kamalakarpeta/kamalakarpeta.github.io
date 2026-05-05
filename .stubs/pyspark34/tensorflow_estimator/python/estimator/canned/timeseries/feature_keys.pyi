from _typeshed import Incomplete

class State:
    """Key formats for accepting/returning state."""
    STATE_TUPLE: str
    STATE_PREFIX: str

class Times:
    """Key formats for accepting/returning times."""
    TIMES: str

class Values:
    """Key formats for accepting/returning values."""
    VALUES: str

class TrainEvalFeatures(Times, Values):
    """Feature names used during training and evaluation."""
class PredictionFeatures(Times, State):
    """Feature names used during prediction."""
class FilteringFeatures(Times, Values, State):
    """Special feature names for filtering."""
class PredictionResults(Times):
    """Keys returned when predicting (not comprehensive)."""
class FilteringResults(Times, State):
    """Keys returned from evaluation/filtering."""

class SavedModelLabels:
    """Names of signatures exported with export_saved_model."""
    PREDICT: Incomplete
    FILTER: str
    COLD_START_FILTER: str
