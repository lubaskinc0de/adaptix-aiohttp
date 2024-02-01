from typing import TypeVar, Any, Type

from adaptix import Retort

from route_wrapper.common import Loader

T = TypeVar("T")


class RetortLoader(Loader):
    def __init__(self, retort: Retort):
        self.retort = retort

    def load(self, data: Any, tp: Type[T]) -> T:
        return self.retort.load(data, tp)
