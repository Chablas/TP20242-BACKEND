import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Producto_Almacen(Base):
    __tablename__ = "productos_almacenes"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    producto_id = Column(Integer)
    almacen_id = Column(Integer)
    cantidad = Column(Integer)
    #created_at = Column(String(19))
    #updated_at = DateTime(default=datetime.datetime.utcnow)