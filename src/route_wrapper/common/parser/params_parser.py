from inspect import Signature, Parameter
from typing import get_origin, Annotated

from route_wrapper.common.parser.common.source import Source


class ParamsParser:
    def __init__(self, view_signature: Signature):
        self.view_signature = view_signature

    def get_source_params(self) -> dict[str, Parameter]:
        params = {}

        for key, value in self.view_signature.parameters.items():
            if value.annotation != Parameter.empty:
                if (
                    get_origin(value.annotation) == Annotated
                    and value.annotation.__metadata__[0] in Source
                ):
                    params[key] = value
        return params
