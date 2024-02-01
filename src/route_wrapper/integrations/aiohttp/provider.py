from aiohttp import web

from typing import (
    TypeVar,
)

from src.route_wrapper import web_provider
from route_wrapper.integrations.aiohttp.request_adapter import RequestAdapter

T = TypeVar("T")


@web_provider(web.Request)
def aiohttp_provider(
    request: web.Request,
):
    request_adapter = RequestAdapter(request)

    return request_adapter
