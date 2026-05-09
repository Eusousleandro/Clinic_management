from typing import List

from fastapi import APIRouter, Depends

from app.application.use_cases.service import Service
from app.interface.dependencies.service_dependency import ServiceDependency
from app.interface.schemas.service_schema import ServiceCreate, ServiceResponse, ServiceUpdate

router = APIRouter(prefix='/service', tags=['service'])


@router.get('/', response_model=List[ServiceResponse])
async def get_services(
    service: Service = Depends(ServiceDependency.get_depedency_service)
):
    return await service.get_services()

@router.get('/{id}', response_model=ServiceResponse)
async def get_service_by_id(
    id: int, 
    service: Service = Depends(ServiceDependency.get_depedency_service),
):
    return await service.get_service_by_id(id)

@router.post('/', response_model=ServiceResponse)
async def create_service(
    server: ServiceCreate,
    service: Service = Depends(ServiceDependency.get_depedency_service)
):
    return await service.create_service(server)

@router.put('/{id}', response_model=ServiceResponse)
async def update_service(
    id: int, 
    server: ServiceUpdate,
    service: Service = Depends(ServiceDependency.get_depedency_service)
):
    return await service.update_service(id, server)

@router.delete('/{id}', response_model=ServiceResponse)
async def delete_service(
    id: int, 
    service: Service = Depends(ServiceDependency.get_depedency_service)
):
    return await service.delete_service(id)