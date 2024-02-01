from typing import Any, Protocol, TypeAlias, Mapping
from abc import abstractmethod

RequestBody: TypeAlias = Any
RequestQuery: TypeAlias = Mapping[str, Any]
RequestHeaders: TypeAlias = Mapping[str, str]
RequestCookies: TypeAlias = Mapping[str, str]


class Request(Protocol):
    @abstractmethod
    async def read(self) -> RequestBody:
        raise NotImplementedError

    @property
    @abstractmethod
    def query(self) -> RequestQuery:
        raise NotImplementedError

    @property
    @abstractmethod
    def headers(self) -> RequestHeaders:
        raise NotImplementedError

    @property
    @abstractmethod
    def cookies(self) -> RequestCookies:
        raise NotImplementedError
