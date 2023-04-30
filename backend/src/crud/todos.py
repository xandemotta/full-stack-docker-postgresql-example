from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import Todo


async def create_todo(
    session: AsyncSession,
    content: str
) -> Todo:
    todo = Todo(content=content)
    session.add(todo)
    await session.commit()
    await session.refresh(todo)
    return todo


async def get_todos(
    session: AsyncSession
) -> List[Todo]:
    stmt = select(Todo)
    return (await session.scalars(stmt)).all()


async def get_todo_by_id(
    session: AsyncSession,
    todo_id: int
) -> Optional[Todo]:
    stmt = select(Todo).where(Todo.id == todo_id)
    return await session.scalar(stmt)


async def toggle_is_done(
    session: AsyncSession,
    todo_id: int
) -> Optional[Todo]:
    todo = await get_todo_by_id(session, todo_id)
    if not todo:
        return None
    todo.is_done = not todo.is_done
    session.add(todo)
    await session.commit()
    await session.refresh(todo)
    return todo


async def delete(
    session: AsyncSession,
    todo_id: int
) -> bool:
    todo = await get_todo_by_id(session, todo_id)
    if not todo:
        return False
    await session.delete(todo)
    await session.commit()
    return True
