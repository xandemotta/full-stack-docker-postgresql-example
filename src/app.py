from fastapi import FastAPI


def create_app() -> FastAPI:
    app_ = FastAPI(
        docs_url="/",
        redoc_url="/redoc"
    )

    _include_routers(app_)

    return app_


def _include_routers(app_: FastAPI):
    """Include routers to application"""

    from routers.todo.router import router as todo_router

    app_.include_router(todo_router)


app = create_app()
