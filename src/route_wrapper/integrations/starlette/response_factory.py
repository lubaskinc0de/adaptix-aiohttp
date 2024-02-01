from starlette.responses import JSONResponse

from src.route_wrapper import MappingDumper
from src.route_wrapper import OutputModelT
from src.route_wrapper import WebResponseFactory


class JSONResponseFactory(WebResponseFactory):
    def __init__(self, dumper: MappingDumper) -> None:
        self.dumper = dumper

    async def __call__(self, output: OutputModelT) -> JSONResponse:
        dumped = self.dumper.dump(output)
        return JSONResponse(dumped)
