from _typeshed import Incomplete
from tensorflow.python.debug.cli import cli_config as cli_config, command_parser as command_parser, debugger_cli_common as debugger_cli_common

class BaseUI:
    """Base class of tfdbg user interface."""
    CLI_PROMPT: str
    CLI_EXIT_COMMANDS: Incomplete
    ERROR_MESSAGE_PREFIX: str
    INFO_MESSAGE_PREFIX: str
    def __init__(self, on_ui_exit: Incomplete | None = None, config: Incomplete | None = None) -> None:
        """Constructor of the base class.

    Args:
      on_ui_exit: (`Callable`) the callback to be called when the UI exits.
      config: An instance of `cli_config.CLIConfig()` carrying user-facing
        configurations.
    """
    def set_help_intro(self, help_intro) -> None:
        '''Set an introductory message to the help output of the command registry.

    Args:
      help_intro: (RichTextLines) Rich text lines appended to the beginning of
        the output of the command "help", as introductory information.
    '''
    def register_command_handler(self, prefix, handler, help_info, prefix_aliases: Incomplete | None = None) -> None:
        """A wrapper around CommandHandlerRegistry.register_command_handler().

    In addition to calling the wrapped register_command_handler() method, this
    method also registers the top-level tab-completion context based on the
    command prefixes and their aliases.

    See the doc string of the wrapped method for more details on the args.

    Args:
      prefix: (str) command prefix.
      handler: (callable) command handler.
      help_info: (str) help information.
      prefix_aliases: (list of str) aliases of the command prefix.
    """
    def register_tab_comp_context(self, *args, **kwargs) -> None:
        """Wrapper around TabCompletionRegistry.register_tab_comp_context()."""
    def run_ui(self, init_command: Incomplete | None = None, title: Incomplete | None = None, title_color: Incomplete | None = None, enable_mouse_on_start: bool = True) -> None:
        '''Run the UI until user- or command- triggered exit.

    Args:
      init_command: (str) Optional command to run on CLI start up.
      title: (str) Optional title to display in the CLI.
      title_color: (str) Optional color of the title, e.g., "yellow".
      enable_mouse_on_start: (bool) Whether the mouse mode is to be enabled on
        start-up.

    Returns:
      An exit token of arbitrary type. Can be None.
    '''
    @property
    def config(self):
        """Obtain the CLIConfig of this `BaseUI` instance."""
