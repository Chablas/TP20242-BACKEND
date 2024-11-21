from sqlalchemy import Column, Integer, String
from src.api.db.conexion import Base

class Movimiento_Almacen(Base):
    __tablename__ = "movimientos_almacenes"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    producto_id = Column(Integer)
    almacen_id = Column(Integer)
    cantidad = Column(Integer)
    tipo_movimiento = Column(String(7))
    created_at = Column(String(19))
    #updated_at = DateTime(default=datetime.datetime.utcnow)