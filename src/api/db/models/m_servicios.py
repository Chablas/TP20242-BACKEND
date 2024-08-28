import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Servicio(Base):
    __tablename__ = "servicios"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    condiciones_previas = Column(String(1000))
    servicio_incluye = Column(String(1000))
    servicio_no_incluye = Column(String(1000))
    restricciones = Column(String(1000))
    producto_id = Column(String(50))
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)