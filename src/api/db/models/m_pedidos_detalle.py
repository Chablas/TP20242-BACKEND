from sqlalchemy import Column, Integer, String, Float
from src.api.db.conexion import Base

class PedidosDetalle(Base):
    __tablename__ = "pedidos_detalle"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    pedido_id = Column(Integer)
    producto_id = Column(Float)
    cantidad = Column(String(19))
    #updated_at = DateTime(default=datetime.datetime.utcnow)