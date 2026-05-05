from _typeshed import Incomplete
from tensorflow.python.client import pywrap_tf_session as pywrap_tf_session
from tensorflow.python.platform import gfile as gfile

HELP_INDENT: str
EXPLICIT_USER_EXIT: str
REGEX_MATCH_LINES_KEY: str
INIT_SCROLL_POS_KEY: str
MAIN_MENU_KEY: str

class CommandLineExit(Exception):
    def __init__(self, exit_token: Incomplete | None = None) -> None: ...
    @property
    def exit_token(self): ...

class RichLine:
    """Rich single-line text.

  Attributes:
    text: A plain string, the raw text represented by this object.  Should not
      contain newlines.
    font_attr_segs: A list of (start, end, font attribute) triples, representing
      richness information applied to substrings of text.
  """
    text: Incomplete
    font_attr_segs: Incomplete
    def __init__(self, text: str = '', font_attr: Incomplete | None = None) -> None:
        """Construct a RichLine with no rich attributes or a single attribute.

    Args:
      text: Raw text string
      font_attr: If specified, a single font attribute to be applied to the
        entire text.  Extending this object via concatenation allows creation
        of text with varying attributes.
    """
    def __add__(self, other):
        """Concatenate two chunks of maybe rich text to make a longer rich line.

    Does not modify self.

    Args:
      other: Another piece of text to concatenate with this one.
        If it is a plain str, it will be appended to this string with no
        attributes.  If it is a RichLine, it will be appended to this string
        with its attributes preserved.

    Returns:
      A new RichLine comprising both chunks of text, with appropriate
        attributes applied to the corresponding substrings.
    """
    def __len__(self) -> int: ...

def rich_text_lines_from_rich_line_list(rich_text_list, annotations: Incomplete | None = None):
    """Convert a list of RichLine objects or strings to a RichTextLines object.

  Args:
    rich_text_list: a list of RichLine objects or strings
    annotations: annotations for the resultant RichTextLines object.

  Returns:
    A corresponding RichTextLines object.
  """
def get_tensorflow_version_lines(include_dependency_versions: bool = False):
    """Generate RichTextLines with TensorFlow version info.

  Args:
    include_dependency_versions: Include the version of TensorFlow's key
      dependencies, such as numpy.

  Returns:
    A formatted, multi-line `RichTextLines` object.
  """

class RichTextLines:
    """Rich multi-line text.

  Line-by-line text output, with font attributes (e.g., color) and annotations
  (e.g., indices in a multi-dimensional tensor). Used as the text output of CLI
  commands. Can be rendered on terminal environments such as curses.

  This is not to be confused with Rich Text Format (RTF). This class is for text
  lines only.
  """
    def __init__(self, lines, font_attr_segs: Incomplete | None = None, annotations: Incomplete | None = None) -> None:
        '''Constructor of RichTextLines.

    Args:
      lines: A list of str or a single str, representing text output to
        screen. The latter case is for convenience when the text output is
        single-line.
      font_attr_segs: A map from 0-based row index to a list of 3-tuples.
        It lists segments in each row that have special font attributes, such
        as colors, that are not the default attribute. For example:
        {1: [(0, 3, "red"), (4, 7, "green")], 2: [(10, 20, "yellow")]}

        In each tuple, the 1st element is the start index of the segment. The
        2nd element is the end index, in an "open interval" fashion. The 3rd
        element is an object or a list of objects that represents the font
        attribute. Colors are represented as strings as in the examples above.
      annotations: A map from 0-based row index to any object for annotating
        the row. A typical use example is annotating rows of the output as
        indices in a multi-dimensional tensor. For example, consider the
        following text representation of a 3x2x2 tensor:
          [[[0, 0], [0, 0]],
           [[0, 0], [0, 0]],
           [[0, 0], [0, 0]]]
        The annotation can indicate the indices of the first element shown in
        each row, i.e.,
          {0: [0, 0, 0], 1: [1, 0, 0], 2: [2, 0, 0]}
        This information can make display of tensors on screen clearer and can
        help the user navigate (scroll) to the desired location in a large
        tensor.

    Raises:
      ValueError: If lines is of invalid type.
    '''
    @property
    def lines(self): ...
    @property
    def font_attr_segs(self): ...
    @property
    def annotations(self): ...
    def num_lines(self): ...
    def slice(self, begin, end):
        """Slice a RichTextLines object.

    The object itself is not changed. A sliced instance is returned.

    Args:
      begin: (int) Beginning line index (inclusive). Must be >= 0.
      end: (int) Ending line index (exclusive). Must be >= 0.

    Returns:
      (RichTextLines) Sliced output instance of RichTextLines.

    Raises:
      ValueError: If begin or end is negative.
    """
    def extend(self, other) -> None:
        '''Extend this instance of RichTextLines with another instance.

    The extension takes effect on the text lines, the font attribute segments,
    as well as the annotations. The line indices in the font attribute
    segments and the annotations are adjusted to account for the existing
    lines. If there are duplicate, non-line-index fields in the annotations,
    the value from the input argument "other" will override that in this
    instance.

    Args:
      other: (RichTextLines) The other RichTextLines instance to be appended at
        the end of this instance.
    '''
    def append(self, line, font_attr_segs: Incomplete | None = None) -> None:
        """Append a single line of text.

    Args:
      line: (str) The text to be added to the end.
      font_attr_segs: (list of tuples) Font attribute segments of the appended
        line.
    """
    def append_rich_line(self, rich_line) -> None: ...
    def prepend(self, line, font_attr_segs: Incomplete | None = None) -> None:
        """Prepend (i.e., add to the front) a single line of text.

    Args:
      line: (str) The text to be added to the front.
      font_attr_segs: (list of tuples) Font attribute segments of the appended
        line.
    """
    def write_to_file(self, file_path) -> None:
        """Write the object itself to file, in a plain format.

    The font_attr_segs and annotations are ignored.

    Args:
      file_path: (str) path of the file to write to.
    """

def regex_find(orig_screen_output, regex, font_attr):
    """Perform regex match in rich text lines.

  Produces a new RichTextLines object with font_attr_segs containing highlighted
  regex matches.

  Example use cases include:
  1) search for specific items in a large list of items, and
  2) search for specific numerical values in a large tensor.

  Args:
    orig_screen_output: The original RichTextLines, in which the regex find
      is to be performed.
    regex: The regex used for matching.
    font_attr: Font attribute used for highlighting the found result.

  Returns:
    A modified copy of orig_screen_output.

  Raises:
    ValueError: If input str regex is not a valid regular expression.
  """
def wrap_rich_text_lines(inp, cols):
    """Wrap RichTextLines according to maximum number of columns.

  Produces a new RichTextLines object with the text lines, font_attr_segs and
  annotations properly wrapped. This ought to be used sparingly, as in most
  cases, command handlers producing RichTextLines outputs should know the
  screen/panel width via the screen_info kwarg and should produce properly
  length-limited lines in the output accordingly.

  Args:
    inp: Input RichTextLines object.
    cols: Number of columns, as an int.

  Returns:
    1) A new instance of RichTextLines, with line lengths limited to cols.
    2) A list of new (wrapped) line index. For example, if the original input
      consists of three lines and only the second line is wrapped, and it's
      wrapped into two lines, this return value will be: [0, 1, 3].
  Raises:
    ValueError: If inputs have invalid types.
  """

class CommandHandlerRegistry:
    '''Registry of command handlers for CLI.

  Handler methods (callables) for user commands can be registered with this
  class, which then is able to dispatch commands to the correct handlers and
  retrieve the RichTextLines output.

  For example, suppose you have the following handler defined:
    def echo(argv, screen_info=None):
      return RichTextLines(["arguments = %s" % " ".join(argv),
                            "screen_info = " + repr(screen_info)])

  you can register the handler with the command prefix "echo" and alias "e":
    registry = CommandHandlerRegistry()
    registry.register_command_handler("echo", echo,
        "Echo arguments, along with screen info", prefix_aliases=["e"])

  then to invoke this command handler with some arguments and screen_info, do:
    registry.dispatch_command("echo", ["foo", "bar"], screen_info={"cols": 80})

  or with the prefix alias:
    registry.dispatch_command("e", ["foo", "bar"], screen_info={"cols": 80})

  The call will return a RichTextLines object which can be rendered by a CLI.
  '''
    HELP_COMMAND: str
    HELP_COMMAND_ALIASES: Incomplete
    VERSION_COMMAND: str
    VERSION_COMMAND_ALIASES: Incomplete
    def __init__(self) -> None: ...
    def register_command_handler(self, prefix, handler, help_info, prefix_aliases: Incomplete | None = None) -> None:
        '''Register a callable as a command handler.

    Args:
      prefix: Command prefix, i.e., the first word in a command, e.g.,
        "print" as in "print tensor_1".
      handler: A callable of the following signature:
          foo_handler(argv, screen_info=None),
        where argv is the argument vector (excluding the command prefix) and
          screen_info is a dictionary containing information about the screen,
          such as number of columns, e.g., {"cols": 100}.
        The callable should return:
          1) a RichTextLines object representing the screen output.

        The callable can also raise an exception of the type CommandLineExit,
        which if caught by the command-line interface, will lead to its exit.
        The exception can optionally carry an exit token of arbitrary type.
      help_info: A help string.
      prefix_aliases: Aliases for the command prefix, as a list of str. E.g.,
        shorthands for the command prefix: ["p", "pr"]

    Raises:
      ValueError: If
        1) the prefix is empty, or
        2) handler is not callable, or
        3) a handler is already registered for the prefix, or
        4) elements in prefix_aliases clash with existing aliases.
        5) help_info is not a str.
    '''
    def dispatch_command(self, prefix, argv, screen_info: Incomplete | None = None):
        '''Handles a command by dispatching it to a registered command handler.

    Args:
      prefix: Command prefix, as a str, e.g., "print".
      argv: Command argument vector, excluding the command prefix, represented
        as a list of str, e.g.,
        ["tensor_1"]
      screen_info: A dictionary containing screen info, e.g., {"cols": 100}.

    Returns:
      An instance of RichTextLines or None. If any exception is caught during
      the invocation of the command handler, the RichTextLines will wrap the
      error type and message.

    Raises:
      ValueError: If
        1) prefix is empty, or
        2) no command handler is registered for the command prefix, or
        3) the handler is found for the prefix, but it fails to return a
          RichTextLines or raise any exception.
      CommandLineExit:
        If the command handler raises this type of exception, this method will
        simply pass it along.
    '''
    def is_registered(self, prefix):
        """Test if a command prefix or its alias is has a registered handler.

    Args:
      prefix: A prefix or its alias, as a str.

    Returns:
      True iff a handler is registered for prefix.
    """
    def get_help(self, cmd_prefix: Incomplete | None = None):
        """Compile help information into a RichTextLines object.

    Args:
      cmd_prefix: Optional command prefix. As the prefix itself or one of its
        aliases.

    Returns:
      A RichTextLines object containing the help information. If cmd_prefix
      is None, the return value will be the full command-line help. Otherwise,
      it will be the help information for the specified command.
    """
    def set_help_intro(self, help_intro) -> None:
        '''Set an introductory message to help output.

    Args:
      help_intro: (RichTextLines) Rich text lines appended to the
        beginning of the output of the command "help", as introductory
        information.
    '''

class TabCompletionRegistry:
    """Registry for tab completion responses."""
    def __init__(self) -> None: ...
    def register_tab_comp_context(self, context_words, comp_items) -> None:
        '''Register a tab-completion context.

    Register that, for each word in context_words, the potential tab-completions
    are the words in comp_items.

    A context word is a pre-existing, completed word in the command line that
    determines how tab-completion works for another, incomplete word in the same
    command line.
    Completion items consist of potential candidates for the incomplete word.

    To give a general example, a context word can be "drink", and the completion
    items can be ["coffee", "tea", "water"]

    Note: A context word can be empty, in which case the context is for the
     top-level commands.

    Args:
      context_words: A list of context words belonging to the context being
        registered. It is a list of str, instead of a single string, to support
        synonym words triggering the same tab-completion context, e.g.,
        both "drink" and the short-hand "dr" can trigger the same context.
      comp_items: A list of completion items, as a list of str.

    Raises:
      TypeError: if the input arguments are not all of the correct types.
    '''
    def deregister_context(self, context_words) -> None:
        """Deregister a list of context words.

    Args:
      context_words: A list of context words to deregister, as a list of str.

    Raises:
      KeyError: if there are word(s) in context_words that do not correspond
        to any registered contexts.
    """
    def extend_comp_items(self, context_word, new_comp_items) -> None:
        """Add a list of completion items to a completion context.

    Args:
      context_word: A single completion word as a string. The extension will
        also apply to all other context words of the same context.
      new_comp_items: (list of str) New completion items to add.

    Raises:
      KeyError: if the context word has not been registered.
    """
    def remove_comp_items(self, context_word, comp_items) -> None:
        """Remove a list of completion items from a completion context.

    Args:
      context_word: A single completion word as a string. The removal will
        also apply to all other context words of the same context.
      comp_items: Completion items to remove.

    Raises:
      KeyError: if the context word has not been registered.
    """
    def get_completions(self, context_word, prefix):
        """Get the tab completions given a context word and a prefix.

    Args:
      context_word: The context word.
      prefix: The prefix of the incomplete word.

    Returns:
      (1) None if no registered context matches the context_word.
          A list of str for the matching completion items. Can be an empty list
          of a matching context exists, but no completion item matches the
          prefix.
      (2) Common prefix of all the words in the first return value. If the
          first return value is None, this return value will be None, too. If
          the first return value is not None, i.e., a list, this return value
          will be a str, which can be an empty str if there is no common
          prefix among the items of the list.
    """

class CommandHistory:
    """Keeps command history and supports lookup."""
    def __init__(self, limit: int = 100, history_file_path: Incomplete | None = None) -> None:
        """CommandHistory constructor.

    Args:
      limit: Maximum number of the most recent commands that this instance
        keeps track of, as an int.
      history_file_path: (str) Manually specified path to history file. Used in
        testing.
    """
    def add_command(self, command) -> None:
        """Add a command to the command history.

    Args:
      command: The history command, as a str.

    Raises:
      TypeError: if command is not a str.
    """
    def most_recent_n(self, n):
        """Look up the n most recent commands.

    Args:
      n: Number of most recent commands to look up.

    Returns:
      A list of n most recent commands, or all available most recent commands,
      if n exceeds size of the command history, in chronological order.
    """
    def lookup_prefix(self, prefix, n):
        """Look up the n most recent commands that starts with prefix.

    Args:
      prefix: The prefix to lookup.
      n: Number of most recent commands to look up.

    Returns:
      A list of n most recent commands that have the specified prefix, or all
      available most recent commands that have the prefix, if n exceeds the
      number of history commands with the prefix.
    """

class MenuItem:
    """A class for an item in a text-based menu."""
    def __init__(self, caption, content, enabled: bool = True) -> None:
        """Menu constructor.

    TODO(cais): Nested menu is currently not supported. Support it.

    Args:
      caption: (str) caption of the menu item.
      content: Content of the menu item. For a menu item that triggers
        a command, for example, content is the command string.
      enabled: (bool) whether this menu item is enabled.
    """
    @property
    def caption(self): ...
    @property
    def type(self): ...
    @property
    def content(self): ...
    def is_enabled(self): ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...

class Menu:
    """A class for text-based menu."""
    def __init__(self, name: Incomplete | None = None) -> None:
        """Menu constructor.

    Args:
      name: (str or None) name of this menu.
    """
    def append(self, item) -> None:
        """Append an item to the Menu.

    Args:
      item: (MenuItem) the item to be appended.
    """
    def insert(self, index, item) -> None: ...
    def num_items(self): ...
    def captions(self): ...
    def caption_to_item(self, caption):
        """Get a MenuItem from the caption.

    Args:
      caption: (str) The caption to look up.

    Returns:
      (MenuItem) The first-match menu item with the caption, if any.

    Raises:
      LookupError: If a menu item with the caption does not exist.
    """
    def format_as_single_line(self, prefix: Incomplete | None = None, divider: str = ' | ', enabled_item_attrs: Incomplete | None = None, disabled_item_attrs: Incomplete | None = None):
        '''Format the menu as a single-line RichTextLines object.

    Args:
      prefix: (str) String added to the beginning of the line.
      divider: (str) The dividing string between the menu items.
      enabled_item_attrs: (list or str) Attributes applied to each enabled
        menu item, e.g., ["bold", "underline"].
      disabled_item_attrs: (list or str) Attributes applied to each
        disabled menu item, e.g., ["red"].

    Returns:
      (RichTextLines) A single-line output representing the menu, with
        font_attr_segs marking the individual menu items.
    '''
