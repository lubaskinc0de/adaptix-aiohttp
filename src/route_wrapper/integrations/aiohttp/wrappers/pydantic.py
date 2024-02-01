from typing import Optional, Type, Union

from route_wrapper.integrations.pydantic.dumper import PydanticDumper
from src.route_wrapper import view_wrapper
from route_wrapper.integrations.aiohttp.response_factory import JSONResponseFactory
from src.route_wrapper import WebResponseFactory
from route_wrapper.integrations.aiohttp.provider import aiohttp_provider

from route_wrapper.integrations.pydantic.provider import pydantic_provider


def pydantic_wrapper(
    response_factory: Union[
        Optional[WebResponseFactory], Optional[Type[WebResponseFactory]]
    ] = None,
):
    return view_wrapper(
        data_provider=pydantic_provider,
        response_factory=response_factory,
        default_response_factory=JSONResponseFactory,
        dumper=PydanticDumper(),
        data_provider_kwargs={},
        web_provider=aiohttp_provider,
    )
