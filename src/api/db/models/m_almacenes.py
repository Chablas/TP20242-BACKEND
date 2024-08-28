import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Almacen(Base):
    __tablename__ = "almacenes"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    nombre = Column(String(100))
    ubicacion = Column(String(100))
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)