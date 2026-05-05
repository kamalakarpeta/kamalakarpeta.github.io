from tensorflow.python.debug.lib import debug_data as debug_data

class ExpressionEvaluator:
    """Evaluates Python expressions using debug tensor values from a dump."""
    def __init__(self, dump) -> None:
        """Constructor of ExpressionEvaluator.

    Args:
      dump: an instance of `DebugDumpDir`.
    """
    def evaluate(self, expression):
        """Parse an expression.

    Args:
      expression: the expression to be parsed.

    Returns:
      The result of the evaluation.

    Raises:
      ValueError: If the value of one or more of the debug tensors in the
        expression are not available.
    """
