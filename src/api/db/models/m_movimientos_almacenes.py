import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Movimiento_Almacen(Base):
    __tablename__ = "movimientos_almacenes"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    productos_almacenes_id = Column(Integer)
    tipo_movimiento = Column(Integer)
    cantidad = Column(Integer)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)