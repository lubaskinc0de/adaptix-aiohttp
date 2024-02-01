from functools import partial

from adaptix import Retort

from route_wrapper.integrations.adaptix import adaptix_provider
from route_wrapper.integrations.adaptix.dumper import RetortDumper

from src.route_wrapper import view_wrapper, base_wrapper

from route_wrapper.integrations.starlette.response_factory import JSONResponseFactory
from route_wrapper.integrations.starlette.provider import starlette_provider


@base_wrapper(
    default_response_factory=JSONResponseFactory,
    web_provider=starlette_provider,
)
def adaptix_wrapper(
    retort: Retort,
):
    retort_dumper = RetortDumper(retort)

    return partial(
        view_wrapper,
        dumper=retort_dumper,
        data_provider=adaptix_provider,
        data_provider_kwargs={
            "retort": retort,
        },
    )
