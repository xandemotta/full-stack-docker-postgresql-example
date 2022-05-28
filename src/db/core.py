from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

from src.core.config import DATABASE_URI

engine = create_engine(
    DATABASE_URI, echo=True, future=True
)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=Session)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
