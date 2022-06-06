from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

from .core import engine

Base = declarative_base(bind=engine)


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    content = Column(String(100))
    is_done = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
