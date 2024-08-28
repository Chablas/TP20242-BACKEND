import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Orden_Compra_Detalle(Base):
    __tablename__ = "ordenes_compra_detalle"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    orden_id = Column(Integer)
    producto_id = Column(Integer)
    cantidad = Column(Integer)
    movimiento_id = Column(Integer)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)