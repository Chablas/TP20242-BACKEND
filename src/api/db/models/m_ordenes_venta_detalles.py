import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Orden_Venta_Detalle(Base):
    __tablename__ = "ordenes_venta_detalle"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    orden_id = Column(Integer)
    producto_id = Column(Integer)
    cantidad = Column(Integer)
    movimiento_id = Column(Integer)
    fecha_entrega = Column(DateTime)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)