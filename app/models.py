from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase

# Definición de Base (Crucial para Pytest y SQLAlchemy 2.0)
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)

from pydantic import BaseModel

# Esquema para validar la entrada de datos
class UserCreate(BaseModel):
    username: str
    email: str