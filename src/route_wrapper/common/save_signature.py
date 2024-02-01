import inspect
from typing import Callable, Any

from route_wrapper.common.parser import ParamsParser


def save_signature(
    inner_wrapper: Callable[[..., Any, inspect.Signature], Callable[[Any], Any]]
):
    def wrapper(view: Any):
        view_signature = inspect.signature(view)
        params_parser = ParamsParser(view_signature)
        source_params = params_parser.get_source_params()

        view_wrapper = inner_wrapper(view, view_signature, source_params)

        view_wrapper.__signature__ = inspect.Signature(
            parameters=[
                value
                for key, value in view_signature.parameters.items()
                if key not in source_params
            ],
            return_annotation=view_signature.return_annotation,
        )

        view_wrapper.__doc__ = view.__doc__

        return view_wrapper

    return wrapper
