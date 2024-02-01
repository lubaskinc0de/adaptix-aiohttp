from typing import Annotated, TypeVar

from route_wrapper.common import InputModelT
from route_wrapper.common import Source

ArgT = TypeVar("ArgT")

FromBody = Annotated[InputModelT, Source.BODY]
FromQuery = Annotated[ArgT, Source.QUERY]
FromHeaders = Annotated[ArgT, Source.HEADERS]
FromPath = Annotated[ArgT, Source.PATH]
FromCookie = Annotated[ArgT, Source.COOKIES]
