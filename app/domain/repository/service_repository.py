from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.service import ServiceEntity

class IServiceRepository(ABC):

    @abstractmethod
    def get_All(self) -> List[ServiceEntity]:
        pass

    @abstractmethod
    def get_user_id(self, id: int) -> Optional[ServiceEntity]:
        pass

    @abstractmethod
    def create(self, service: ServiceEntity) -> None:
        pass

    @abstractmethod
    def update(self, service: ServiceEntity) -> None:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass