from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app_ = FastAPI(docs_url="/", redoc_url="/redoc")

    _include_routers(app_)

    app_.add_middleware(
        CORSMiddleware,
        allow_origins=("*",),
        allow_credentials=True,
        allow_methods=("*",),
        allow_headers=("*",),
    )

    return app_


def _include_routers(app_: FastAPI):
    """Include routers to application"""

    from routers.todo.router import router as todo_router

    app_.include_router(todo_router)


app = create_app()
