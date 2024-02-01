from aiohttp import web

from route_wrapper.common import WebResponseFactory, MappingDumper, OutputModelT


class JSONResponseFactory(WebResponseFactory):
    def __init__(self, dumper: MappingDumper) -> None:
        self.dumper = dumper

    async def __call__(self, output: OutputModelT) -> web.Response:
        dumped = self.dumper.dump(output)
        return web.json_response(data=dumped)
