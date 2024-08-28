import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from src.api.db.conexion import Base

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    nombre = Column(String(50))
    informacion_general = Column(String(500))
    precio = Column(Float)
    garantia = Column(String(50))
    estado = Column(Boolean)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)