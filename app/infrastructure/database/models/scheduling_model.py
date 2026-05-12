from sqlalchemy import Column, Integer, String, DateTime, Boolean, Time
from datetime import datetime, UTC

from app.infrastructure.database.connection import Base

class Scheduling(Base):

    __tablename__ = 'schedulings'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(UTC)
    )

    updated_at = Column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(UTC), 
        onupdate=lambda: datetime.now(UTC)
    )