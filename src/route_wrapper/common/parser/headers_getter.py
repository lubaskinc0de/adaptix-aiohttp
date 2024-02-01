from typing import Optional, Any

from .common.getter_chain import GetterChain
from .common.source import Source
from .common.getter_chain_request import GetterChainRequest


class HeadersGetterChain(GetterChain):
    source = Source.HEADERS

    async def get(self, request: GetterChainRequest) -> Optional[Any]:
        if not self.compare(request):
            return await super().get(request)

        headers = request.http_request.headers

        if request.arg_name not in headers:
            return self.get_missing(request)

        return headers[request.arg_name]
