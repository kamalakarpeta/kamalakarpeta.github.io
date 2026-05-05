from _typeshed import Incomplete
from tensorflow.python.debug.cli import debugger_cli_common as debugger_cli_common

RL: Incomplete

class NavigationHistoryItem:
    """Individual item in navigation history."""
    command: Incomplete
    screen_output: Incomplete
    scroll_position: Incomplete
    def __init__(self, command, screen_output, scroll_position) -> None:
        """Constructor of NavigationHistoryItem.

    Args:
      command: (`str`) the command line text.
      screen_output: the screen output of the command.
      scroll_position: (`int`) scroll position in the screen output.
    """

class CursesNavigationHistory:
    """Navigation history containing commands, outputs and scroll info."""
    BACK_ARROW_TEXT: str
    FORWARD_ARROW_TEXT: str
    def __init__(self, capacity) -> None:
        """Constructor of CursesNavigationHistory.

    Args:
      capacity: (`int`) How many items this object can hold. Each item consists
        of a command stirng, an output RichTextLines object and a scroll
        position.

    Raises:
      ValueError: If capacity is not a positive number.
    """
    def add_item(self, command, screen_output, scroll_position) -> None:
        """Add an item to the navigation histoyr.

    Args:
      command: command line text.
      screen_output: screen output produced for the command.
      scroll_position: (`int`) scroll position in the screen output.
    """
    def update_scroll_position(self, new_scroll_position) -> None:
        """Update the scroll position of the currently-pointed-to history item.

    Args:
      new_scroll_position: (`int`) new scroll-position value.

    Raises:
      ValueError: If the history is empty.
    """
    def size(self): ...
    def pointer(self): ...
    def go_back(self):
        """Go back one place in the history, if possible.

    Decrease the pointer value by 1, if possible. Otherwise, the pointer value
    will be unchanged.

    Returns:
      The updated pointer value.

    Raises:
      ValueError: If history is empty.
    """
    def go_forward(self):
        """Go forward one place in the history, if possible.

    Increase the pointer value by 1, if possible. Otherwise, the pointer value
    will be unchanged.

    Returns:
      The updated pointer value.

    Raises:
      ValueError: If history is empty.
    """
    def can_go_back(self):
        """Test whether client can go back one place.

    Returns:
      (`bool`) Whether going back one place is possible.
    """
    def can_go_forward(self):
        """Test whether client can go forward one place.

    Returns:
      (`bool`) Whether going back one place is possible.
    """
    def render(self, max_length, backward_command, forward_command, latest_command_attribute: str = 'black_on_white', old_command_attribute: str = 'magenta_on_white'):
        """Render the rich text content of the single-line navigation bar.

    Args:
      max_length: (`int`) Maximum length of the navigation bar, in characters.
      backward_command: (`str`) command for going backward. Used to construct
        the shortcut menu item.
      forward_command: (`str`) command for going forward. Used to construct the
        shortcut menu item.
       latest_command_attribute: font attribute for latest command.
       old_command_attribute: font attribute for old (non-latest) command.

    Returns:
      (`debugger_cli_common.RichTextLines`) the navigation bar text with
        attributes.
    """
