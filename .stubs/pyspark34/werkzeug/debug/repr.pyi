import typing as t
from _typeshed import Incomplete

missing: Incomplete
RegexType: Incomplete
HELP_HTML: str
OBJECT_DUMP_HTML: str

def debug_repr(obj: object) -> str:
    """Creates a debug repr of an object as HTML string."""
def dump(obj: object = ...) -> None:
    """Print the object details to stdout._write (for the interactive
    console of the web debugger.
    """

class _Helper:
    """Displays an HTML version of the normal help, for the interactive
    debugger only because it requires a patched sys.stdout.
    """
    def __call__(self, topic: t.Any | None = None) -> None: ...

helper: Incomplete

class DebugReprGenerator:
    def __init__(self) -> None: ...
    list_repr: Incomplete
    tuple_repr: Incomplete
    set_repr: Incomplete
    frozenset_repr: Incomplete
    deque_repr: Incomplete
    def regex_repr(self, obj: t.Pattern) -> str: ...
    def string_repr(self, obj: str | bytes, limit: int = 70) -> str: ...
    def dict_repr(self, d: dict[int, None] | dict[str, int] | dict[str | int, int], recursive: bool, limit: int = 5) -> str: ...
    def object_repr(self, obj: type[dict] | t.Callable | type[list] | None) -> str: ...
    def dispatch_repr(self, obj: t.Any, recursive: bool) -> str: ...
    def fallback_repr(self) -> str: ...
    def repr(self, obj: object) -> str: ...
    def dump_object(self, obj: object) -> str: ...
    def dump_locals(self, d: dict[str, t.Any]) -> str: ...
    def render_object_dump(self, items: list[tuple[str, str]], title: str, repr: str | None = None) -> str: ...
