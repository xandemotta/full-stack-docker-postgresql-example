from typing import List, Union

from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.db import Todo


def create_todo(
        db: Session,
        content: str
) -> Todo:
    db_todo = Todo(content=content)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todos(
        db: Session
) -> List[Todo]:
    return db.query(Todo).all()


def get_todo_by_id(
        db: Session,
        todo_id: int
) -> Union[Todo, None]:
    return db.query(Todo).where(Todo.id == todo_id).first()


def toggle_is_done(
        db: Session,
        todo_id: int
) -> Union[Todo, None]:
    db_todo = get_todo_by_id(db, todo_id)
    if not db_todo:
        raise HTTPException(
            status_code=404,
            detail='Todo is not found'
        )
    db_todo.is_done = not db_todo.is_done
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete(
        db: Session,
        todo_id: int
) -> None:
    db_todo = get_todo_by_id(db, todo_id)
    if not db_todo:
        raise HTTPException(
            status_code=404,
            detail='Todo is not found'
        )
    db.delete(db_todo)
    db.commit()
