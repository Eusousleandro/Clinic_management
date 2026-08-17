from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.user import UserEntity

def IUserRepository():

    @abstractmethod
    def get_All(self) -> List[UserEntity]:
        pass

    @abstractmethod
    def get_user_id(self, id: int) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def create(self, user: UserEntity) -> None:
        pass

    @abstractmethod
    def update(self, user: UserEntity) -> None:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass    