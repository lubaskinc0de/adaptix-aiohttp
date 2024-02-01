from typing import Optional, Any

from .common.getter_chain import GetterChain
from .common.source import Source
from .common.getter_chain_request import GetterChainRequest


class QueryGetterChain(GetterChain):
    source = Source.QUERY

    async def get(self, request: GetterChainRequest) -> Optional[Any]:
        if not self.compare(request):
            return await super().get(request)

        query_params = request.http_request.query

        if request.arg_name not in query_params:
            return self.get_missing(request)

        return query_params[request.arg_name]
