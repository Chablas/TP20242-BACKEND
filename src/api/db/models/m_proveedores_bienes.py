import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Proveedor_Bien(Base):
    __tablename__ = "proveedores_bienes"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    precio = Column(Float)
    codigo = Column(String(50))
    proveedor_id = Column(Integer)
    bien_id = Column(Integer)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)