from _typeshed import Incomplete
from tensorflow.python.debug.lib import common as common
from tensorflow.python.debug.wrappers import framework as framework

def publish_traceback(debug_server_urls, graph, feed_dict, fetches, old_graph_version):
    """Publish traceback and source code if graph version is new.

  `graph.version` is compared with `old_graph_version`. If the former is higher
  (i.e., newer), the graph traceback and the associated source code is sent to
  the debug server at the specified gRPC URLs.

  Args:
    debug_server_urls: A single gRPC debug server URL as a `str` or a `list` of
      debug server URLs.
    graph: A Python `tf.Graph` object.
    feed_dict: Feed dictionary given to the `Session.run()` call.
    fetches: Fetches from the `Session.run()` call.
    old_graph_version: Old graph version to compare to.

  Returns:
    If `graph.version > old_graph_version`, the new graph version as an `int`.
    Else, the `old_graph_version` is returned.
  """

class GrpcDebugWrapperSession(framework.NonInteractiveDebugWrapperSession):
    """Debug Session wrapper that send debug data to gRPC stream(s)."""
    def __init__(self, sess, grpc_debug_server_addresses, watch_fn: Incomplete | None = None, thread_name_filter: Incomplete | None = None, log_usage: bool = True) -> None:
        '''Constructor of DumpingDebugWrapperSession.

    Args:
      sess: The TensorFlow `Session` object being wrapped.
      grpc_debug_server_addresses: (`str` or `list` of `str`) Single or a list
        of the gRPC debug server addresses, in the format of
        <host:port>, with or without the "grpc://" prefix. For example:
          "localhost:7000",
          ["localhost:7000", "192.168.0.2:8000"]
      watch_fn: (`Callable`) A Callable that can be used to define per-run
        debug ops and watched tensors. See the doc of
        `NonInteractiveDebugWrapperSession.__init__()` for details.
      thread_name_filter: Regular-expression white list for threads on which the
        wrapper session will be active. See doc of `BaseDebugWrapperSession` for
        more details.
      log_usage: (`bool`) whether the usage of this class is to be logged.

    Raises:
       TypeError: If `grpc_debug_server_addresses` is not a `str` or a `list`
         of `str`.
    '''
    def prepare_run_debug_urls(self, fetches, feed_dict):
        """Implementation of abstract method in superclass.

    See doc of `NonInteractiveDebugWrapperSession.prepare_run_debug_urls()`
    for details.

    Args:
      fetches: Same as the `fetches` argument to `Session.run()`
      feed_dict: Same as the `feed_dict` argument to `Session.run()`

    Returns:
      debug_urls: (`str` or `list` of `str`) file:// debug URLs to be used in
        this `Session.run()` call.
    """

def register_signal_handler() -> None: ...

class TensorBoardDebugWrapperSession(GrpcDebugWrapperSession):
    """A tfdbg Session wrapper that can be used with TensorBoard Debugger Plugin.

  This wrapper is the same as `GrpcDebugWrapperSession`, except that it uses a
    predefined `watch_fn` that
    1) uses `DebugIdentity` debug ops with the `gated_grpc` attribute set to
        `True` to allow the interactive enabling and disabling of tensor
       breakpoints.
    2) watches all tensors in the graph.
  This saves the need for the user to define a `watch_fn`.
  """
    def __init__(self, sess, grpc_debug_server_addresses, thread_name_filter: Incomplete | None = None, send_traceback_and_source_code: bool = True, log_usage: bool = True) -> None:
        '''Constructor of TensorBoardDebugWrapperSession.

    Args:
      sess: The `tf.compat.v1.Session` instance to be wrapped.
      grpc_debug_server_addresses: gRPC address(es) of debug server(s), as a
        `str` or a `list` of `str`s. E.g., "localhost:2333",
        "grpc://localhost:2333", ["192.168.0.7:2333", "192.168.0.8:2333"].
      thread_name_filter: Optional filter for thread names.
      send_traceback_and_source_code: Whether traceback of graph elements and
        the source code are to be sent to the debug server(s).
      log_usage: Whether the usage of this class is to be logged (if
        applicable).
    '''
    def run(self, fetches, feed_dict: Incomplete | None = None, options: Incomplete | None = None, run_metadata: Incomplete | None = None, callable_runner: Incomplete | None = None, callable_runner_args: Incomplete | None = None, callable_options: Incomplete | None = None): ...
