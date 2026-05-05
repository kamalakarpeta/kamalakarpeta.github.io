import abc
from _typeshed import Incomplete
from tensorflow_estimator.python.estimator.canned.timeseries import math_utils as math_utils
from tensorflow_estimator.python.estimator.canned.timeseries.feature_keys import TrainEvalFeatures as TrainEvalFeatures
from typing import NamedTuple

class ModelOutputs(NamedTuple):
    loss: Incomplete
    end_state: Incomplete
    predictions: Incomplete
    prediction_times: Incomplete

class TimeSeriesModel(metaclass=abc.ABCMeta):
    """Base class for creating generative time series models."""
    num_features: Incomplete
    dtype: Incomplete
    def __init__(self, num_features, exogenous_feature_columns: Incomplete | None = None, dtype=...) -> None:
        """Constructor for generative models.

    Args:
      num_features: Number of features for the time series
      exogenous_feature_columns: A list of `tf.feature_column`s (for example
        `tf.feature_column.embedding_column`) corresponding to exogenous
        features which provide extra information to the model but are not part
        of the series to be predicted. Passed to
        `tf.feature_column.input_layer`.
      dtype: The floating point datatype to use.
    """
    @property
    def exogenous_feature_columns(self):
        """`tf.feature_colum`s for features which are not predicted."""
    def generate(self, number_of_series, series_length, model_parameters: Incomplete | None = None, seed: Incomplete | None = None) -> None:
        """Sample synthetic data from model parameters, with optional substitutions.

    Returns `number_of_series` possible sequences of future values, sampled from
    the generative model with each conditioned on the previous. Samples are
    based on trained parameters, except for those parameters explicitly
    overridden in `model_parameters`.

    For distributions over future observations, see predict().

    Args:
      number_of_series: Number of time series to create.
      series_length: Length of each time series.
      model_parameters: A dictionary mapping model parameters to values, which
        replace trained parameters when generating data.
      seed: If specified, return deterministic time series according to this
        value.

    Returns:
      A dictionary with keys TrainEvalFeatures.TIMES (mapping to an array with
      shape [number_of_series, series_length]) and TrainEvalFeatures.VALUES
      (mapping to an array with shape [number_of_series, series_length,
      num_features]).
    """
    def initialize_graph(self, input_statistics: Incomplete | None = None) -> None:
        """Define ops for the model, not depending on any previously defined ops.

    Args:
      input_statistics: A math_utils.InputStatistics object containing input
        statistics. If None, data-independent defaults are used, which may
        result in longer or unstable training.
    """
    def define_loss(self, features, mode):
        """Default loss definition with state replicated across a batch.

    Time series passed to this model have a batch dimension, and each series in
    a batch can be operated on in parallel. This loss definition assumes that
    each element of the batch represents an independent sample conditioned on
    the same initial state (i.e. it is simply replicated across the batch). A
    batch size of one provides sequential operations on a single time series.

    More complex processing may operate instead on get_start_state() and
    get_batch_loss() directly.

    Args:
      features: A dictionary (such as is produced by a chunker) with at minimum
        the following key/value pairs (others corresponding to the
        `exogenous_feature_columns` argument to `__init__` may be included
        representing exogenous regressors):
        TrainEvalFeatures.TIMES: A [batch size x window size] integer Tensor
          with times for each observation. If there is no artificial chunking,
          the window size is simply the length of the time series.
        TrainEvalFeatures.VALUES: A [batch size x window size x num features]
          Tensor with values for each observation.
      mode: The tf.estimator.ModeKeys mode to use (TRAIN, EVAL). For INFER, see
        predict().

    Returns:
      A ModelOutputs object.
    """
    @abc.abstractmethod
    def get_start_state(self):
        """Returns a tuple of state for the start of the time series.

    For example, a mean and covariance. State should not have a batch
    dimension, and will often be TensorFlow Variables to be learned along with
    the rest of the model parameters.
    """
    @abc.abstractmethod
    def get_batch_loss(self, features, mode, state):
        """Return predictions, losses, and end state for a time series.

    Args:
      features: A dictionary with times, values, and (optionally) exogenous
        regressors. See `define_loss`.
      mode: The tf.estimator.ModeKeys mode to use (TRAIN, EVAL, INFER).
      state: Model-dependent state, each with size [batch size x ...]. The
        number and type will typically be fixed by the model (for example a mean
        and variance).

    Returns:
      A ModelOutputs object.
    """
    @abc.abstractmethod
    def predict(self, features):
        '''Returns predictions of future observations given an initial state.

    Computes distributions for future observations. For sampled draws from the
    model where each is conditioned on the previous, see generate().

    Args:
      features: A dictionary with at minimum the following key/value pairs
        (others corresponding to the `exogenous_feature_columns` argument to
        `__init__` may be included representing exogenous regressors):
        PredictionFeatures.TIMES: A [batch size x window size] Tensor with times
          to make predictions for. Times must be increasing within each part of
          the batch, and must be greater than the last time `state` was updated.
        PredictionFeatures.STATE_TUPLE: Model-dependent state, each with size
          [batch size x ...]. The number and type will typically be fixed by the
          model (for example a mean and variance). Typically these will be the
          end state returned by get_batch_loss, predicting beyond that data.

    Returns:
      A dictionary with model-dependent predictions corresponding to the
      requested times. Keys indicate the type of prediction, and values have
      shape [batch size x window size x ...]. For example state space models
      return a "predicted_mean" and "predicted_covariance".
    '''
