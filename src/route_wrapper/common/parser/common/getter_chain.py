from __future__ import annotations

from abc import ABC, abstractmethod
from inspect import Parameter
from typing import Any, Optional, ClassVar

from route_wrapper.common.introspection import compare_annotated
from route_wrapper.common.parser.common.source import Source

from .getter_chain_request import GetterChainRequest


class GetterChain(ABC):
    """Implements chain of responsiblity pattern"""

    next_getter: Optional[GetterChain]
    source: ClassVar[Source]

    def __init__(self, next_getter: Optional[GetterChain] = None):
        self.next_getter = next_getter

    def compare(self, request: GetterChainRequest) -> bool:
        return compare_annotated(request.annotation, self.source)

    def get_missing(self, request: GetterChainRequest) -> Optional[Any]:
        default = request.arg_default

        if default == Parameter.empty:
            return None

        return default

    @abstractmethod
    async def get(self, request: GetterChainRequest) -> Optional[Any]:
        if not self.next_getter:
            return None

        return await self.next_getter.get(request)
