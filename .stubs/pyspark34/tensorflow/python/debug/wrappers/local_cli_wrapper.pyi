from _typeshed import Incomplete
from tensorflow.python.debug.cli import analyzer_cli as analyzer_cli, cli_config as cli_config, cli_shared as cli_shared, command_parser as command_parser, debugger_cli_common as debugger_cli_common, profile_analyzer_cli as profile_analyzer_cli, ui_factory as ui_factory
from tensorflow.python.debug.lib import common as common, debug_data as debug_data
from tensorflow.python.debug.wrappers import framework as framework
from tensorflow.python.lib.io import file_io as file_io

class LocalCLIDebugWrapperSession(framework.BaseDebugWrapperSession):
    """Concrete subclass of BaseDebugWrapperSession implementing a local CLI.

  This class has all the methods that a `session.Session` object has, in order
  to support debugging with minimal code changes. Invoking its `run()` method
  will launch the command-line interface (CLI) of tfdbg.
  """
    def __init__(self, sess, dump_root: Incomplete | None = None, log_usage: bool = True, ui_type: str = 'curses', thread_name_filter: Incomplete | None = None, config_file_path: bool = False) -> None:
        """Constructor of LocalCLIDebugWrapperSession.

    Args:
      sess: The TensorFlow `Session` object being wrapped.
      dump_root: (`str`) optional path to the dump root directory. Must be a
        directory that does not exist or an empty directory. If the directory
        does not exist, it will be created by the debugger core during debug
        `run()` calls and removed afterwards. If `None`, the debug dumps will
        be at tfdbg_<random_string> under the system temp directory.
      log_usage: (`bool`) whether the usage of this class is to be logged.
      ui_type: (`str`) requested UI type. Currently supported:
        (curses | readline)
      thread_name_filter: Regular-expression white list for thread name. See
        the doc of `BaseDebugWrapperSession` for details.
      config_file_path: Optional override to the default configuration file
        path, which is at `${HOME}/.tfdbg_config`.

    Raises:
      ValueError: If dump_root is an existing and non-empty directory or if
        dump_root is a file.
    """
    def add_tensor_filter(self, filter_name, tensor_filter) -> None:
        """Add a tensor filter.

    Args:
      filter_name: (`str`) name of the filter.
      tensor_filter: (`callable`) the filter callable. See the doc string of
        `DebugDumpDir.find()` for more details about its signature.
    """
    def on_session_init(self, request):
        """Overrides on-session-init callback.

    Args:
      request: An instance of `OnSessionInitRequest`.

    Returns:
      An instance of `OnSessionInitResponse`.
    """
    def on_run_start(self, request):
        """Overrides on-run-start callback.

    Args:
      request: An instance of `OnRunStartRequest`.

    Returns:
      An instance of `OnRunStartResponse`.
    """
    def on_run_end(self, request):
        """Overrides on-run-end callback.

    Actions taken:
      1) Load the debug dump.
      2) Bring up the Analyzer CLI.

    Args:
      request: An instance of OnSessionInitRequest.

    Returns:
      An instance of OnSessionInitResponse.
    """
