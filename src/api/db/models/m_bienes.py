import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Bien(Base):
    __tablename__ = "bienes"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    marca = Column(String(50))
    especificaciones_tecnicas = Column(String(1000))
    producto_id = Column(Integer)
    categoria_id = Column(Integer)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)