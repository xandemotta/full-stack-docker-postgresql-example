from pydantic import BaseModel


class CreateTodoRequestScheme(BaseModel):
    content: str


class PkRequestScheme(BaseModel):
    pk: int
