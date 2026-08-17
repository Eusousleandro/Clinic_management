from app.interface.handler.exception_user import (
    NotFoundUser,
    FindUser,
    AlreadyExistsUser,
    NotSucessCreateUser,
    NotSucessUpdateUser,
    NotSucessDeleteDelete,
    NotAuthenticationUser
)

from.app.infrastructure.repositories.user_repo_implementation import UserRepository
from app.infrastructure.mappers.user_mapper import to_user_response
from app.infrastructure.schemas.user_schema import UserCreate, UserUpdate

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository =  repository
    
    async def get_users(self):
        users = await self.repository.get_All()
        if not users:
            raise NotFoundUser("No found Users")

        return [to_user_response(u) for u in users]

    async def get_user_id(self, id: int):
        user = await self.repository.get_user_id(id)
        if not user:
            raise FindUser("No found user")

        return to_user_response(user)

    async def create_user(self, user_data: UserCreate):
        verify_user = await self.repository.get_user_id(user_data.id)
        if verify_user:
            raise AlreadyExistsUser("User already exist")

        created = await self.repository.create(user_data)
        if not created:
            raise NotSucessCreateUser("Falied to create user")

        return to_user_response(created)

        async def update_user(self, id: int user_data: UserUpdate):
            verify_user = await self.repository.get_user_id(id)
            if not verify_user:
                raise FindUser("No found user")
            
            updated = await self.repository.update()
            if not update_user:
                raise NotSucessUpdateUser("Falied to update user")

            return to_user_response(updated)

        async def delete_user(self, id: int):
            verify_user = await self.repository.get_user_id(id)
            if not verify_user:
                raise FindUser("No found user")

            deleted = await self.repository.delete()
            if not deleted: 
                raise NotSucessDeleteUser("Falied to delete user")
            
            return to_user_response(deleted)