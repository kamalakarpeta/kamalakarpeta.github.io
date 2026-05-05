from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops

def assert_next(transformations):
    '''A transformation that asserts which transformations happen next.

  Transformations should be referred to by their base name, not including
  version suffix. For example, use "Batch" instead of "BatchV2". "Batch" will
  match any of "Batch", "BatchV1", "BatchV2", etc.

  Args:
    transformations: A `tf.string` vector `tf.Tensor` identifying the
      transformations that are expected to happen next.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  '''
def assert_prev(transformations):
    '''Asserts which transformations, with which attributes, happened previously.

    Each transformation is repesented as a tuple in the input.

    The first element is the base op name of the transformation, not including
    version suffix.  For example, use "BatchDataset" instead of
    "BatchDatasetV2".  "BatchDataset" will match any of "BatchDataset",
    "BatchDatasetV1", "BatchDatasetV2", etc.

    The second element is a dict of attribute name-value pairs.  Attributes
    values must be of type bool, int, or string.

    Example usage:

    >>> dataset_ops.Dataset.from_tensors(0) \\\n    ... .map(lambda x: x) \\\n    ... .batch(1, deterministic=True, num_parallel_calls=8) \\\n    ... .assert_prev([("ParallelBatchDataset", {"deterministic": True}), \\\n    ...               ("MapDataset", {})])

  Args:
    transformations: A list of tuples identifying the (required) transformation
      name, with (optional) attribute name-value pairs, that are expected to
      have happened previously.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  '''
def non_serializable():
    """A non-serializable identity transformation.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  """
def sleep(sleep_microseconds):
    """Sleeps for `sleep_microseconds` before producing each input element.

  Args:
    sleep_microseconds: The number of microseconds to sleep before producing an
      input element.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  """

class _AssertNextDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that asserts which transformations happen next."""
    def __init__(self, input_dataset, transformations) -> None:
        """See `assert_next()` for details."""

class _AssertPrevDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that asserts which transformations happened previously."""
    def __init__(self, input_dataset, transformations) -> None:
        """See `assert_prev()` for details."""

class _NonSerializableDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that performs non-serializable identity transformation."""
    def __init__(self, input_dataset) -> None:
        """See `non_serializable()` for details."""

class _SleepDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that sleeps before producing each upstream element."""
    def __init__(self, input_dataset, sleep_microseconds) -> None: ...
