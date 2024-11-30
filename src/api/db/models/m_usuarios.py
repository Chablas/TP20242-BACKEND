from sqlalchemy import Column, Integer, String, Boolean
from src.api.db.conexion import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50))
    password = Column(String(60))
    #nombres = Column(String(50))
    #apellidos = Column(String(50))
    #tipo_documento = Column(String(50))
    #numero_documento = Column(Integer)
    #celular = Column(Integer)
    #correo = Column(String(50))
    #contraseña = Column(String(50))
    islogged = Column(Boolean, default=False)
    #created_at = DateTime(default=datetime.datetime.utcnow)
    #updated_at = DateTime(default=datetime.datetime.utcnow)