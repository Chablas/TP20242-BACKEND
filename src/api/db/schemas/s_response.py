from src.api.db.schemas.s_almacen import AlmacenResponse
from src.api.db.schemas.s_bien import BienResponse
from src.api.db.schemas.s_producto_almacen import ProductoAlmacenResponse
from src.api.db.schemas.s_proveedor_bien import ProveedorBienResponse
from src.api.db.schemas.s_proveedor import ProveedorResponse
from src.api.db.schemas.s_servicio import ServicioResponse
from src.api.db.schemas.s_usuarios import UsuarioResponse
from pydantic import BaseModel
from typing import List

class Mensaje(BaseModel):
    mensaje:str

class AlmacenMensajeDato(BaseModel):
    mensaje:str
    dato: AlmacenResponse

class BienMensajeDato(BaseModel):
    mensaje:str
    dato: BienResponse

class ProductoAlmacenMensajeDato(BaseModel):
    mensaje:str
    dato: ProductoAlmacenResponse

class ProveedorBienMensajeDato(BaseModel):
    mensaje:str
    dato: ProveedorBienResponse

class ProveedorMensajeDato(BaseModel):
    mensaje:str
    dato: ProveedorResponse

class ServicioMensajeDato(BaseModel):
    mensaje:str
    dato: ServicioResponse

class UsuarioMensajeDato(BaseModel):
    mensaje:str
    dato: UsuarioResponse