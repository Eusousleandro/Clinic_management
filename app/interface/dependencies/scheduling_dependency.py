from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.use_cases.scheduling import Scheduling
from app.config.dependency import Dependencies
from app.infrastructure.repositories.scheduling_repo_implementation import SchedulingRepository


class SchedulingDependency:
    def get_dependency_scheduling(db: Session = Depends(Dependencies.get_db)) -> Scheduling:
        repository = SchedulingRepository(db)
        return Scheduling(repository)