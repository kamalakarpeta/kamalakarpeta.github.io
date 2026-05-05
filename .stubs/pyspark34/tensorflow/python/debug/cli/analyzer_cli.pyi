from _typeshed import Incomplete
from tensorflow.python.debug.cli import cli_config as cli_config, cli_shared as cli_shared, command_parser as command_parser, debugger_cli_common as debugger_cli_common, evaluator as evaluator, ui_factory as ui_factory
from tensorflow.python.debug.lib import debug_graphs as debug_graphs, source_utils as source_utils

RL: Incomplete
HANG_UNFINISHED: str
HANG_FINISHED: str
HANG_SUFFIX: str
DEPTH_TEMPLATE: str
OP_TYPE_TEMPLATE: str
CTRL_LABEL: str
ELLIPSIS: str
SORT_TENSORS_BY_TIMESTAMP: str
SORT_TENSORS_BY_DUMP_SIZE: str
SORT_TENSORS_BY_OP_TYPE: str
SORT_TENSORS_BY_TENSOR_NAME: str

class DebugAnalyzer:
    """Analyzer for debug data from dump directories."""
    def __init__(self, debug_dump, config) -> None:
        """DebugAnalyzer constructor.

    Args:
      debug_dump: A DebugDumpDir object.
      config: A `cli_config.CLIConfig` object that carries user-facing
        configurations.
    """
    def add_tensor_filter(self, filter_name, filter_callable) -> None:
        """Add a tensor filter.

    A tensor filter is a named callable of the signature:
      filter_callable(dump_datum, tensor),

    wherein dump_datum is an instance of debug_data.DebugTensorDatum carrying
    metadata about the dumped tensor, including tensor name, timestamps, etc.
    tensor is the value of the dumped tensor as an numpy.ndarray object.
    The return value of the function is a bool.
    This is the same signature as the input argument to
    debug_data.DebugDumpDir.find().

    Args:
      filter_name: (str) name of the filter. Cannot be empty.
      filter_callable: (callable) a filter function of the signature described
        as above.

    Raises:
      ValueError: If filter_name is an empty str.
      TypeError: If filter_name is not a str.
                 Or if filter_callable is not callable.
    """
    def get_tensor_filter(self, filter_name):
        """Retrieve filter function by name.

    Args:
      filter_name: Name of the filter set during add_tensor_filter() call.

    Returns:
      The callable associated with the filter name.

    Raises:
      ValueError: If there is no tensor filter of the specified filter name.
    """
    def get_help(self, handler_name): ...
    def list_tensors(self, args, screen_info: Incomplete | None = None):
        """Command handler for list_tensors.

    List tensors dumped during debugged Session.run() call.

    Args:
      args: Command-line arguments, excluding the command prefix, as a list of
        str.
      screen_info: Optional dict input containing screen information such as
        cols.

    Returns:
      Output text lines as a RichTextLines object.

    Raises:
      ValueError: If `--filter_exclude_node_names` is used without `-f` or
        `--tensor_filter` being used.
    """
    def node_info(self, args, screen_info: Incomplete | None = None):
        """Command handler for node_info.

    Query information about a given node.

    Args:
      args: Command-line arguments, excluding the command prefix, as a list of
        str.
      screen_info: Optional dict input containing screen information such as
        cols.

    Returns:
      Output text lines as a RichTextLines object.
    """
    def list_inputs(self, args, screen_info: Incomplete | None = None):
        """Command handler for inputs.

    Show inputs to a given node.

    Args:
      args: Command-line arguments, excluding the command prefix, as a list of
        str.
      screen_info: Optional dict input containing screen information such as
        cols.

    Returns:
      Output text lines as a RichTextLines object.
    """
    def print_tensor(self, args, screen_info: Incomplete | None = None):
        """Command handler for print_tensor.

    Print value of a given dumped tensor.

    Args:
      args: Command-line arguments, excluding the command prefix, as a list of
        str.
      screen_info: Optional dict input containing screen information such as
        cols.

    Returns:
      Output text lines as a RichTextLines object.
    """
    def list_outputs(self, args, screen_info: Incomplete | None = None):
        """Command handler for inputs.

    Show inputs to a given node.

    Args:
      args: Command-line arguments, excluding the command prefix, as a list of
        str.
      screen_info: Optional dict input containing screen information such as
        cols.

    Returns:
      Output text lines as a RichTextLines object.
    """
    def evaluate_expression(self, args, screen_info: Incomplete | None = None): ...
    def print_source(self, args, screen_info: Incomplete | None = None):
        """Print the content of a source file."""
    def list_source(self, args, screen_info: Incomplete | None = None):
        """List Python source files that constructed nodes and tensors."""

def create_analyzer_ui(debug_dump, tensor_filters: Incomplete | None = None, ui_type: str = 'curses', on_ui_exit: Incomplete | None = None, config: Incomplete | None = None):
    '''Create an instance of CursesUI based on a DebugDumpDir object.

  Args:
    debug_dump: (debug_data.DebugDumpDir) The debug dump to use.
    tensor_filters: (dict) A dict mapping tensor filter name (str) to tensor
      filter (Callable).
    ui_type: (str) requested UI type, e.g., "curses", "readline".
    on_ui_exit: (`Callable`) the callback to be called when the UI exits.
    config: A `cli_config.CLIConfig` object.

  Returns:
    (base_ui.BaseUI) A BaseUI subtype object with a set of standard analyzer
      commands and tab-completions registered.
  '''
