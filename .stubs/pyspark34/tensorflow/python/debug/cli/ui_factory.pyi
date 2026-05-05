from _typeshed import Incomplete

SUPPORTED_UI_TYPES: Incomplete

def get_ui(ui_type, on_ui_exit: Incomplete | None = None, available_ui_types: Incomplete | None = None, config: Incomplete | None = None):
    """Create a `base_ui.BaseUI` subtype.

  This factory method attempts to fallback to other available ui_types on
  ImportError. For example, if `ui_type` is `curses`, but `curses` cannot be
  imported properly, e.g., on Windows, will fallback to `readline`.

  Args:
    ui_type: (`str`) requested UI type. Currently supported:
      (curses | readline)
    on_ui_exit: (`Callable`) the callback to be called when the UI exits.
    available_ui_types: (`None` or `list` of `str`) Manually-set available
      ui_types.
    config: An instance of `cli_config.CLIConfig()` carrying user-facing
      configurations.

  Returns:
    A `base_ui.BaseUI` subtype object.

  Raises:
    ValueError: on invalid ui_type or on exhausting or fallback ui_types.
  """
