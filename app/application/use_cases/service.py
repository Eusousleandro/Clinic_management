from fastapi import HTTPException, status

from app.infrastructure.repositories.service_repository_implementation import ServiceRepository
from app.interface.mappers.service_mapper import to_service_response
from app.interface.schemas.service_schema import ServiceCreate, ServiceUpdate
from app.interface.handler.exception_service import ServiceExceptionHandler

class Service:
    def __init__(self, repository: ServiceRepository):
        self.repository = repository

    async def get_services(self):
        services = await self.repository.get_All()
        if not services:
            raise ServiceExceptionHandler.notfound_handle_exception(None, Exception("No services found"))
        return [to_service_response(s) for s in services]
    
    async def get_service_by_id(self, id: int):
        service = await self.repository.get_user_id(id)
        if not service:
            raise ServiceExceptionHandler.find_handle_exception(None, Exception("Service not found"))
        return to_service_response(service)
    
    async def create_service(self, service_data: ServiceCreate):
        verify_service = await self.repository.get_user_id(service_data.id)
        if verify_service:
            raise ServiceExceptionHandler.already_exists_handle_exception(None, Exception("Service already exists"))        
        service = await self.repository.create(service_data)
        if not service:
            raise ServiceExceptionHandler.create_handle_exception(None, Exception("Failed to create service"))
        return to_service_response(service)
    
    async def update_service(self, id: int, service_data: ServiceUpdate):
        service = await self.repository.get_user_id(id)
        if not service:
            raise ServiceExceptionHandler.notfound_handle_exception(None, Exception("Service not found"))
        
        updated_service = await self.repository.update(id, service_data)
        if not updated_service:
            raise ServiceExceptionHandler.update_handle_exception(None, Exception("Failed to update service"))
        return to_service_response(updated_service)
    
    async def delete_service(self, id: int):
        service = await self.repository.get_user_id(id)
        if not service:
            raise ServiceExceptionHandler.notfound_handle_exception(None, Exception("Service not found"))
        
        deleted_service = await self.repository.delete(id)
        if not deleted_service:
            raise ServiceExceptionHandler.delete_handle_exception(None, Exception("Failed to delete service"))
        return to_service_response(deleted_service)