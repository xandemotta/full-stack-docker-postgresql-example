from fastapi import FastAPI, HTTPException

from src.core.errors import http_exception_handler


def create_app() -> FastAPI:
    app_ = FastAPI(
        docs_url='/',
        redoc_url='/redoc'
    )

    _include_routers(app_)
    _include_exception_handlers(app_)

    return app_


def _include_routers(app_: FastAPI):
    """Include routers to application"""

    from src.routers.todo.router import router as todo_router

    app_.include_router(todo_router)


def _include_exception_handlers(app_: FastAPI):
    """Add exception handlers to applications"""

    app_.add_exception_handler(HTTPException, http_exception_handler)


app = create_app()
