import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from src.api.db.conexion import Base
import pytz

LIMA_TZ = pytz.timezone("America/Lima")

class Producto_Almacen(Base):
    __tablename__ = "productos_almacenes"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    producto_id = Column(Integer)
    almacen_id = Column(Integer)
    cantidad = Column(Integer)
    created_at = Column(DateTime, default=lambda: datetime.datetime.now(LIMA_TZ))
    #updated_at = DateTime(default=datetime.datetime.utcnow)