from typing import (
    TypeVar,
)

from route_wrapper.integrations.pydantic.loader import PydanticLoader
from src.route_wrapper import ParamsGetter
from src.route_wrapper import OutputModelT
from src.route_wrapper import Route
from src.route_wrapper import RouteWrapper

T = TypeVar("T")


async def pydantic_provider(
    route: Route,
) -> OutputModelT:
    loader = PydanticLoader()
    params_getter = ParamsGetter(loader, route, route.source_params)

    internal_wrapper = RouteWrapper(
        route=route,
        params_getter=params_getter,
    )

    result = await internal_wrapper()
    return result
