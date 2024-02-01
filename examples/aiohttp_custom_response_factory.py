from typing import List

from aiohttp import web, ClientSession

from route_wrapper import FromBody

from route_wrapper.common import OutputModelT
from route_wrapper.common import WebResponseFactory

from route_wrapper.integrations.adaptix.dumper import RetortDumper
from route_wrapper.integrations.aiohttp import adaptix_wrapper

from example_todo_client import TodoClient
from example_models import TodoList, retort, Todo, BaseTodo


class MyResponseFactory(WebResponseFactory):
    def __init__(self, dumper: RetortDumper) -> None:
        self.dumper = dumper

    async def __call__(self, output: OutputModelT) -> web.Response:
        print("Hello!")
        return web.json_response(self.dumper.dump(output))


class TodoHandler:
    def __init__(self, todo_client: TodoClient):
        self.todo_client = todo_client

    @adaptix_wrapper(retort)
    async def get_todos(self, _request: web.Request) -> TodoList:
        return await self.todo_client.get_todos()

    @adaptix_wrapper(retort, response_factory=MyResponseFactory)
    async def create_todo(
        self,
        _request: web.Request,
        new_todo: FromBody[BaseTodo],
    ) -> Todo:
        todo = Todo(
            todo=new_todo.todo,
            completed=new_todo.completed,
            user_id=new_todo.user_id,
            todo_id=1,
        )

        return todo


async def init_app(_argv: List[str]) -> web.Application:
    app = web.Application()

    client_session = ClientSession()

    todo_client = TodoClient(client_session)
    todo_handler = TodoHandler(todo_client)

    app.add_routes([web.get("/todos/", todo_handler.get_todos)])
    app.add_routes([web.post("/todos/{c}/", todo_handler.create_todo)])

    return app
