from sqlalchemy.orm import Session

from app.domain.repository.scheduling_repository import ISchedulingRepository
from app.infrastructure.database.models.scheduling_model import Scheduling
from app.interface.schemas.scheduling_schemas import SchedulingCreate, SchedulingUpdate

class SchedulingRepository(ISchedulingRepository):
    def __init__(self, db: Session):
        self.db = db
    
    async def get_All(self):
        return self.db.query(Scheduling).all()

    async def get_user_id(self, id: int):
        return self.db.query(Scheduling).filter(Scheduling.id == id).first()

    async def get_user_name(self, name: str):
        return self.db.query(Scheduling).filter(Scheduling.name == name).first()

    async def create(self, scheduling_data: SchedulingCreate):
        new_scheduling = Scheduling(**scheduling_data.model_dump())
        self.db.add(new_scheduling)
        self.db.commit()
        self.db.refresh(new_scheduling)
        return new_scheduling

    async def update(self, id: int, scheduling_data: SchedulingUpdate):
        scheduling_update = self.db.query(Scheduling).filter(Scheduling.id == id).first()
        scheduling = scheduling_data.model_dump(exclude_unset=True)

        for keys, values in scheduling.items():
            setattr(scheduling_update, keys, values)

        self.db.commit()
        self.db.refresh(scheduling_update)
        return scheduling_update

    async def delete(self, id: int):
        scheduling = self.db.query(Scheduling).filter(Scheduling.id == id).first()
        self.db.delete(scheduling)
        self.db.commit()
        return scheduling