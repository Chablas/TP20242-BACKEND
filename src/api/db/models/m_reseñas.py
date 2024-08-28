import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base

class Reseña(Base):
    __tablename__ = "reseñas"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    estrellas = Column(Integer)
    comentario = Column(String(1000))
    fecha = Column(DateTime)
    usuario_id = Column(Integer)
    producto_id = Column(Integer)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)