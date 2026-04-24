from sqlalchemy import Column, Integer, Numeric, String
from app.infrastructure.database.connection import Base

class Service(Base):

    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    price = Column(Numeric(10,2), default=0.0)