from typing import Any, get_origin, Annotated

from route_wrapper.common.parser.common.source import Source


def compare_annotated(tp: Any, metadata: Source) -> bool:
    return get_origin(tp) == Annotated and tp.__metadata__[0] == metadata
