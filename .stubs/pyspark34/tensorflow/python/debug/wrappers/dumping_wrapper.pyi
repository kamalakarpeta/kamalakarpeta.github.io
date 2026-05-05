from _typeshed import Incomplete
from tensorflow.core.util import event_pb2 as event_pb2
from tensorflow.python.debug.lib import debug_data as debug_data
from tensorflow.python.debug.wrappers import framework as framework
from tensorflow.python.platform import gfile as gfile

class DumpingDebugWrapperSession(framework.NonInteractiveDebugWrapperSession):
    """Debug Session wrapper that dumps debug data to filesystem."""
    def __init__(self, sess, session_root, watch_fn: Incomplete | None = None, thread_name_filter: Incomplete | None = None, pass_through_operrors: Incomplete | None = None, log_usage: bool = True) -> None:
        """Constructor of DumpingDebugWrapperSession.

    Args:
      sess: The TensorFlow `Session` object being wrapped.
      session_root: (`str`) Path to the session root directory. Must be a
        directory that does not exist or an empty directory. If the directory
        does not exist, it will be created by the debugger core during debug
        `tf.Session.run`
        calls.
        As the `run()` calls occur, subdirectories will be added to
        `session_root`. The subdirectories' names has the following pattern:
          run_<epoch_time_stamp>_<zero_based_run_counter>
        E.g., run_1480734393835964_ad4c953a85444900ae79fc1b652fb324
      watch_fn: (`Callable`) A Callable that can be used to define per-run
        debug ops and watched tensors. See the doc of
        `NonInteractiveDebugWrapperSession.__init__()` for details.
      thread_name_filter: Regular-expression white list for threads on which the
        wrapper session will be active. See doc of `BaseDebugWrapperSession` for
        more details.
      pass_through_operrors: If true, all captured OpErrors will be
        propagated. By default this captures all OpErrors.
      log_usage: (`bool`) whether the usage of this class is to be logged.

    Raises:
       ValueError: If `session_root` is an existing and non-empty directory or
       if `session_root` is a file.
    """
    def prepare_run_debug_urls(self, fetches, feed_dict):
        """Implementation of abstract method in superclass.

    See doc of `NonInteractiveDebugWrapperSession.prepare_run_debug_urls()`
    for details. This implementation creates a run-specific subdirectory under
    self._session_root and stores information regarding run `fetches` and
    `feed_dict.keys()` in the subdirectory.

    Args:
      fetches: Same as the `fetches` argument to `Session.run()`
      feed_dict: Same as the `feed_dict` argument to `Session.run()`

    Returns:
      debug_urls: (`str` or `list` of `str`) file:// debug URLs to be used in
        this `Session.run()` call.
    """
