from fastapi import HTTPException, status

from app.domain.exceptions.exception import (
    AlreadyExistsHandleException, 
    CreateHandleException, 
    DeleteHandleException, 
    FindHandleException, 
    NotFoundHandleException, 
    UpdateHandleException
)

from app.infrastructure.repositories.service_repository_implementation import ServiceRepository
from app.interface.mappers.service_mapper import to_service_response
from app.interface.schemas.service_schema import ServiceCreate, ServiceUpdate

class Service:
    def __init__(self, repository: ServiceRepository):
        self.repository = repository

    async def get_services(self):
        services = await self.repository.get_All()
        if not services:
            raise NotFoundHandleException("No services found")
        return [to_service_response(s) for s in services]
    
    async def get_service_by_id(self, id: int):
        service = await self.repository.get_user_id(id)
        if not service:
            raise FindHandleException("Service not found")
        return to_service_response(service)
    
    async def create_service(self, service_data: ServiceCreate):
        verify_service = await self.repository.get_user_name(service_data.name)
        if verify_service:
            raise AlreadyExistsHandleException("Service already exists")
        
        service = await self.repository.create(service_data)
        if not service:
            raise CreateHandleException("Failed to create service")
        return to_service_response(service)
    
    async def update_service(self, id: int, service_data: ServiceUpdate):
        service = await self.repository.get_user_id(id)
        if not service:
            raise NotFoundHandleException("Service not found")
        
        updated_service = await self.repository.update(id, service_data)
        if not updated_service:
            raise UpdateHandleException("Failed to update service")
        return to_service_response(updated_service)
    
    async def delete_service(self, id: int):
        service = await self.repository.get_user_id(id)
        if not service:
            raise NotFoundHandleException("Service not found")
        
        deleted_service = await self.repository.delete(id)
        if not deleted_service:
            raise DeleteHandleException("Failed to delete service")
        return to_service_response(deleted_service)