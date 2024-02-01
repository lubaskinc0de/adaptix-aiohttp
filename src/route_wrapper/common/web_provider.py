from inspect import Signature, Parameter
from typing import (
    TypeVar,
    Any,
)

from route_wrapper.common.route import Route
from route_wrapper.common import OutputModelT

T = TypeVar("T")


def web_provider(request_type: type):
    def inner(wrapper_func: Any):
        def decorator(
            view: Any, view_signature: Signature, source_params: dict[str, Parameter]
        ):
            view_return_type: OutputModelT | Signature.empty = (
                view_signature.return_annotation
            )

            if not view_return_type:
                raise TypeError("View has no return type!")

            if len(view_signature.parameters) == 0:
                raise TypeError("View must accept request")

            if list(view_signature.parameters.keys())[0] == "self":
                is_method = True
            else:
                is_method = False

            if is_method and len(view_signature.parameters) < 2:
                raise TypeError(
                    "Your method view must accept self and request parameters."
                )

            def wrapper(*args, **kwargs) -> Any:
                args = list(args) + list(kwargs.values())
                request = None
                for arg in args:
                    if isinstance(arg, request_type):
                        request = arg

                if not request:
                    raise AttributeError("No request!")

                if not is_method:
                    obj = None
                else:
                    obj = args[0]

                request = wrapper_func(request)

                return Route(
                    request=request,
                    source_params=source_params,
                    view_signature=view_signature,
                    view_obj=obj,
                    view=view,
                    additional_kwargs={
                        key: value
                        for key, value in kwargs.items()
                        if key not in source_params
                        and not isinstance(value, request_type)
                    },
                )

            return wrapper

        return decorator

    return inner
