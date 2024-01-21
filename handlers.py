from adaptix import Retort
from aiohttp import web

from todo_client import TodoClient


class TodoHandler:
    def __init__(self, todo_client: TodoClient, retort: Retort) -> None:
        self.todo_client = todo_client
        self.retort = retort

    async def get_todos(self, _request: web.Request) -> web.Response:
        todos = await self.todo_client.get_todos()
        todos_json = self.retort.dump(todos)

        return web.json_response(todos_json)
