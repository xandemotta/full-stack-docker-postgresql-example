from typing import Generic, TypeVar, Type, Union

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from models import Base

Model = TypeVar("Model", Base, Base)


class BaseDAO(Generic[Model]):
    def __init__(self, model: Type[Model], session: AsyncSession):
        self.model = model
        self.session = session
    
    async def get(self, for_update: bool = False, **kwargs) -> Model | None:
        stmt = select(self.model).filter_by(**kwargs)
        if for_update:
            stmt = stmt.with_for_update()
        return await self.session.scalar(stmt)
    
    async def get_or_create(self, defaults: dict = {}, for_update: bool = False, **kwargs) -> Tuple[Model, bool]:
        i = await self.get(for_update=for_update, **kwargs)
        if i:
            return i, False
        kwargs.update(defaults)
        i = self.model(**kwargs)
        self.session.add(i)
        await self.session.flush()
        return i, True
    
    async def update(self, id: int, **kwargs):
        stmt = update(self.model).values(**kwargs).where(self.model.id == id)
        await self.session.execute(stmt)
    
    async def delete(self, id: int):
        stmt = update(self.model).where(self.model.id == id)
        await self.session.execute(stmt)
