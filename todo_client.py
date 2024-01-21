from adaptix import Retort
from aiohttp import ClientSession

from models import TodoList


class TodoClient:
    def __init__(self, client_session: ClientSession, retort: Retort) -> None:
        self.client_session = client_session
        self.retort = retort

        self._url = "https://dummyjson.com/todos"

    async def get_todos(self) -> TodoList:
        async with self.client_session.get(self._url) as response:
            json = await response.json()
            model = self.retort.load(json, TodoList)

            return model
