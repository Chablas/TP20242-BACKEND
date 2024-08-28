import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Usuario_Rol(Base):
    __tablename__ = "usuarios_roles"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    usuario_id = Column(Integer)
    rol_id = Column(Integer)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)