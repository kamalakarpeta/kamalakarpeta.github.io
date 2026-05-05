from _typeshed import Incomplete

class Interval:
    """Represents an interval between a start and end value."""
    start: Incomplete
    start_included: Incomplete
    end: Incomplete
    end_included: Incomplete
    def __init__(self, start, start_included, end, end_included) -> None: ...
    def contains(self, value): ...
    def __eq__(self, other): ...

def parse_command(command):
    """Parse command string into a list of arguments.

  - Disregards whitespace inside double quotes and brackets.
  - Strips paired leading and trailing double quotes in arguments.
  - Splits the command at whitespace.

  Nested double quotes and brackets are not handled.

  Args:
    command: (str) Input command.

  Returns:
    (list of str) List of arguments.
  """
def extract_output_file_path(args):
    '''Extract output file path from command arguments.

  Args:
    args: (list of str) command arguments.

  Returns:
    (list of str) Command arguments with the output file path part stripped.
    (str or None) Output file path (if any).

  Raises:
    SyntaxError: If there is no file path after the last ">" character.
  '''
def parse_tensor_name_with_slicing(in_str):
    '''Parse tensor name, potentially suffixed by slicing string.

  Args:
    in_str: (str) Input name of the tensor, potentially followed by a slicing
      string. E.g.: Without slicing string: "hidden/weights/Variable:0", with
      slicing string: "hidden/weights/Variable:0[1, :]"

  Returns:
    (str) name of the tensor
    (str) slicing string, if any. If no slicing string is present, return "".
  '''
def validate_slicing_string(slicing_string):
    """Validate a slicing string.

  Check if the input string contains only brackets, digits, commas and
  colons that are valid characters in numpy-style array slicing.

  Args:
    slicing_string: (str) Input slicing string to be validated.

  Returns:
    (bool) True if and only if the slicing string is valid.
  """
def parse_indices(indices_string):
    '''Parse a string representing indices.

  For example, if the input is "[1, 2, 3]", the return value will be a list of
  indices: [1, 2, 3]

  Args:
    indices_string: (str) a string representing indices. Can optionally be
      surrounded by a pair of brackets.

  Returns:
    (list of int): Parsed indices.
  '''
def parse_ranges(range_string):
    '''Parse a string representing numerical range(s).

  Args:
    range_string: (str) A string representing a numerical range or a list of
      them. For example:
        "[-1.0,1.0]", "[-inf, 0]", "[[-inf, -1.0], [1.0, inf]]"

  Returns:
    (list of list of float) A list of numerical ranges parsed from the input
      string.

  Raises:
    ValueError: If the input doesn\'t represent a range or a list of ranges.
  '''
def parse_memory_interval(interval_str):
    '''Convert a human-readable memory interval to a tuple of start and end value.

  Args:
    interval_str: (`str`) A human-readable str representing an interval
      (e.g., "[10kB, 20kB]", "<100M", ">100G"). Only the units "kB", "MB", "GB"
      are supported. The "B character at the end of the input `str` may be
      omitted.

  Returns:
    `Interval` object where start and end are in bytes.

  Raises:
    ValueError: if the input is not valid.
  '''
def parse_time_interval(interval_str):
    '''Convert a human-readable time interval to a tuple of start and end value.

  Args:
    interval_str: (`str`) A human-readable str representing an interval
      (e.g., "[10us, 20us]", "<100s", ">100ms"). Supported time suffixes are
      us, ms, s.

  Returns:
    `Interval` object where start and end are in microseconds.

  Raises:
    ValueError: if the input is not valid.
  '''
def parse_readable_size_str(size_str):
    '''Convert a human-readable str representation to number of bytes.

  Only the units "kB", "MB", "GB" are supported. The "B character at the end
  of the input `str` may be omitted.

  Args:
    size_str: (`str`) A human-readable str representing a number of bytes
      (e.g., "0", "1023", "1.1kB", "24 MB", "23GB", "100 G".

  Returns:
    (`int`) The parsed number of bytes.

  Raises:
    ValueError: on failure to parse the input `size_str`.
  '''
def parse_readable_time_str(time_str):
    """Parses a time string in the format N, Nus, Nms, Ns.

  Args:
    time_str: (`str`) string consisting of an integer time value optionally
      followed by 'us', 'ms', or 's' suffix. If suffix is not specified,
      value is assumed to be in microseconds. (e.g. 100us, 8ms, 5s, 100).

  Returns:
    Microseconds value.
  """
def evaluate_tensor_slice(tensor, tensor_slicing):
    '''Call eval on the slicing of a tensor, with validation.

  Args:
    tensor: (numpy ndarray) The tensor value.
    tensor_slicing: (str or None) Slicing of the tensor, e.g., "[:, 1]". If
      None, no slicing will be performed on the tensor.

  Returns:
    (numpy ndarray) The sliced tensor.

  Raises:
    ValueError: If tensor_slicing is not a valid numpy ndarray slicing str.
  '''
def get_print_tensor_argparser(description):
    """Get an ArgumentParser for a command that prints tensor values.

  Examples of such commands include print_tensor and print_feed.

  Args:
    description: Description of the ArgumentParser.

  Returns:
    An instance of argparse.ArgumentParser.
  """
