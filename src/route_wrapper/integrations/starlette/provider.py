from starlette.requests import Request

from typing import (
    TypeVar,
)

from route_wrapper import web_provider
from .request_adapter import RequestAdapter

T = TypeVar("T")


@web_provider(Request)
def starlette_provider(
    request: Request,
):
    request_adapter = RequestAdapter(request)

    return request_adapter
