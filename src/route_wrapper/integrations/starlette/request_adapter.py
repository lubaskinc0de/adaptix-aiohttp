from typing import Any

from starlette.requests import Request as StarletteRequest

from src.route_wrapper import (
    Request,
    RequestQuery,
    RequestHeaders,
    RequestCookies,
)


class RequestAdapter(Request):
    def __init__(self, request: StarletteRequest) -> None:
        self.request = request

    async def read(self) -> dict[str, Any]:
        return await self.request.json()

    @property
    def query(self) -> RequestQuery:
        return self.request.query_params

    @property
    def headers(self) -> RequestHeaders:
        return self.request.headers

    @property
    def cookies(self) -> RequestCookies:
        return self.request.cookies
