from sqlalchemy import Column, Integer, String
from src.api.db.conexion import Base

class Rol(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))