from _typeshed import Incomplete
from torch.utils.data.datapipes.datapipe import IterDataPipe
from typing import Callable, Iterator, TypeVar

__all__ = ['FilterIterDataPipe']

T = TypeVar('T')
T_co = TypeVar('T_co', covariant=True)

class FilterIterDataPipe(IterDataPipe[T_co]):
    """
    Filters out elements from the source datapipe according to input ``filter_fn`` (functional name: ``filter``).

    Args:
        datapipe: Iterable DataPipe being filtered
        filter_fn: Customized function mapping an element to a boolean.
        input_col: Index or indices of data which ``filter_fn`` is applied, such as:

            - ``None`` as default to apply ``filter_fn`` to the data directly.
            - Integer(s) is used for list/tuple.
            - Key(s) is used for dict.

    Example:
        >>> # xdoctest: +SKIP
        >>> from torchdata.datapipes.iter import IterableWrapper
        >>> def is_even(n):
        ...     return n % 2 == 0
        >>> dp = IterableWrapper(range(5))
        >>> filter_dp = dp.filter(filter_fn=is_even)
        >>> list(filter_dp)
        [0, 2, 4]
    """
    datapipe: IterDataPipe[T_co]
    filter_fn: Callable
    input_col: Incomplete
    def __init__(self, datapipe: IterDataPipe[T_co], filter_fn: Callable, input_col: Incomplete | None = None) -> None: ...
    def __iter__(self) -> Iterator[T_co]: ...
