from _typeshed import Incomplete
from torch.utils.data.datapipes.datapipe import IterDataPipe
from typing import Tuple

__all__ = ['StreamReaderIterDataPipe']

class StreamReaderIterDataPipe(IterDataPipe[Tuple[str, bytes]]):
    '''
    Given IO streams and their label names, yields bytes with label
    name in a tuple (functional name: ``read_from_stream``).

    Args:
        datapipe: Iterable DataPipe provides label/URL and byte stream
        chunk: Number of bytes to be read from stream per iteration.
            If ``None``, all bytes will be read until the EOF.

    Example:
        >>> # xdoctest: +SKIP
        >>> from torchdata.datapipes.iter import IterableWrapper, StreamReader
        >>> from io import StringIO
        >>> dp = IterableWrapper([("alphabet", StringIO("abcde"))])
        >>> list(StreamReader(dp, chunk=1))
        [(\'alphabet\', \'a\'), (\'alphabet\', \'b\'), (\'alphabet\', \'c\'), (\'alphabet\', \'d\'), (\'alphabet\', \'e\')]
    '''
    datapipe: Incomplete
    chunk: Incomplete
    def __init__(self, datapipe, chunk: Incomplete | None = None) -> None: ...
    def __iter__(self): ...
