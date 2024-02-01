from typing import Any

from aiohttp import web

from src.route_wrapper import (
    Request,
    RequestQuery,
    RequestHeaders,
    RequestCookies,
)


class RequestAdapter(Request):
    def __init__(self, aiohttp_request: web.Request) -> None:
        self.aiohttp_request = aiohttp_request

    async def read(self) -> dict[str, Any]:
        return await self.aiohttp_request.json()

    @property
    def query(self) -> RequestQuery:
        return self.aiohttp_request.query

    @property
    def headers(self) -> RequestHeaders:
        return self.aiohttp_request.headers

    @property
    def cookies(self) -> RequestCookies:
        return self.aiohttp_request.cookies
