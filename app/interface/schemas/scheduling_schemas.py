from datetime import time
from typing import Optional

from pydantic import BaseModel

class SchedulingSchema(BaseModel):
    name: str
    description: Optional[str] = None
    start_time: time
    end_time: time
    is_active: bool

class SchedulingCreate(SchedulingSchema):
    pass

class SchedulingUpdate(SchedulingSchema):
    name: str | None = None
    description: Optional[str] | None = None
    start_time: time | None = None
    end_time: time | None = None
    is_active: bool | None = None

class SchedulingResponse(SchedulingSchema):
    id: int

    class Config:
        orm_mode = True