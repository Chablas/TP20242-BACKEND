import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    nombre = Column(String(50))
    descripcion = Column(String(100))
    imagen = Column(String(1000))
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)