from typing import Protocol, TypeVar, Any, Optional
from abc import abstractmethod

T = TypeVar("T")


class Dumper(Protocol):
    @abstractmethod
    def dump(self, data: T, tp: Optional[Any] = None) -> Any:
        raise NotImplementedError


class MappingDumper(Dumper):
    @abstractmethod
    def dump(self, data: T, tp: Optional[Any] = None) -> dict[str, Any]:
        raise NotImplementedError
