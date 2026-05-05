import typing as t
from ..wrappers.request import Request
from ..wrappers.response import Response
from .console import Console as Console
from .tbtools import DebugFrameSummary as DebugFrameSummary, DebugTraceback as DebugTraceback, render_console_html as render_console_html
from _typeshed import Incomplete
from _typeshed.wsgi import StartResponse, WSGIApplication as WSGIApplication, WSGIEnvironment as WSGIEnvironment

PIN_TIME: Incomplete

def hash_pin(pin: str) -> str: ...
def get_machine_id() -> str | bytes | None: ...

class _ConsoleFrame:
    """Helper class so that we can reuse the frame console code for the
    standalone console.
    """
    console: Incomplete
    id: int
    def __init__(self, namespace: dict[str, t.Any]) -> None: ...
    def eval(self, code: str) -> t.Any: ...

def get_pin_and_cookie_name(app: WSGIApplication) -> tuple[str, str] | tuple[None, None]:
    """Given an application object this returns a semi-stable 9 digit pin
    code and a random key.  The hope is that this is stable between
    restarts to not make debugging particularly frustrating.  If the pin
    was forcefully disabled this returns `None`.

    Second item in the resulting tuple is the cookie name for remembering.
    """

class DebuggedApplication:
    '''Enables debugging support for a given application::

        from werkzeug.debug import DebuggedApplication
        from myapp import app
        app = DebuggedApplication(app, evalex=True)

    The ``evalex`` argument allows evaluating expressions in any frame
    of a traceback. This works by preserving each frame with its local
    state. Some state, such as context globals, cannot be restored with
    the frame by default. When ``evalex`` is enabled,
    ``environ["werkzeug.debug.preserve_context"]`` will be a callable
    that takes a context manager, and can be called multiple times.
    Each context manager will be entered before evaluating code in the
    frame, then exited again, so they can perform setup and cleanup for
    each call.

    :param app: the WSGI application to run debugged.
    :param evalex: enable exception evaluation feature (interactive
                   debugging).  This requires a non-forking server.
    :param request_key: The key that points to the request object in this
                        environment.  This parameter is ignored in current
                        versions.
    :param console_path: the URL for a general purpose console.
    :param console_init_func: the function that is executed before starting
                              the general purpose console.  The return value
                              is used as initial namespace.
    :param show_hidden_frames: by default hidden traceback frames are skipped.
                               You can show them by setting this parameter
                               to `True`.
    :param pin_security: can be used to disable the pin based security system.
    :param pin_logging: enables the logging of the pin system.

    .. versionchanged:: 2.2
        Added the ``werkzeug.debug.preserve_context`` environ key.
    '''
    app: Incomplete
    evalex: Incomplete
    frames: Incomplete
    frame_contexts: Incomplete
    request_key: Incomplete
    console_path: Incomplete
    console_init_func: Incomplete
    show_hidden_frames: Incomplete
    secret: Incomplete
    pin_logging: Incomplete
    def __init__(self, app: WSGIApplication, evalex: bool = False, request_key: str = 'werkzeug.request', console_path: str = '/console', console_init_func: t.Callable[[], dict[str, t.Any]] | None = None, show_hidden_frames: bool = False, pin_security: bool = True, pin_logging: bool = True) -> None: ...
    @property
    def pin(self) -> str | None: ...
    @pin.setter
    def pin(self, value: str) -> None: ...
    @property
    def pin_cookie_name(self) -> str:
        """The name of the pin cookie."""
    def debug_application(self, environ: WSGIEnvironment, start_response: StartResponse) -> t.Iterator[bytes]:
        """Run the application and conserve the traceback frames."""
    def execute_command(self, request: Request, command: str, frame: DebugFrameSummary | _ConsoleFrame) -> Response:
        """Execute a command in a console."""
    def display_console(self, request: Request) -> Response:
        """Display a standalone shell."""
    def get_resource(self, request: Request, filename: str) -> Response:
        """Return a static resource from the shared folder."""
    def check_pin_trust(self, environ: WSGIEnvironment) -> bool | None:
        """Checks if the request passed the pin test.  This returns `True` if the
        request is trusted on a pin/cookie basis and returns `False` if not.
        Additionally if the cookie's stored pin hash is wrong it will return
        `None` so that appropriate action can be taken.
        """
    def pin_auth(self, request: Request) -> Response:
        """Authenticates with the pin."""
    def log_pin_request(self) -> Response:
        """Log the pin if needed."""
    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse) -> t.Iterable[bytes]:
        """Dispatch the requests."""
