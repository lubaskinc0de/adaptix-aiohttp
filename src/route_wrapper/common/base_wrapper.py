from typing import Type, Optional, Union

from route_wrapper.common import WebResponseFactory


def base_wrapper(
    default_response_factory: Type[WebResponseFactory],
    web_provider,
):
    def inner(func):
        def wrapper(
            *args,
            response_factory: Union[
                Optional[WebResponseFactory], Optional[Type[WebResponseFactory]]
            ] = None,
            raw: bool = False,
            **kwargs,
        ):
            partial_view_wrapper = func(*args, **kwargs)
            return partial_view_wrapper(
                response_factory=response_factory,
                web_provider=web_provider,
                default_response_factory=default_response_factory,
                raw=raw,
            )

        return wrapper

    return inner
