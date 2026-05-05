import abc
from _typeshed import Incomplete
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.client import session as session
from tensorflow.python.debug.lib import debug_utils as debug_utils
from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.training import monitored_session as monitored_session
from tensorflow.python.util import nest as nest
from tensorflow.python.util.compat import collections_abc as collections_abc

class OnSessionInitRequest:
    """Request to an on-session-init callback.

  This callback is invoked during the __init__ call to a debug-wrapper session.
  """
    session: Incomplete
    def __init__(self, sess) -> None:
        """Constructor.

    Args:
      sess: A tensorflow Session object.
    """

class OnSessionInitAction:
    """Enum-like values for possible action to take on session init."""
    PROCEED: str
    REMOTE_INSTR_LOOP: str

class OnSessionInitResponse:
    """Response from an on-session-init callback."""
    action: Incomplete
    def __init__(self, action) -> None:
        """Constructor.

    Args:
      action: (`OnSessionInitAction`) Debugger action to take on session init.
    """

class OnRunStartRequest:
    """Request to an on-run-start callback.

  This callback is invoked during a run() call of the debug-wrapper
  session, immediately after the run() call counter is incremented.
  """
    fetches: Incomplete
    feed_dict: Incomplete
    run_options: Incomplete
    run_metadata: Incomplete
    run_call_count: Incomplete
    is_callable_runner: Incomplete
    def __init__(self, fetches, feed_dict, run_options, run_metadata, run_call_count, is_callable_runner: bool = False) -> None:
        """Constructor of `OnRunStartRequest`.

    Args:
      fetches: Fetch targets of the run() call.
      feed_dict: The feed dictionary to the run() call.
      run_options: RunOptions input to the run() call.
      run_metadata: RunMetadata input to the run() call.
        The above four arguments are identical to the input arguments to the
        run() method of a non-wrapped TensorFlow session.
      run_call_count: 1-based count of how many run calls (including this one)
        has been invoked.
      is_callable_runner: (bool) whether a runner returned by
        Session.make_callable is being run.
    """

class OnRunStartAction:
    """Enum-like values for possible action to take on start of a run() call."""
    DEBUG_RUN: str
    PROFILE_RUN: str
    NON_DEBUG_RUN: str

class OnRunStartResponse:
    """Request from an on-run-start callback.

  The caller of the callback can use this response object to specify what
  action the debug-wrapper session actually takes on the run() call.
  """
    action: Incomplete
    debug_urls: Incomplete
    debug_ops: Incomplete
    node_name_regex_allowlist: Incomplete
    op_type_regex_allowlist: Incomplete
    tensor_dtype_regex_allowlist: Incomplete
    tolerate_debug_op_creation_failures: Incomplete
    def __init__(self, action, debug_urls, debug_ops: str = 'DebugIdentity', node_name_regex_allowlist: Incomplete | None = None, op_type_regex_allowlist: Incomplete | None = None, tensor_dtype_regex_allowlist: Incomplete | None = None, tolerate_debug_op_creation_failures: bool = False) -> None:
        """Constructor of `OnRunStartResponse`.

    Args:
      action: (`OnRunStartAction`) the action actually taken by the wrapped
        session for the run() call.
      debug_urls: (`list` of `str`) debug_urls used in watching the tensors
        during the run() call.
      debug_ops: (`str` or `list` of `str`) Debug op(s) to be used by the
        debugger.
      node_name_regex_allowlist: Regular-expression allowlist for node
        name.
      op_type_regex_allowlist: Regular-expression allowlist for op type.
      tensor_dtype_regex_allowlist: Regular-expression allowlist for tensor
        dtype.
      tolerate_debug_op_creation_failures: Whether debug op creation failures
        are to be tolerated.
    """

class OnRunEndRequest:
    """Request to an on-run-end callback.

  The callback is invoked immediately before the wrapped run() call ends.
  """
    performed_action: Incomplete
    run_metadata: Incomplete
    client_graph_def: Incomplete
    tf_error: Incomplete
    def __init__(self, performed_action, run_metadata: Incomplete | None = None, client_graph_def: Incomplete | None = None, tf_error: Incomplete | None = None) -> None:
        """Constructor for `OnRunEndRequest`.

    Args:
      performed_action: (`OnRunStartAction`) Actually-performed action by the
        debug-wrapper session.
      run_metadata: run_metadata output from the run() call (if any).
      client_graph_def: (GraphDef) GraphDef from the client side, i.e., from
        the python front end of TensorFlow. Can be obtained with
        session.graph.as_graph_def().
      tf_error: (errors.OpError subtypes) TensorFlow OpError that occurred
        during the run (if any).
    """

class OnRunEndResponse:
    """Response from an on-run-end callback."""
    def __init__(self) -> None: ...

class BaseDebugWrapperSession(session.SessionInterface, metaclass=abc.ABCMeta):
    """Base class of debug-wrapper session classes.

  Concrete classes that inherit from this class need to implement the abstract
  methods such as on_session_init, on_run_start and on_run_end.
  """
    def __init__(self, sess, thread_name_filter: Incomplete | None = None, pass_through_operrors: bool = False) -> None:
        '''Constructor of `BaseDebugWrapperSession`.

    Args:
      sess: An (unwrapped) TensorFlow session instance. It should be a subtype
        of `BaseSession` or `tf.MonitoredSession`.
      thread_name_filter: Regular-expression filter (allowlist) for name(s) of
        thread(s) on which the wrapper session will be active. This regular
        expression is used in a start-anchored fashion on the thread name, i.e.,
        by applying the `match` method of the compiled pattern. The default
        `None` means that the wrapper session will be active on all threads.
        E.g., r"MainThread$", r"QueueRunnerThread.*".
      pass_through_operrors: If True, all captured OpErrors will be
        propagated.  By default this captures all OpErrors.

    Raises:
      ValueError: On invalid `OnSessionInitAction` value.
      NotImplementedError: If a non-DirectSession sess object is received.
    '''
    @property
    def graph(self): ...
    @property
    def graph_def(self): ...
    @property
    def sess_str(self): ...
    @property
    def session(self): ...
    def run(self, fetches, feed_dict: Incomplete | None = None, options: Incomplete | None = None, run_metadata: Incomplete | None = None, callable_runner: Incomplete | None = None, callable_runner_args: Incomplete | None = None, callable_options: Incomplete | None = None):
        """Wrapper around Session.run() that inserts tensor watch options.

    Args:
      fetches: Same as the `fetches` arg to regular `Session.run()`.
      feed_dict: Same as the `feed_dict` arg to regular `Session.run()`.
      options: Same as the `options` arg to regular `Session.run()`.
      run_metadata: Same as the `run_metadata` arg to regular `Session.run()`.
      callable_runner: A `callable` returned by `Session.make_callable()`.
        If not `None`, `fetches` and `feed_dict` must both be `None`.
        Mutually exclusive with `callable_options`.
      callable_runner_args: An optional list of arguments to `callable_runner`
        or for `callable_options`.
      callable_options: An instance of `config_pb2.CallableOptions`, to be
        used with `Session._make_callable_from_options()`. Mutually exclusive
        with `callable_runner`.

    Returns:
      Simply forwards the output of the wrapped `Session.run()` call.

    Raises:
      ValueError: On invalid `OnRunStartAction` value. Or if `callable_runner`
        is not `None` and either or both of `fetches` and `feed_dict` is `None`.
    """
    def run_step_fn(self, step_fn): ...
    def partial_run_setup(self, fetches, feeds: Incomplete | None = None) -> None:
        """Sets up the feeds and fetches for partial runs in the session."""
    def partial_run(self, handle, fetches, feed_dict: Incomplete | None = None) -> None: ...
    def list_devices(self, *args, **kwargs): ...
    def reset(self, *args, **kwargs): ...
    def make_callable(self, fetches, feed_list: Incomplete | None = None, accept_options: bool = False): ...
    @property
    def run_call_count(self): ...
    def increment_run_call_count(self) -> None: ...
    @abc.abstractmethod
    def on_session_init(self, request):
        """Callback invoked during construction of the debug-wrapper session.

    This is a blocking callback.
    The invocation happens right before the constructor ends.

    Args:
      request: (`OnSessionInitRequest`) callback request carrying information
        such as the session being wrapped.

    Returns:
      An instance of `OnSessionInitResponse`.
    """
    @abc.abstractmethod
    def on_run_start(self, request):
        """Callback invoked on run() calls to the debug-wrapper session.

    This is a blocking callback.
    The invocation happens after the wrapper's run() call is entered,
    after an increment of run call counter.

    Args:
      request: (`OnRunStartRequest`) callback request object carrying
        information about the run call such as the fetches, feed dict, run
        options, run metadata, and how many `run()` calls to this wrapper
        session have occurred.

    Returns:
      An instance of `OnRunStartResponse`, carrying information to
        debug URLs used to watch the tensors.
    """
    @abc.abstractmethod
    def on_run_end(self, request):
        """Callback invoked on run() calls to the debug-wrapper session.

    This is a blocking callback.
    The invocation happens right before the wrapper exits its run() call.

    Args:
      request: (`OnRunEndRequest`) callback request object carrying information
        such as the actual action performed by the session wrapper for the
        run() call.

    Returns:
      An instance of `OnRunStartResponse`.
    """
    def as_default(self): ...
    def __enter__(self): ...
    def __exit__(self, exec_type: type[BaseException] | None, exec_value: BaseException | None, exec_tb: types.TracebackType | None) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def should_stop(self): ...

class WatchOptions:
    """Type for return values of watch_fn."""
    debug_ops: Incomplete
    node_name_regex_allowlist: Incomplete
    op_type_regex_allowlist: Incomplete
    tensor_dtype_regex_allowlist: Incomplete
    tolerate_debug_op_creation_failures: Incomplete
    def __init__(self, debug_ops: Incomplete | None = None, node_name_regex_allowlist: Incomplete | None = None, op_type_regex_allowlist: Incomplete | None = None, tensor_dtype_regex_allowlist: Incomplete | None = None, tolerate_debug_op_creation_failures: bool = False) -> None:
        '''Constructor of WatchOptions: Debug watch options.

    Used as return values of `watch_fn`s.

    Args:
      debug_ops: (`str` or `list of str`) Debug ops to be used.
      node_name_regex_allowlist: Regular-expression allowlist for node_name,
        e.g., `"(weight_[0-9]+|bias_.*)"`
      op_type_regex_allowlist: Regular-expression allowlist for the op type of
        nodes, e.g., `"(Variable|Add)"`.
        If both `node_name_regex_allowlist` and `op_type_regex_allowlist`
        are set, the two filtering operations will occur in a logical `AND`
        relation. In other words, a node will be included if and only if it
        hits both allowlists.
      tensor_dtype_regex_allowlist: Regular-expression allowlist for Tensor
        data type, e.g., `"^int.*"`.
        This allowlist operates in logical `AND` relations to the two allowlists
        above.
      tolerate_debug_op_creation_failures: (`bool`) whether debug op creation
        failures (e.g., due to dtype incompatibility) are to be tolerated by not
        throwing exceptions.
    '''

class NonInteractiveDebugWrapperSession(BaseDebugWrapperSession, metaclass=abc.ABCMeta):
    """Base class for non-interactive (i.e., non-CLI) debug wrapper sessions."""
    def __init__(self, sess, watch_fn: Incomplete | None = None, thread_name_filter: Incomplete | None = None, pass_through_operrors: bool = False) -> None:
        """Constructor of NonInteractiveDebugWrapperSession.

    Args:
      sess: The TensorFlow `Session` object being wrapped.
      watch_fn: (`Callable`) A Callable that maps the fetches and feeds of a
        debugged `Session.run()` call to `WatchOptions.`
        * Args:
          * `fetches`: the fetches to the `Session.run()` call.
          * `feeds`: the feeds to the `Session.run()` call.

        * Returns:
         (`tf_debug.WatchOptions`) An object containing debug options including
           the debug ops to use, the node names, op types and/or tensor data
           types to watch, etc. See the documentation of `tf_debug.WatchOptions`
           for more details.
      thread_name_filter: Regular-expression white list for threads on which the
        wrapper session will be active. See doc of `BaseDebugWrapperSession` for
        more details.
      pass_through_operrors: If true, all captured OpErrors will be
        propagated.  By default this captures all OpErrors.
    Raises:
       TypeError: If a non-None `watch_fn` is specified and it is not callable.
    """
    def on_session_init(self, request):
        """See doc of BaseDebugWrapperSession.on_run_start."""
    @abc.abstractmethod
    def prepare_run_debug_urls(self, fetches, feed_dict):
        """Abstract method to be implemented by concrete subclasses.

    This method prepares the run-specific debug URL(s).

    Args:
      fetches: Same as the `fetches` argument to `Session.run()`
      feed_dict: Same as the `feed_dict` argument to `Session.run()`

    Returns:
      debug_urls: (`str` or `list` of `str`) Debug URLs to be used in
        this `Session.run()` call.
    """
    def on_run_start(self, request):
        """See doc of BaseDebugWrapperSession.on_run_start."""
    def on_run_end(self, request):
        """See doc of BaseDebugWrapperSession.on_run_end."""
