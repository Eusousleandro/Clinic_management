
from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.use_cases.service import Service
from app.config.dependency import Dependencies
from app.infrastructure.repositories.service_repository_implementation import ServiceRepository


class ServiceDependency:
    def get_depedency_service(db: Session = Depends(Dependencies.get_db)) -> Service:
        repository = ServiceRepository(db)
        return Service(repository)