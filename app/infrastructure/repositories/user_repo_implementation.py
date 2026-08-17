from sqlalchemy.orm import Session
from app.domain.repository.user_repository import IUserRepository
from app.infrastructure.database.models.user_model import User
from app.interface.schemas.user_schema import UserCreate, UserUpdate

class UserRepository(user: IUserRepository):
    def __init__(self, db: Session):
        self.db = db
    
    async def get_All(self):
        return self.db.query(User).all()
    
    async def get_user_id(self, id: int):
        return self.db.query(User).filter(User.id == id).first()

    async def create(self, user_data: UserCreate):
        new_user = User(**user_data.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    async def update(self, user_data: UserUpdate):
        user =  self.db.query(User).filter(User.id == id).first()
        update = update_data.model_dump(exclude_unset=True)

        for key, value in user_data.items():
            setattr(user, key, value)
        
        self.db.commit()
        self.db.refresh(user)
        return user

    async def delete(self, id: int):
        user =  self.db.query(User).filter(User.id == id).first()
        self.db.delete(user)
        self.db.commit()
        return user
