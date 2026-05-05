from _typeshed import Incomplete
from tensorflow.python.debug.cli import debugger_cli_common as debugger_cli_common
from tensorflow.python.platform import gfile as gfile

RL: Incomplete

class CLIConfig:
    """Client-facing configurations for TFDBG command-line interfaces."""
    def __init__(self, config_file_path: Incomplete | None = None) -> None: ...
    def get(self, property_name): ...
    def set(self, property_name, property_val) -> None:
        """Set the value of a property.

    Supports limitd property value types: `bool`, `int` and `str`.

    Args:
      property_name: Name of the property.
      property_val: Value of the property. If the property has `bool` type and
        this argument has `str` type, the `str` value will be parsed as a `bool`

    Raises:
      ValueError: if a `str` property_value fails to be parsed as a `bool`.
      KeyError: if `property_name` is an invalid property name.
    """
    def set_callback(self, property_name, callback) -> None:
        """Set a set-callback for given property.

    Args:
      property_name: Name of the property.
      callback: The callback as a `callable` of signature:
          def cbk(config):
        where config is the config after it is set to the new value.
        The callback is invoked each time the set() method is called with the
        matching property_name.

    Raises:
      KeyError: If property_name does not exist.
      TypeError: If `callback` is not callable.
    """
    def summarize(self, highlight: Incomplete | None = None):
        """Get a text summary of the config.

    Args:
      highlight: A property name to highlight in the output.

    Returns:
      A `RichTextLines` output.
    """
