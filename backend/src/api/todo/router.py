from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from schemes import Ok, Task, ListTasks, ReqCreateTask, ReqToggleDoneTask
from services import ServicesFactory
from core import get_services

router = APIRouter(prefix="/todo")


@router.post("/create", response_model=Task)
async def create_task(
    services: ServicesFactory = Depends(get_services), *, data: ReqCreateTask
):
    task = await services.todo_service.create(data)
    return task


@router.get("/all", response_model=ListTasks)
async def get_all_tasks(services: ServicesFactory = Depends(get_services)):
    todos = await services.todo_service.get_all()
    return todos


@router.get("/get", response_model=Task)
async def get_task(services: ServicesFactory = Depends(get_services), *, pk: int):
    task = await services.todo_service.get(pk)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/toggle_done", response_model=Task)
async def toggle_done_task(
    services: ServicesFactory = Depends(get_services), *, data: ReqToggleDoneTask 
):
    task = await services.todo_service.toggle_done(data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/delete", response_model=Ok)
async def delete_task(services: ServicesFactory = Depends(get_services), *, pk: int):
    ok = await services.todo_service.delete(pk)
    return {"ok": ok}
