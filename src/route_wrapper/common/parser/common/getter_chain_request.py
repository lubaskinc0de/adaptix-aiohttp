from dataclasses import dataclass
from typing import Any

from route_wrapper.common.protocols.loader import Loader
from route_wrapper.common.protocols.request import Request


@dataclass
class GetterChainRequest:
    http_request: Request
    annotation: Any
    body_loader: Loader
    params_loader: Loader
    arg_name: str
    arg_default: Any
