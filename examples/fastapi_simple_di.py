from fastapi import FastAPI, Request, Depends
from example_models import retort, BaseTodo, Todo

from route_wrapper.integrations.fastapi import adaptix_wrapper
from route_wrapper import FromBody, FromQuery, FromHeaders

app = FastAPI()


class Dependency:
    pass


app.dependency_overrides[Dependency] = lambda: "hello"


@app.post("/")
@adaptix_wrapper(retort)
async def new_todo(
    _request: Request,
    todo: FromBody[BaseTodo],
    q: FromQuery[int],
    h: FromHeaders[str],
    some_dep: Dependency = Depends(),
) -> Todo:
    print(q, h, some_dep)
    return Todo(
        todo_id=10,
        todo=todo.todo,
        completed=todo.completed,
        user_id=todo.user_id,
    )
