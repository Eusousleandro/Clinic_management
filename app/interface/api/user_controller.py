from fastapi import APIRouter, Depends

from app.application.use_cases.user import UserService
from app.interface.schemas.user_schema import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/", response_model=List[UserResponse])
async def list_users(
    users: User = Depends()
):
    return await users.get_users()

@router.get("/{id}", response_model=UserResponse)
async def list_unique_user(
    id: int
):
    return await user.get_user_id(id)

@router.post("/create", response_model=UserResponse)
async def create_user(
    user: UserCreate,
):
    return await user.create_user(user)

@router.put("/update/{id}", response_model=UserResponse)
async update_user(
    id: int,
    user: UserUpdate
):
    return await user.update_user(id, user)

@router.delete("/delete/{id}", response_model=UserResponse)
async delete_user(
    id: int
):
    return await user.delete_user(id)