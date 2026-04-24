from typing import Optional
from pydantic import BaseModel


class ServiceBase(BaseModel):
    name: str
    description: Optional[str]
    duration_minutes: int
    price: float

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    name: str | None
    description: Optional[str] | None
    duration_minutes: int | None
    price: float | None

class ServiceResponse(ServiceBase):
    id: int

    class Config:
        from_attributes = True