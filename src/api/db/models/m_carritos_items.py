import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Carrito_Items(Base):
    __tablename__ = "carritos_items"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    carrito_id = Column(Integer)
    producto_id = Column(Integer)
    cantidad = Column(Integer)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)