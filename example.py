from typing import List

from adaptix import Retort, name_mapping, NameStyle

from aiohttp import web, ClientSession

from handlers import TodoHandler
from models import Todo
from todo_client import TodoClient


def init_retort() -> Retort:
    return Retort(
        recipe=[
            name_mapping(Todo, name_style=NameStyle.CAMEL),
            name_mapping(
                Todo,
                map={
                    "todo_id": "id",
                },
            ),
        ],
    )


async def init_app(_argv: List[str]) -> web.Application:
    app = web.Application()

    client_session = ClientSession()
    retort = init_retort()
    weather_client = TodoClient(client_session, retort)
    weather_handler = TodoHandler(weather_client, retort)

    app.add_routes([web.get("/todos/", weather_handler.get_todos)])

    return app
