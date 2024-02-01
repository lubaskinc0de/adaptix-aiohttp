from aiohttp import web

from src.route_wrapper import MappingDumper
from src.route_wrapper import OutputModelT
from src.route_wrapper import WebResponseFactory


class JSONResponseFactory(WebResponseFactory):
    def __init__(self, dumper: MappingDumper) -> None:
        self.dumper = dumper

    async def __call__(self, output: OutputModelT) -> web.Response:
        dumped = self.dumper.dump(output)
        return web.json_response(data=dumped)
