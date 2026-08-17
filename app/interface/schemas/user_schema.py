from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    name: str 
    email: str
    password: str
    role: str

class UseCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: str  | None
    email: str | None
    password: str | None
    role: str | None

class UserResponse(BaseModel):
    id: int
    name: str 
    email: str
    password: str
    role: str

model_config= ConfigDict(from_attributes= True)