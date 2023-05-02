from typing import List
from datetime import datetime

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    content: str
    is_done: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ListTasks(BaseModel):
    __root__ = List[Task]


class ReqCreateTask(BaseModel):
    content: str


class ReqToggleDoneTask(BaseModel):
    pk: int

