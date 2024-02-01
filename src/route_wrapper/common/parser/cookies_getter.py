from typing import Optional, Any

from .common.getter_chain import GetterChain
from .common.source import Source
from .common.getter_chain_request import GetterChainRequest


class CookiesGetterChain(GetterChain):
    source = Source.COOKIES

    async def get(self, request: GetterChainRequest) -> Optional[Any]:
        if not self.compare(request):
            return await super().get(request)

        cookies = request.http_request.cookies

        if request.arg_name not in cookies:
            return self.get_missing(request)

        return cookies[request.arg_name]
