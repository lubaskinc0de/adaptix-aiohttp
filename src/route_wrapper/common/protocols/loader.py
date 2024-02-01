from typing import Protocol, TypeVar, Type, Any
from abc import abstractmethod

T = TypeVar("T")


class Loader(Protocol):
    @abstractmethod
    def load(self, data: Any, tp: Type[T]) -> T:
        raise NotImplementedError
