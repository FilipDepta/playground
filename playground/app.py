from starlette.applications import Starlette
from starlette.responses import (
    JSONResponse,
    PlainTextResponse,
)
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({"hello": "world"})


async def favicon(request):
    return PlainTextResponse("")


app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
        Route("/favicon.ico", favicon),
    ],
)
