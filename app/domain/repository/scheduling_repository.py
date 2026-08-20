from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.scheduling import Scheduling

class ISchedulingRepository(ABC):

    @abstractmethod
    def get_All(self) -> List[SchedulingEntity]:
        pass

    @abstractmethod
    def get_user_id(self, id: int) -> Optional[SchedulingEntity]:
        pass

    @abstractmethod
    def create(self, scheduling: SchedulingEntity) -> None:
        pass

    @abstractmethod
    def update(self, scheduling: SchedulingEntity) -> None:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass