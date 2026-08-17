from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.user import UserEntity

def IUserRepository():

    def get_All(self) -> List[UserEntity]:
        pass

    def get_user_id(self, id: int) -> Optional[UserEntity]:
        pass

    def create(self, user: UserEntity) -> None:
        pass

    def update(self, user: UserEntity) -> None:
        pass


    def delete(self, id: int) -> None:
        pass    