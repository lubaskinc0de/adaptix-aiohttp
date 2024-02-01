from typing import Optional

from .common.getter_chain import GetterChain
from .common.source import Source
from .common.getter_chain_request import GetterChainRequest

from route_wrapper.common import InputModelT


class BodyGetterChain(GetterChain):
    source = Source.BODY

    async def get(self, request: GetterChainRequest) -> Optional[InputModelT]:
        if not self.compare(request):
            return await super().get(request)

        data = await request.http_request.read()
        model = request.body_loader.load(data, request.annotation)

        return model
