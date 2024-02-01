from typing import Union, Optional, Type, Any

from route_wrapper.common import Dumper
from route_wrapper.common import WebResponseFactory


def provide_response_by_factory(
    default_factory: Type[WebResponseFactory],
    dumper: Dumper,
    response_factory: Union[
        Optional[WebResponseFactory], Optional[Type[WebResponseFactory]]
    ] = None,
):
    def inner(func: Any):
        async def wrapper(*args, **kwargs):
            result = await func(*args, **kwargs)
            if response_factory:
                if isinstance(response_factory, type):
                    factory = response_factory(dumper)
                    response = await factory(result)

                    return response

                response = await response_factory(result)
                return response

            factory = default_factory(dumper)
            response = await factory(result)

            return response

        return wrapper

    return inner
