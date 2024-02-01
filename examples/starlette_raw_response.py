from starlette.applications import Starlette, Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from example_models import Todo, BaseTodo, retort

from route_wrapper.integrations.starlette import adaptix_wrapper
from route_wrapper import FromBody, FromQuery, FromHeaders


@adaptix_wrapper(retort)
async def new_todo(
    _request: Request,
    todo: FromBody[BaseTodo],
    q: FromQuery[int],
    h: FromHeaders[str],
) -> Todo:
    print(q, h)
    return Todo(
        todo_id=10,
        todo=todo.todo,
        completed=todo.completed,
        user_id=todo.user_id,
    )


@adaptix_wrapper(retort, raw=True)
async def new_todo_raw(
    _request: Request,
    todo: FromBody[BaseTodo],
) -> JSONResponse:
    todo = Todo(
        todo_id=10,
        todo=todo.todo,
        completed=todo.completed,
        user_id=todo.user_id,
    )

    response = JSONResponse(
        content=retort.dump(todo),
        status_code=201,
    )

    return response

m = ["POST"]

app = Starlette(
    debug=True,
    routes=[
        Route("/", new_todo, methods=m),
        Route("/raw", new_todo_raw, methods=m),
    ],
)
