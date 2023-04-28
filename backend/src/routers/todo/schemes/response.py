from datetime import datetime

from pydantic import BaseModel


class TodoResponseScheme(BaseModel):
    id: int
    content: str
    is_done: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
