from _typeshed import Incomplete
from tensorflow.python.debug.cli import base_ui as base_ui, debugger_cli_common as debugger_cli_common

class ReadlineUI(base_ui.BaseUI):
    """Readline-based Command-line UI."""
    def __init__(self, on_ui_exit: Incomplete | None = None, config: Incomplete | None = None) -> None: ...
    def run_ui(self, init_command: Incomplete | None = None, title: Incomplete | None = None, title_color: Incomplete | None = None, enable_mouse_on_start: bool = True):
        """Run the CLI: See the doc of base_ui.BaseUI.run_ui for more details."""
