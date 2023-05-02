from dao import DAOFactory

from schemes import ListTasks, Task, ReqCreateTask, ReqToggleDoneTask
from .converters import convert_to_dto, convert_multiple_to_dto


class TodoService:
    def __init__(self, daos: DAOFactory):
        self.daos = daos
    
    async def create(self, data: ReqCreateTask) -> Task:
        task = await self.daos.todo_dao.create(content=content)
        await self.daos.session.commit()
        return convert_to_dto(task, Task)
    
    async def get_all(self) -> ListTasks:
        tasks = await self.daos.todo_dao.get_all()
        return convert_multiple_to_dto(tasks, Task)
    
    async def get(self, id: int) -> Task:
        task = await self.daos.todo_dao.get(id=id)
        return convert_to_dto(task, Task)
    
    async def toggle_done(self, data: ReqToggleDoneTask) -> Task:
        task = await self.daos.todo_dao.get(for_update=True, id=data.pk)
        task.is_done = not task.is_done
        self.daos.session.add(task)
        await self.session.commit()
        return task
    
    async def delete(self, id: int) -> bool:
        try:
            await self.daos.todo_dao.delete(id)
            return True
        except:
            return False
