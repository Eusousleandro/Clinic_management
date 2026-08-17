from app.infrastructure.models.user_model import User
from app.interface.schemas.user_schema import UserResponse

def to_users_response(user: User) -> UserResponse:
    return UserResponse(
        id=user.id,
        name=user.name,
        email=user.email,
        role=user.role
    )