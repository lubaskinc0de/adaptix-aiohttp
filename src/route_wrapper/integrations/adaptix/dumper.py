from typing import Optional, Any, TypeVar

from adaptix import Retort

from route_wrapper.common import MappingDumper

T = TypeVar("T")


class RetortDumper(MappingDumper):
    def __init__(self, retort: Retort):
        self.retort = retort

    def dump(self, data: T, tp: Optional[Any] = None) -> dict[str, Any]:
        return self.retort.dump(data, tp)
