from typing import List

from fastapi import APIRouter, Depends

from app.application.use_cases.scheduling import Scheduling
from app.interface.dependencies.scheduling_dependency import SchedulingDependency
from app.interface.schemas.scheduling_schemas import SchedulingCreate, SchedulingResponse, SchedulingUpdate

router = APIRouter(prefix='/scheduling', tags=['schedulings'])

@router.get('/', response_model=List[SchedulingResponse])
async def get_All(
    scheduling: Scheduling = Depends(SchedulingDependency.get_dependency_scheduling)
):
    return await scheduling.get_scheduling()

@router.get('/{id}', response_model=SchedulingResponse)
async def get_all_scheduling(
    id: int,
    scheduling: Scheduling = Depends(SchedulingDependency.get_dependency_scheduling)
):
    return await scheduling.get_scheduling_id(id)

@router.post('/', response_model=SchedulingResponse)
async def scheduling_create(
    schedul: SchedulingCreate,
    scheduling: Scheduling = Depends(SchedulingDependency.get_dependency_scheduling)
):
    return await scheduling.create_scheduling(schedul)

@router.put('/{id}', response_model=SchedulingResponse)
async def scheduling_update(
    id: int,
    schedul: SchedulingUpdate,
    scheduling: Scheduling = Depends(SchedulingDependency.get_dependency_scheduling)
):
    return await scheduling.update_scheduling(id, schedul)

@router.delete('/{id}', response_model=SchedulingResponse)
async def scheduling_delete(
    id: int,
    scheduling: Scheduling = Depends(SchedulingDependency.get_dependency_scheduling)
):
    return await scheduling.delete_scheduling(id)