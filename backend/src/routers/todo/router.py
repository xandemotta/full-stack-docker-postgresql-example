from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from crud import todos
from .schemes.request import CreateTodoRequestScheme, PkRequestScheme
from .schemes.response import TodoResponseScheme

router = APIRouter(prefix="/api/todo")


@router.post("/create", response_model=TodoResponseScheme)
async def create(
    session: AsyncSession = Depends(get_session), *, data: CreateTodoRequestScheme
):
    todo = await todos.create_todo(session, data.content)
    return todo


@router.get("/all", response_model=List[TodoResponseScheme])
async def get_all_todos(session: AsyncSession = Depends(get_session)):
    all_todos = await todos.get_todos(session)
    return all_todos


@router.get("/get", response_model=TodoResponseScheme)
async def get_todo(session: AsyncSession = Depends(get_session), *, pk: int):
    todo = await todos.get_todo_by_id(session, pk)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/toggle_is_done", response_model=TodoResponseScheme)
async def toggle_is_done(
    session: AsyncSession = Depends(get_session), *, data: PkRequestScheme
):
    todo = await todos.toggle_is_done(session, data.pk)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.delete("/delete")
async def delete(session: AsyncSession = Depends(get_session), *, pk: int):
    ok = await todos.delete(session, pk)
    return {"ok": ok}
