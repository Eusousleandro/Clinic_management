from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.patient import Patient

class IPatientRepository(ABC):

    @abstractmethod
    def get_users(self) -> List[Patient]:
        pass

    @abstractmethod
    def get_user(self, id: int) -> Optional[Patient]:
        pass

    @abstractmethod
    def create(self, patient: Patient) -> None:
        pass

    @abstractmethod
    def update(self, id: int, patient: Patient) -> None:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass