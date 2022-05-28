from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db import get_db
from src.crud import todos
from src.routers.todo.schemes.request import CreateTodoRequestScheme
from src.routers.todo.schemes.response import TodoResponseScheme

router = APIRouter(
    prefix='/api/todo'
)


@router.post('/create', response_model=TodoResponseScheme)
async def create(
        db: Session = Depends(get_db),
        *,
        data: CreateTodoRequestScheme
):
    todo = todos.create_todo(db, data.content)
    return todo


@router.get('/all', response_model=List[TodoResponseScheme])
async def get_all_todos(
        db: Session = Depends(get_db)
):
    all_todos = todos.get_todos(db)
    return all_todos


@router.get('/get', response_model=TodoResponseScheme)
async def get_todo(
        db: Session = Depends(get_db),
        *,
        pk: int
):
    todo = todos.get_todo_by_id(db, pk)
    if not todo:
        raise HTTPException(
            status_code=404,
            detail='Todo is not found'
        )
    return todo


@router.put('/toggle_is_done', response_model=TodoResponseScheme)
async def toggle_is_done(
        db: Session = Depends(get_db),
        *,
        pk: int
):
    todo = todos.toggle_is_done(db, pk)
    return todo


@router.delete('/delete')
async def delete(
        db: Session = Depends(get_db),
        *,
        pk: int
):
    todos.delete(db, pk)
    return {'ok': True}
