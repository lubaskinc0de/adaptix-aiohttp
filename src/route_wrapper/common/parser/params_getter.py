from inspect import Parameter
from typing import TypeVar, Any, Optional, Mapping

from .common.getter_chain import GetterChain
from .common.getter_chain_request import GetterChainRequest

from .body_getter import BodyGetterChain
from .query_getter import QueryGetterChain
from .headers_getter import HeadersGetterChain
from .cookies_getter import CookiesGetterChain

from route_wrapper.common import Loader
from route_wrapper.common.route import Route

RequestT = TypeVar("RequestT")


class ParamsGetter:
    def __init__(
        self,
        body_loader: Loader,
        route: Route,
        params: Mapping[str, Parameter],
        getter_chain: Optional[GetterChain] = None,
        params_loader: Optional[Loader] = None,
    ) -> None:
        self.request = route.request
        self.params = params
        self.body_loader = body_loader
        self.getter_chain = getter_chain

        if not self.getter_chain:
            getter_chain = BodyGetterChain(
                CookiesGetterChain(HeadersGetterChain(QueryGetterChain()))
            )

            self.getter_chain = getter_chain

        self.params_loader = params_loader

        if not self.params_loader:
            self.params_loader = body_loader

    async def get_params(self) -> dict[str, Any]:
        params = {}

        for key, value in self.params.items():
            request = GetterChainRequest(
                annotation=value.annotation,
                arg_name=key,
                http_request=self.request,
                body_loader=self.body_loader,
                params_loader=self.params_loader,
                arg_default=value.default,
            )

            arg = await self.getter_chain.get(request)

            if arg:
                params[key] = arg

        return params
