from dataclasses import dataclass
from typing import List

from adaptix import Retort, name_mapping, NameStyle
from pydantic import BaseModel


@dataclass
class BaseTodo:
    todo: str
    completed: bool
    user_id: int


class BaseTodoPydantic(BaseModel):
    todo: str
    completed: bool
    user_id: int


@dataclass
class Todo(BaseTodo):
    todo_id: int


class TodoPydantic(BaseTodoPydantic):
    todo_id: int


@dataclass
class TodoList:
    todos: List[Todo]


retort = Retort(
    recipe=[
        name_mapping(BaseTodo, name_style=NameStyle.CAMEL),
        name_mapping(
            Todo,
            map={
                "todo_id": "id",
                "user_id": "userId",
            },
        ),
    ],
    strict_coercion=False,
)
