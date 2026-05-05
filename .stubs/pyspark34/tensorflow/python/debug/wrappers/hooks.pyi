from _typeshed import Incomplete
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.debug.lib import debug_utils as debug_utils
from tensorflow.python.debug.wrappers import dumping_wrapper as dumping_wrapper, framework as framework, grpc_wrapper as grpc_wrapper, local_cli_wrapper as local_cli_wrapper
from tensorflow.python.training import session_run_hook as session_run_hook

class LocalCLIDebugHook(session_run_hook.SessionRunHook):
    """Command-line-interface debugger hook.

  Can be used as a hook for `tf.compat.v1.train.MonitoredSession`s and
  `tf.estimator.Estimator`s. Provides a substitute for
  `tfdbg.LocalCLIDebugWrapperSession` in cases where the session is not directly
  available.
  """
    def __init__(self, ui_type: str = 'curses', dump_root: Incomplete | None = None, thread_name_filter: Incomplete | None = None, config_file_path: Incomplete | None = None) -> None:
        """Create a local debugger command-line interface (CLI) hook.

    Args:
      ui_type: (`str`) requested user-interface type. Currently supported:
        (curses | readline).
      dump_root: (`str`) optional path to the dump root directory. Must be a
        directory that does not exist or an empty directory. If the directory
        does not exist, it will be created by the debugger core during debug
        `run()` calls and removed afterwards.
      thread_name_filter: Regular-expression white list for threads on which the
        wrapper session will be active. See doc of `BaseDebugWrapperSession` for
        more details.
      config_file_path: Optional override to the default configuration file
        path, which is at `${HOME}/.tfdbg_config`.
    """
    def add_tensor_filter(self, filter_name, tensor_filter) -> None:
        """Add a tensor filter.

    See doc of `LocalCLIDebugWrapperSession.add_tensor_filter()` for details.
    Override default behavior to accommodate the possibility of this method
    being
    called prior to the initialization of the underlying
    `LocalCLIDebugWrapperSession` object.

    Args:
      filter_name: See doc of `LocalCLIDebugWrapperSession.add_tensor_filter()`
        for details.
      tensor_filter: See doc of
        `LocalCLIDebugWrapperSession.add_tensor_filter()` for details.
    """
    def begin(self) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...

class DumpingDebugHook(session_run_hook.SessionRunHook):
    """A debugger hook that dumps debug data to filesystem.

  Can be used as a hook for `tf.compat.v1.train.MonitoredSession`s and
  `tf.estimator.Estimator`s.
  """
    def __init__(self, session_root, watch_fn: Incomplete | None = None, thread_name_filter: Incomplete | None = None, log_usage: bool = True) -> None:
        """Create a local debugger command-line interface (CLI) hook.

    Args:
      session_root: See doc of
        `dumping_wrapper.DumpingDebugWrapperSession.__init__`.
      watch_fn: See doc of
        `dumping_wrapper.DumpingDebugWrapperSession.__init__`.
      thread_name_filter: Regular-expression white list for threads on which the
        wrapper session will be active. See doc of `BaseDebugWrapperSession` for
        more details.
      log_usage: (bool) Whether usage is to be logged.
    """
    def begin(self) -> None: ...
    def before_run(self, run_context): ...
    def after_run(self, run_context, run_values) -> None: ...

class GrpcDebugHook(session_run_hook.SessionRunHook):
    """A hook that streams debugger-related events to any grpc_debug_server.

  For example, the debugger data server is a grpc_debug_server. The debugger
  data server writes debugger-related events it receives via GRPC to logdir.
  This enables debugging features in Tensorboard such as health pills.

  When the arguments of debug_utils.watch_graph changes, strongly consider
  changing arguments here too so that features are available to tflearn users.

  Can be used as a hook for `tf.compat.v1.train.MonitoredSession`s and
  `tf.estimator.Estimator`s.
  """
    def __init__(self, grpc_debug_server_addresses, watch_fn: Incomplete | None = None, thread_name_filter: Incomplete | None = None, log_usage: bool = True) -> None:
        '''Constructs a GrpcDebugHook.

    Args:
      grpc_debug_server_addresses: (`list` of `str`) A list of the gRPC debug
        server addresses, in the format of <host:port>, with or without the
        "grpc://" prefix. For example: ["localhost:7000", "192.168.0.2:8000"]
      watch_fn: A function that allows for customizing which ops to watch at
        which specific steps. See doc of
        `dumping_wrapper.DumpingDebugWrapperSession.__init__` for details.
      thread_name_filter: Regular-expression white list for threads on which the
        wrapper session will be active. See doc of `BaseDebugWrapperSession` for
        more details.
      log_usage: (bool) Whether usage is to be logged.
    '''
    def before_run(self, run_context):
        """Called right before a session is run.

    Args:
      run_context: A session_run_hook.SessionRunContext. Encapsulates
        information on the run.

    Returns:
      A session_run_hook.SessionRunArgs object.
    """

class TensorBoardDebugHook(GrpcDebugHook):
    """A tfdbg hook that can be used with TensorBoard Debugger Plugin.

  This hook is the same as `GrpcDebugHook`, except that it uses a predefined
    `watch_fn` that
    1) uses `DebugIdentity` debug ops with the `gated_grpc` attribute set to
        `True`, to allow the interactive enabling and disabling of tensor
       breakpoints.
    2) watches all tensors in the graph.
  This saves the need for the user to define a `watch_fn`.
  """
    def __init__(self, grpc_debug_server_addresses, thread_name_filter: Incomplete | None = None, send_traceback_and_source_code: bool = True, log_usage: bool = True) -> None:
        '''Constructor of TensorBoardDebugHook.

    Args:
      grpc_debug_server_addresses: gRPC address(es) of debug server(s), as a
        `str` or a `list` of `str`s. E.g., "localhost:2333",
        "grpc://localhost:2333", ["192.168.0.7:2333", "192.168.0.8:2333"].
      thread_name_filter: Optional filter for thread names.
      send_traceback_and_source_code: Whether traceback of graph elements and
        the source code are to be sent to the debug server(s).
      log_usage: Whether the usage of this class is to be logged (if
        applicable).
    '''
    def before_run(self, run_context): ...
