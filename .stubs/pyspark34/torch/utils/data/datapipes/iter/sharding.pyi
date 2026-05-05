from _typeshed import Incomplete
from enum import IntEnum
from torch.utils.data.datapipes.datapipe import IterDataPipe

__all__ = ['SHARDING_PRIORITIES', 'ShardingFilterIterDataPipe']

class SHARDING_PRIORITIES(IntEnum):
    DEFAULT: int
    DISTRIBUTED: int
    MULTIPROCESSING: int

class _ShardingIterDataPipe(IterDataPipe):
    def apply_sharding(self, num_of_instances: int, instance_id: int, sharding_group: SHARDING_PRIORITIES): ...

class ShardingFilterIterDataPipe(_ShardingIterDataPipe):
    """
    Wrapper that allows DataPipe to be sharded (functional name: ``sharding_filter``). After ``apply_sharding`` is
    called, each instance of the DataPipe (on different workers) will have every `n`-th element of the
    original DataPipe, where `n` equals to the number of instances.

    Args:
        source_datapipe: Iterable DataPipe that will be sharded
    """
    source_datapipe: Incomplete
    sharding_group_filter: Incomplete
    groups: Incomplete
    num_of_instances: int
    instance_id: int
    def __init__(self, source_datapipe: IterDataPipe, sharding_group_filter: Incomplete | None = None) -> None: ...
    def apply_sharding(self, num_of_instances, instance_id, sharding_group=...) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
