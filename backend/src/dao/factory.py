from sqlalchemy.ext.asyncio import AsyncSession

from .todo import TodoDAO


class DAOFactory:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    @property
    def todo_dao(self) -> TodoDAO:
        return TodoDAO(self)
