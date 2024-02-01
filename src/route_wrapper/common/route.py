from dataclasses import dataclass
from inspect import Parameter, Signature
from typing import Any, Mapping, Optional

from route_wrapper.common import Request


@dataclass
class Route:
    request: Request
    view: Any
    source_params: Mapping[str, Parameter]
    view_signature: Signature
    view_obj: Optional[Any]
    additional_kwargs: Mapping[str, Any]
