from _typeshed import Incomplete
from tensorflow_estimator.python.estimator.canned.timeseries.feature_keys import TrainEvalFeatures as TrainEvalFeatures
from typing import NamedTuple

def replicate_state(start_state, batch_size):
    """Create batch versions of state.

  Takes a list of Tensors, adds a batch dimension, and replicates
  batch_size times across that batch dimension. Used to replicate the
  non-batch state returned by get_start_state in define_loss.

  Args:
    start_state: Model-defined state to replicate.
    batch_size: Batch dimension for data.

  Returns:
    Replicated versions of the state.
  """

class Moments(NamedTuple):
    mean: Incomplete
    variance: Incomplete

class InputStatistics(NamedTuple):
    series_start_moments: Incomplete
    overall_feature_moments: Incomplete
    start_time: Incomplete
    total_observation_count: Incomplete

class InputStatisticsFromMiniBatch:
    """Generate statistics from mini-batch input."""
    def __init__(self, num_features, dtype, starting_variance_window_size: int = 16) -> None:
        """Configure the input statistics object.

    Args:
      num_features: Number of features for the time series
      dtype: The floating point data type to use.
      starting_variance_window_size: The number of datapoints to use when
        computing the mean and variance at the start of the series.
    """
    def initialize_graph(self, features, update_statistics: bool = True):
        """Create any ops needed to provide input statistics.

    Should be called before statistics are requested.

    Args:
      features: A dictionary, the output of a `TimeSeriesInputFn` (with keys
        TrainEvalFeatures.TIMES and TrainEvalFeatures.VALUES).
      update_statistics: Whether `features` should be used to update adaptive
        statistics. Typically True for training and false for evaluation.

    Returns:
      An InputStatistics object composed of Variables, which will be updated
      based on mini-batches of data if requested.
    """
    class _AdaptiveInputAuxiliaryStatistics(NamedTuple('_AdaptiveInputAuxiliaryStatistics', [('max_time_seen', Incomplete), ('chunk_count', Incomplete), ('inter_observation_duration_sum', Incomplete), ('example_count', Incomplete), ('overall_feature_sum', Incomplete), ('overall_feature_sum_of_squares', Incomplete)])):
        """Extra statistics used to incrementally update InputStatistics."""
        def __new__(cls, num_features, dtype): ...
