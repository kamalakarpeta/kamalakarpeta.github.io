import threading
from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.eager import context as context
from tensorflow.python.keras.engine import base_layer_utils as base_layer_utils
from tensorflow.python.keras.utils import control_flow_util as control_flow_util, tf_contextlib as tf_contextlib, tf_inspect as tf_inspect
from tensorflow.python.keras.utils.generic_utils import LazyLoader as LazyLoader
from tensorflow.python.util import tf_decorator as tf_decorator

training_lib: Incomplete

def use_wrapped_call(layer, call_fn, default_training_value: Incomplete | None = None, return_method: bool = False):
    """Creates fn that adds the losses returned by call_fn & returns the outputs.

  Args:
    layer: A Keras layer object
    call_fn: tf.function that takes layer inputs (and possibly a training arg),
      and returns a tuple of (outputs, list of losses).
    default_training_value: Default value of the training kwarg. If `None`, the
      default is `K.learning_phase()`.
    return_method: Whether to return a method bound to the layer.

  Returns:
    function that calls call_fn and returns the outputs. Losses returned by
    call_fn are added to the layer losses.
  """
def layer_uses_training_bool(layer):
    """Returns whether this layer or any of its children uses the training arg."""
def list_all_layers(obj): ...
def list_all_layers_and_sublayers(obj): ...
def maybe_add_training_arg(original_call, wrapped_call, expects_training_arg, default_training_value):
    """Decorate call and optionally adds training argument.

  If a layer expects a training argument, this function ensures that 'training'
  is present in the layer args or kwonly args, with the default training value.

  Args:
    original_call: Original call function.
    wrapped_call: Wrapped call function.
    expects_training_arg: Whether to include 'training' argument.
    default_training_value: Default value of the training kwarg to include in
      the arg spec. If `None`, the default is `K.learning_phase()`.

  Returns:
    Tuple of (
      function that calls `wrapped_call` and sets the training arg,
      Argspec of returned function or `None` if the argspec is unchanged)
  """
def get_training_arg_index(call_fn):
    """Returns the index of 'training' in the layer call function arguments.

  Args:
    call_fn: Call function.

  Returns:
    - n: index of 'training' in the call function arguments.
    - -1: if 'training' is not found in the arguments, but layer.call accepts
          variable keyword arguments
    - None: if layer doesn't expect a training argument.
  """
def set_training_arg(training, index, args, kwargs): ...
def get_training_arg(index, args, kwargs): ...
def remove_training_arg(index, args, kwargs) -> None: ...

class SaveOptionsContext(threading.local):
    save_traces: bool
    def __init__(self) -> None: ...

def keras_option_scope(save_traces) -> Generator[None, None, None]: ...
def should_save_traces():
    """Whether to trace layer functions-can be disabled in the save_traces arg."""
def no_automatic_dependency_tracking_scope(obj) -> Generator[None, None, None]:
    """A context that disables automatic dependency tracking when assigning attrs.

  Objects that inherit from Autotrackable automatically creates dependencies
  to trackable objects through attribute assignments, and wraps data structures
  (lists or dicts) with trackable classes. This scope may be used to temporarily
  disable this behavior. This works similar to the decorator
  `no_automatic_dependency_tracking`.

  Example usage:
  ```
  model = tf.keras.Model()
  model.arr1 = []  # Creates a ListWrapper object
  with no_automatic_dependency_tracking_scope(model):
    model.arr2 = []  # Creates a regular, untracked python list
  ```

  Args:
    obj: A trackable object.

  Yields:
    a scope in which the object doesn't track dependencies.
  """
