from pydantic import BaseModel


class CreateTodoRequestScheme(BaseModel):
    content: str
