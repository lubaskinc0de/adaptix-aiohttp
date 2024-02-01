from typing import Any

from fastapi import Request as FastapiRequest

from route_wrapper.common import (
    Request,
    RequestQuery,
    RequestHeaders,
    RequestCookies,
)


class RequestAdapter(Request):
    def __init__(self, request: FastapiRequest) -> None:
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
