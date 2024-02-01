from inspect import Signature, Parameter

from route_wrapper import save_signature, Route, provide_response_by_factory


def view_wrapper(
    web_provider,
    default_response_factory,
    dumper,
    response_factory,
    data_provider,
    data_provider_kwargs,
    raw: bool = False,
):
    @save_signature
    def inner(view, view_signature: Signature, source_params: dict[str, Parameter]):
        web_wrapper = web_provider(view, view_signature, source_params)

        async def request_handler(*args, **kwargs):
            route: Route = web_wrapper(*args, **kwargs)
            output = await data_provider(route, **data_provider_kwargs)
            return output

        if raw:
            return request_handler

        return provide_response_by_factory(
            default_factory=default_response_factory,
            dumper=dumper,
            response_factory=response_factory,
        )(request_handler)

    return inner
