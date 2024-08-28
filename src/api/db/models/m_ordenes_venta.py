import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Orden_Venta(Base):
    __tablename__ = "ordenes_venta"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    usuario_id = Column(Integer)
    total = Column(Float)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)