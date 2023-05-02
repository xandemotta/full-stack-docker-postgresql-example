from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from .db import async_session
from dao import DAOFactory
from services import ServicesFactory


async def get_services(session: AsyncSession = Depends(get_session)) -> ServicesFactory:
    daos = DAOFactory(session)
    services = ServicesFactory(daos)
    return services


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session