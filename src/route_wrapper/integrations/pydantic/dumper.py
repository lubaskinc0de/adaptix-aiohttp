from typing import Optional, Any, TypeVar
from pydantic import BaseModel

from route_wrapper.common import MappingDumper

T = TypeVar("T", bound=BaseModel)


class PydanticDumper(MappingDumper):
    def dump(self, data: T, tp: Optional[Any] = None) -> dict[str, Any]:
        return data.model_dump()
