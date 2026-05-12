from app.domain.exceptions.exception_scheduling import (
    NotFoundScheduling,
    FindScheduling,
    AlreadyExistsScheduling,
    NotSucessCreateScheduling,
    NotSucessUpdateScheduling,
    NotSucessDeleteScheduling
)

from app.infrastructure.repositories.scheduling_repo_implementation import SchedulingRepository
from app.interface.mappers.scheduling_mapper import to_scheduling_response
from app.interface.schemas.scheduling_schemas import SchedulingCreate, SchedulingUpdate


class Scheduling:
    def __init__(self, repository: SchedulingRepository):
        self.repository = repository

    async def get_scheduling(self):
        schedulings = await self.repository.get_All()
        if not schedulings:
            raise NotFoundScheduling()
        
        return [to_scheduling_response(s) for s in schedulings]
        

    async def get_scheduling_id(self, id: int):
        scheduling = await self.repository.get_user_id(id)
        if not scheduling:
            raise FindScheduling()
        
        return to_scheduling_response(scheduling)
    
    async def create_scheduling(self, id: int, scheduling: SchedulingCreate):
        scheduling_verify =  await self.repository.get_user_id(id)
        if scheduling_verify: 
            raise AlreadyExistsScheduling()
        
        created = await self.repository.create(scheduling)
        if not created:
            raise NotSucessCreateScheduling()
        
        return to_scheduling_response(created)
    
    async def update_scheduling(self, id: int, scheduling: SchedulingUpdate):
        scheduling_verify =  await self.repository.get_user_id(id)
        if not scheduling_verify:
            raise NotFoundScheduling()
        
        updated = await self.repository.update(id, scheduling)
        if not updated:
            raise NotSucessUpdateScheduling()
        
        return to_scheduling_response(updated)
    
    async def delete_scheduling(self, id: int):
        scheduling_verify = await self.repository.delete(id)
        if not scheduling_verify:
            raise NotFoundScheduling()
        
        delete = await self.repository.delete(id)
        if not delete:
            raise NotSucessDeleteScheduling()
        
        return to_scheduling_response(delete)