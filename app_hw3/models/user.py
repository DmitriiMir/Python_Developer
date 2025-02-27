from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app_hw3.backend.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    # Связь с таблицей Task
    tasks = relationship("Task", back_populates="user")
