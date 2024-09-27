import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, BLOB
from src.api.db.conexion import Base

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    nombre = Column(String(50))
    #imagen = BLOB()
    informacion_general = Column(String(500))
    precio = Column(Float)
    garantia = Column(String(50))
    imagen = Column(String(1000))
    estado = Column(Boolean)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)