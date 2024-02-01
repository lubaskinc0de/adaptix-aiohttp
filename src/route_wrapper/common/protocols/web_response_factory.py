from abc import abstractmethod
from typing import Protocol, Any

from .dumper import Dumper
from .models import OutputModelT


class WebResponseFactory(Protocol):
    dumper: Dumper

    @abstractmethod
    async def __call__(self, output: OutputModelT) -> Any:
        raise NotImplementedError
