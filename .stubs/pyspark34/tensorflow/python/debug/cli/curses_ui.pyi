from _typeshed import Incomplete
from tensorflow.python.debug.cli import base_ui as base_ui, cli_shared as cli_shared, command_parser as command_parser, curses_widgets as curses_widgets, debugger_cli_common as debugger_cli_common, tensor_format as tensor_format

class ScrollBar:
    """Vertical ScrollBar for Curses-based CLI.

  An object of this class has knowledge of the location of the scroll bar
  in the screen coordinates, the current scrolling position, and the total
  number of text lines in the screen text. By using this information, it
  can generate text rendering of the scroll bar, which consists of and UP
  button on the top and a DOWN button on the bottom, in addition to a scroll
  block in between, whose exact location is determined by the scrolling
  position. The object can also calculate the scrolling command (e.g.,
  _SCROLL_UP_A_LINE, _SCROLL_DOWN) from the coordinate of a mouse click
  event in the screen region it occupies.
  """
    BASE_ATTR: Incomplete
    def __init__(self, min_x, min_y, max_x, max_y, scroll_position, output_num_rows) -> None:
        """Constructor of ScrollBar.

    Args:
      min_x: (int) left index of the scroll bar on the screen (inclusive).
      min_y: (int) top index of the scroll bar on the screen (inclusive).
      max_x: (int) right index of the scroll bar on the screen (inclusive).
      max_y: (int) bottom index of the scroll bar on the screen (inclusive).
      scroll_position: (int) 0-based location of the screen output. For example,
        if the screen output is scrolled to the top, the value of
        scroll_position should be 0. If it is scrolled to the bottom, the value
        should be output_num_rows - 1.
      output_num_rows: (int) Total number of output rows.

    Raises:
      ValueError: If the width or height of the scroll bar, as determined
       by min_x, max_x, min_y and max_y, is too small.
    """
    def layout(self):
        """Get the RichTextLines layout of the scroll bar.

    Returns:
      (debugger_cli_common.RichTextLines) The text layout of the scroll bar.
    """
    def get_click_command(self, mouse_y): ...

class CursesUI(base_ui.BaseUI):
    '''Curses-based Command-line UI.

  In this class, the methods with the prefix "_screen_" are the methods that
  interact with the actual terminal using the curses library.
  '''
    CLI_TERMINATOR_KEY: int
    CLI_TAB_KEY: Incomplete
    BACKSPACE_KEY: Incomplete
    REGEX_SEARCH_PREFIX: str
    TENSOR_INDICES_NAVIGATION_PREFIX: str
    CLI_CR_KEYS: Incomplete
    def __init__(self, on_ui_exit: Incomplete | None = None, config: Incomplete | None = None) -> None:
        """Constructor of CursesUI.

    Args:
      on_ui_exit: (Callable) Callback invoked when the UI exits.
      config: An instance of `cli_config.CLIConfig()` carrying user-facing
        configurations.
    """
    def run_ui(self, init_command: Incomplete | None = None, title: Incomplete | None = None, title_color: Incomplete | None = None, enable_mouse_on_start: bool = True):
        """Run the CLI: See the doc of base_ui.BaseUI.run_ui for more details."""
    def get_help(self): ...
