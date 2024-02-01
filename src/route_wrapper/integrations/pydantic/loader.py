from typing import TypeVar, Any, Type

from pydantic import BaseModel

from src.route_wrapper import Loader

T = TypeVar("T", bound=BaseModel)


class PydanticLoader(Loader):
    def load(self, data: Any, tp: Type[T]) -> T:
        return tp(**data)
