from dao import DAOFactory
from .todo import TodoService


class ServicesFactory:
    def __init__(self, daos: DAOFactory):
        self.daos = daos

    @property
    def todo_service(self) -> TodoService:
        return TodoService(self.daos)
