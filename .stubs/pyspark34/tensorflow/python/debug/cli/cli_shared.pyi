from _typeshed import Incomplete
from tensorflow.python.debug.cli import command_parser as command_parser, debugger_cli_common as debugger_cli_common, tensor_format as tensor_format
from tensorflow.python.debug.lib import common as common
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import variables as variables
from tensorflow.python.platform import gfile as gfile

RL = debugger_cli_common.RichLine
DEFAULT_NDARRAY_DISPLAY_THRESHOLD: int
COLOR_BLACK: str
COLOR_BLUE: str
COLOR_CYAN: str
COLOR_GRAY: str
COLOR_GREEN: str
COLOR_MAGENTA: str
COLOR_RED: str
COLOR_WHITE: str
COLOR_YELLOW: str
TIME_UNIT_US: str
TIME_UNIT_MS: str
TIME_UNIT_S: str
TIME_UNITS: Incomplete

def bytes_to_readable_str(num_bytes, include_b: bool = False):
    """Generate a human-readable string representing number of bytes.

  The units B, kB, MB and GB are used.

  Args:
    num_bytes: (`int` or None) Number of bytes.
    include_b: (`bool`) Include the letter B at the end of the unit.

  Returns:
    (`str`) A string representing the number of bytes in a human-readable way,
      including a unit at the end.
  """
def time_to_readable_str(value_us, force_time_unit: Incomplete | None = None):
    """Convert time value to human-readable string.

  Args:
    value_us: time value in microseconds.
    force_time_unit: force the output to use the specified time unit. Must be
      in TIME_UNITS.

  Returns:
    Human-readable string representation of the time value.

  Raises:
    ValueError: if force_time_unit value is not in TIME_UNITS.
  """
def parse_ranges_highlight(ranges_string):
    """Process ranges highlight string.

  Args:
    ranges_string: (str) A string representing a numerical range of a list of
      numerical ranges. See the help info of the -r flag of the print_tensor
      command for more details.

  Returns:
    An instance of tensor_format.HighlightOptions, if range_string is a valid
      representation of a range or a list of ranges.
  """
def numpy_printoptions_from_screen_info(screen_info): ...
def format_tensor(tensor, tensor_name, np_printoptions, print_all: bool = False, tensor_slicing: Incomplete | None = None, highlight_options: Incomplete | None = None, include_numeric_summary: bool = False, write_path: Incomplete | None = None):
    '''Generate formatted str to represent a tensor or its slices.

  Args:
    tensor: (numpy ndarray) The tensor value.
    tensor_name: (str) Name of the tensor, e.g., the tensor\'s debug watch key.
    np_printoptions: (dict) Numpy tensor formatting options.
    print_all: (bool) Whether the tensor is to be displayed in its entirety,
      instead of printing ellipses, even if its number of elements exceeds
      the default numpy display threshold.
      (Note: Even if this is set to true, the screen output can still be cut
       off by the UI frontend if it consist of more lines than the frontend
       can handle.)
    tensor_slicing: (str or None) Slicing of the tensor, e.g., "[:, 1]". If
      None, no slicing will be performed on the tensor.
    highlight_options: (tensor_format.HighlightOptions) options to highlight
      elements of the tensor. See the doc of tensor_format.format_tensor()
      for more details.
    include_numeric_summary: Whether a text summary of the numeric values (if
      applicable) will be included.
    write_path: A path to save the tensor value (after any slicing) to
      (optional). `numpy.save()` is used to save the value.

  Returns:
    An instance of `debugger_cli_common.RichTextLines` representing the
    (potentially sliced) tensor.
  '''
def error(msg):
    """Generate a RichTextLines output for error.

  Args:
    msg: (str) The error message.

  Returns:
    (debugger_cli_common.RichTextLines) A representation of the error message
      for screen output.
  """
def get_tfdbg_logo():
    """Make an ASCII representation of the tfdbg logo."""
def get_run_start_intro(run_call_count, fetches, feed_dict, tensor_filters, is_callable_runner: bool = False):
    """Generate formatted intro for run-start UI.

  Args:
    run_call_count: (int) Run call counter.
    fetches: Fetches of the `Session.run()` call. See doc of `Session.run()`
      for more details.
    feed_dict: Feeds to the `Session.run()` call. See doc of `Session.run()`
      for more details.
    tensor_filters: (dict) A dict from tensor-filter name to tensor-filter
      callable.
    is_callable_runner: (bool) whether a runner returned by
        Session.make_callable is being run.

  Returns:
    (RichTextLines) Formatted intro message about the `Session.run()` call.
  """
def get_run_short_description(run_call_count, fetches, feed_dict, is_callable_runner: bool = False):
    """Get a short description of the run() call.

  Args:
    run_call_count: (int) Run call counter.
    fetches: Fetches of the `Session.run()` call. See doc of `Session.run()`
      for more details.
    feed_dict: Feeds to the `Session.run()` call. See doc of `Session.run()`
      for more details.
    is_callable_runner: (bool) whether a runner returned by
        Session.make_callable is being run.

  Returns:
    (str) A short description of the run() call, including information about
      the fetche(s) and feed(s).
  """
def get_error_intro(tf_error):
    """Generate formatted intro for TensorFlow run-time error.

  Args:
    tf_error: (errors.OpError) TensorFlow run-time error object.

  Returns:
    (RichTextLines) Formatted intro message about the run-time OpError, with
      sample commands for debugging.
  """
