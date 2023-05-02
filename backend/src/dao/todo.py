from .base import BaseDAO
from models import Todo


class TodoDAO(BaseDAO[Todo]):
    def __init__(self, session: AsyncSession):
        super(self, BaseDAO).__init__(Todo, session)

    async def create(self, content: str) -> Todo:
        todo = Todo(content=content)
        await self.session.add(todo)
    
    async def get_all(self) -> List[Todo]:
        stmt = select(self.model)
        tasks = await self.session.scalars(stmt)
        return tasks.all()
