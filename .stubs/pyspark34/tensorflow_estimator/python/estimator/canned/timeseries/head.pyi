from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import estimator_lib as estimator_lib
from tensorflow_estimator.python.estimator.canned import head as head_lib, metric_keys as metric_keys
from tensorflow_estimator.python.estimator.canned.timeseries import feature_keys as feature_keys
from tensorflow_estimator.python.estimator.export import export_lib as export_lib

class _NoStatePredictOutput(export_lib.PredictOutput):
    def as_signature_def(self, receiver_tensors): ...

class TimeSeriesRegressionHead(head_lib._Head):
    """Determines input and output signatures for a time series model."""
    model: Incomplete
    state_manager: Incomplete
    optimizer: Incomplete
    input_statistics_generator: Incomplete
    def __init__(self, model, state_manager, optimizer, input_statistics_generator: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """Creates a `_Head` for time series regression.

    Args:
      model: A model for time series regression.
      state_manager: A state manager.
      optimizer: An optimizer.
      input_statistics_generator: A input statistics generator.
      name: An optional name for the model.
    """
    @property
    def name(self): ...
    def create_loss(self, features, mode, logits: Incomplete | None = None, labels: Incomplete | None = None):
        """See `_Head`."""
    @property
    def logits_dimension(self):
        """See `_Head`."""
    def create_estimator_spec(self, features, mode, labels: Incomplete | None = None):
        """Performs basic error checking and returns an EstimatorSpec."""

class OneShotPredictionHead(TimeSeriesRegressionHead):
    """A time series head which exports a single stateless serving signature.

  The serving default signature exported by this head expects `times`, `values`,
  and any exogenous features, but no state. `values` has shape `[batch_size,
  filter_length, num_features]` and `times` has shape `[batch_size,
  total_length]`, where `total_length > filter_length`. Any exogenous features
  must have their shapes prefixed by the shape of the `times` feature.

  When serving, first performs filtering on the series up to `filter_length`
  starting from the default start state for the model, then computes predictions
  on the remainder of the series, returning them.

  Model state is neither accepted nor returned, so filtering must be performed
  each time predictions are requested when using this head.
  """

def state_to_dictionary(state_tuple):
    """Flatten model state into a dictionary with string keys."""
