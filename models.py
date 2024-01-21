from dataclasses import dataclass
from typing import List


@dataclass
class Todo:
    todo_id: int
    todo: str
    completed: bool
    user_id: int


@dataclass
class TodoList:
    todos: List[Todo]
