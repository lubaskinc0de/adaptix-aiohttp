from aiohttp import ClientSession

from example_models import TodoList, BaseTodo, Todo, retort


class TodoClient:
    def __init__(self, client_session: ClientSession) -> None:
        self.client_session = client_session

        self._url = "https://dummyjson.com/todos"

    async def get_todos(self) -> TodoList:
        async with self.client_session.get(self._url) as response:
            json = await response.json()
            model = retort.load(json, TodoList)

            return model

    async def create_todo(self, todo: BaseTodo) -> Todo:
        post_data = retort.dump(todo)

        async with self.client_session.post(
            f"{self._url}/add", data=post_data
        ) as response:
            json = await response.json()
            model = retort.load(json, Todo)

            return model
