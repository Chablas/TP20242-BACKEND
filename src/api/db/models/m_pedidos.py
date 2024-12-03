from sqlalchemy import Column, Integer, String, Float
from src.api.db.conexion import Base

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    usuario_id = Column(Integer)
    total = Column(Float)
    estado = Column(String(19))
    created_at = Column(String(19))
    #updated_at = DateTime(default=datetime.datetime.utcnow)