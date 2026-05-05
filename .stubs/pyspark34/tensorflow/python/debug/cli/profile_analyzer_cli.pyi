from _typeshed import Incomplete
from tensorflow.python.debug.cli import cli_shared as cli_shared, command_parser as command_parser, debugger_cli_common as debugger_cli_common, ui_factory as ui_factory
from tensorflow.python.debug.lib import profiling as profiling, source_utils as source_utils

RL: Incomplete
SORT_OPS_BY_OP_NAME: str
SORT_OPS_BY_OP_TYPE: str
SORT_OPS_BY_OP_TIME: str
SORT_OPS_BY_EXEC_TIME: str
SORT_OPS_BY_START_TIME: str
SORT_OPS_BY_LINE: str

class ProfileDataTableView:
    """Table View of profiling data."""
    formatted_start_time: Incomplete
    formatted_op_time: Incomplete
    formatted_exec_time: Incomplete
    def __init__(self, profile_datum_list, time_unit=...) -> None:
        """Constructor.

    Args:
      profile_datum_list: List of `ProfileDatum` objects.
      time_unit: must be in cli_shared.TIME_UNITS.
    """
    def value(self, row, col, device_name_filter: Incomplete | None = None, node_name_filter: Incomplete | None = None, op_type_filter: Incomplete | None = None):
        """Get the content of a cell of the table.

    Args:
      row: (int) row index.
      col: (int) column index.
      device_name_filter: Regular expression to filter by device name.
      node_name_filter: Regular expression to filter by node name.
      op_type_filter: Regular expression to filter by op type.

    Returns:
      A debuggre_cli_common.RichLine object representing the content of the
      cell, potentially with a clickable MenuItem.

    Raises:
      IndexError: if row index is out of range.
    """
    def row_count(self): ...
    def column_count(self): ...
    def column_names(self): ...
    def column_sort_id(self, col): ...

class ProfileAnalyzer:
    """Analyzer for profiling data."""
    def __init__(self, graph, run_metadata) -> None:
        """ProfileAnalyzer constructor.

    Args:
      graph: (tf.Graph) Python graph object.
      run_metadata: A `RunMetadata` protobuf object.

    Raises:
      ValueError: If run_metadata is None.
    """
    def list_profile(self, args, screen_info: Incomplete | None = None):
        """Command handler for list_profile.

    List per-operation profile information.

    Args:
      args: Command-line arguments, excluding the command prefix, as a list of
        str.
      screen_info: Optional dict input containing screen information such as
        cols.

    Returns:
      Output text lines as a RichTextLines object.
    """
    def print_source(self, args, screen_info: Incomplete | None = None):
        """Print a Python source file with line-level profile information.

    Args:
      args: Command-line arguments, excluding the command prefix, as a list of
        str.
      screen_info: Optional dict input containing screen information such as
        cols.

    Returns:
      Output text lines as a RichTextLines object.
    """
    def get_help(self, handler_name): ...

def create_profiler_ui(graph, run_metadata, ui_type: str = 'curses', on_ui_exit: Incomplete | None = None, config: Incomplete | None = None):
    '''Create an instance of CursesUI based on a `tf.Graph` and `RunMetadata`.

  Args:
    graph: Python `Graph` object.
    run_metadata: A `RunMetadata` protobuf object.
    ui_type: (str) requested UI type, e.g., "curses", "readline".
    on_ui_exit: (`Callable`) the callback to be called when the UI exits.
    config: An instance of `cli_config.CLIConfig`.

  Returns:
    (base_ui.BaseUI) A BaseUI subtype object with a set of standard analyzer
      commands and tab-completions registered.
  '''
