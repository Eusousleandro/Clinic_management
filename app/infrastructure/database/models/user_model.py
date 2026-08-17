from sqlalchemy import Column, Integer, String
from app.infrastructure.database.connection import Base

class User(Base):
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False)