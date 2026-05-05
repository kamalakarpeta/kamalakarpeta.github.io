from _typeshed import Incomplete
from tensorflow.python.debug.cli import debugger_cli_common as debugger_cli_common
from tensorflow.python.debug.lib import debug_data as debug_data

BEGIN_INDICES_KEY: str
OMITTED_INDICES_KEY: str
DEFAULT_TENSOR_ELEMENT_HIGHLIGHT_FONT_ATTR: str

class HighlightOptions:
    """Options for highlighting elements of a tensor."""
    criterion: Incomplete
    description: Incomplete
    font_attr: Incomplete
    def __init__(self, criterion, description: Incomplete | None = None, font_attr=...) -> None:
        """Constructor of HighlightOptions.

    Args:
      criterion: (callable) A callable of the following signature:
        def to_highlight(X):
          # Args:
          #   X: The tensor to highlight elements in.
          #
          # Returns:
          #   (boolean ndarray) A boolean ndarray of the same shape as X
          #   indicating which elements are to be highlighted (iff True).
        This callable will be used as the argument of np.argwhere() to
        determine which elements of the tensor are to be highlighted.
      description: (str) Description of the highlight criterion embodied by
        criterion.
      font_attr: (str) Font attribute to be applied to the
        highlighted elements.

    """

def format_tensor(tensor, tensor_label, include_metadata: bool = False, auxiliary_message: Incomplete | None = None, include_numeric_summary: bool = False, np_printoptions: Incomplete | None = None, highlight_options: Incomplete | None = None):
    """Generate a RichTextLines object showing a tensor in formatted style.

  Args:
    tensor: The tensor to be displayed, as a numpy ndarray or other
      appropriate format (e.g., None representing uninitialized tensors).
    tensor_label: A label for the tensor, as a string. If set to None, will
      suppress the tensor name line in the return value.
    include_metadata: Whether metadata such as dtype and shape are to be
      included in the formatted text.
    auxiliary_message: An auxiliary message to display under the tensor label,
      dtype and shape information lines.
    include_numeric_summary: Whether a text summary of the numeric values (if
      applicable) will be included.
    np_printoptions: A dictionary of keyword arguments that are passed to a
      call of np.set_printoptions() to set the text format for display numpy
      ndarrays.
    highlight_options: (HighlightOptions) options for highlighting elements
      of the tensor.

  Returns:
    A RichTextLines object. Its annotation field has line-by-line markups to
    indicate which indices in the array the first element of each line
    corresponds to.
  """
def locate_tensor_element(formatted, indices):
    '''Locate a tensor element in formatted text lines, given element indices.

  Given a RichTextLines object representing a tensor and indices of the sought
  element, return the row number at which the element is located (if exists).

  Args:
    formatted: A RichTextLines object containing formatted text lines
      representing the tensor.
    indices: Indices of the sought element, as a list of int or a list of list
      of int. The former case is for a single set of indices to look up,
      whereas the latter case is for looking up a batch of indices sets at once.
      In the latter case, the indices must be in ascending order, or a
      ValueError will be raised.

  Returns:
    1) A boolean indicating whether the element falls into an omitted line.
    2) Row index.
    3) Column start index, i.e., the first column in which the representation
       of the specified tensor starts, if it can be determined. If it cannot
       be determined (e.g., due to ellipsis), None.
    4) Column end index, i.e., the column right after the last column that
       represents the specified tensor. Iff it cannot be determined, None.

  For return values described above are based on a single set of indices to
    look up. In the case of batch mode (multiple sets of indices), the return
    values will be lists of the types described above.

  Raises:
    AttributeError: If:
      Input argument "formatted" does not have the required annotations.
    ValueError: If:
      1) Indices do not match the dimensions of the tensor, or
      2) Indices exceed sizes of the tensor, or
      3) Indices contain negative value(s).
      4) If in batch mode, and if not all sets of indices are in ascending
         order.
  '''
def numeric_summary(tensor):
    """Get a text summary of a numeric tensor.

  This summary is only available for numeric (int*, float*, complex*) and
  Boolean tensors.

  Args:
    tensor: (`numpy.ndarray`) the tensor value object to be summarized.

  Returns:
    The summary text as a `RichTextLines` object. If the type of `tensor` is not
    numeric or Boolean, a single-line `RichTextLines` object containing a
    warning message will reflect that.
  """
