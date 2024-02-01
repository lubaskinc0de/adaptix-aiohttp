from starlette.responses import JSONResponse

from route_wrapper.common import WebResponseFactory, MappingDumper, OutputModelT


class JSONResponseFactory(WebResponseFactory):
    def __init__(self, dumper: MappingDumper) -> None:
        self.dumper = dumper

    async def __call__(self, output: OutputModelT) -> JSONResponse:
        dumped = self.dumper.dump(output)
        return JSONResponse(dumped)
