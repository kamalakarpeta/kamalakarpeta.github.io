from .interfaces import Asset as Asset
from _typeshed import Incomplete
from typing import Iterator, Type

class AssetRegistry:
    def __init__(self) -> None: ...
    def register(self, asset: Type[Asset]) -> Type[Asset]: ...
    def __iter__(self) -> Iterator[Type[Asset]]: ...

asset_registry: Incomplete
