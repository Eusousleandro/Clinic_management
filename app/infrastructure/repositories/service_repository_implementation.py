from sqlalchemy.orm import Session

from app.domain.repository.service_repository import IServiceRepository
from app.infrastructure.database.models.service_model import Service
from app.interface.schemas.service_schema import ServiceUpdate


class ServiceRepository(IServiceRepository):
    def __init__(self, db: Session):
        self.db = db

    async def get_services(self):
        return self.db.query(Service).all
    
    async def get_service_id(self, id: int):
        return self.db.query(Service).filter(Service.id == id).first()

    async def create(self, service_data: Service):
        new_service = Service(**service_data.dict())
        self.db.add(new_service)
        self.db.commit()
        self.db.refresh(new_service)
        return new_service
    
    async def update(self, service: ServiceUpdate):
        service = self.db.query(Service).filter(Service.id == service.id).first()
        service_data = service.model_dump(exclude_unset=True)

        for key, value in service_data.items():
            setattr(service, key, value)
            
        self.db.commit()
        self.db.refresh(service)
        return service

    async def delete(self, id: int):
        service = self.db.query(Service).filter(Service.id == id).first()
        self.db.delete(service)
        self.db.commit()
        return service