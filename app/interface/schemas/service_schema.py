from typing import Optional
from pydantic import BaseModel


class ServiceBase(BaseModel):
    name: str
    duration_minutes: int
    price: float

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    name: str | None
    duration_minutes: int | None
    price: float | None

class ServiceResponse(BaseModel):
    id: int
    name: str
    duration_minutes: int
    price: float

    class Config:
        from_attributes = True