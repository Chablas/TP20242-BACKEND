import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Proveedor(Base):
    __tablename__ = "proveedores"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    nombre = Column(String(50))
    ruc = Column(Integer)
    direccion = Column(String(150))
    correo = Column(String(50))
    telefono = Column(Integer)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)