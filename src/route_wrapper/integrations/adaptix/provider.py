from adaptix import Retort
from typing import (
    TypeVar,
)

from route_wrapper.common.parser import ParamsGetter
from route_wrapper.common import OutputModelT

from route_wrapper import Route
from route_wrapper import RouteWrapper

from route_wrapper.integrations.adaptix.loader import (
    RetortLoader,
)

T = TypeVar("T")


async def adaptix_provider(
    route: Route,
    retort: Retort,
) -> OutputModelT:
    loader = RetortLoader(retort)

    params_retort = retort.replace(strict_coercion=False)
    params_loader = RetortLoader(params_retort)

    params_getter = ParamsGetter(
        loader, route, params_loader=params_loader, params=route.source_params
    )

    internal_wrapper = RouteWrapper(
        route=route,
        params_getter=params_getter,
    )

    result = await internal_wrapper()
    return result
