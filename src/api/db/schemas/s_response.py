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
    detail:str

class MensajeID(BaseModel):
    detail:int

class AlmacenMensajeDato(BaseModel):
    detail:str
    dato: AlmacenResponse

class BienMensajeDato(BaseModel):
    detail:str
    dato: BienResponse

class ProductoAlmacenMensajeDato(BaseModel):
    detail:str
    dato: ProductoAlmacenResponse

class ProveedorBienMensajeDato(BaseModel):
    detail:str
    dato: ProveedorBienResponse

class ProveedorMensajeDato(BaseModel):
    detail:str
    dato: ProveedorResponse

class ServicioMensajeDato(BaseModel):
    detail:str
    dato: ServicioResponse

class UsuarioMensajeDato(BaseModel):
    detail:str
    dato: UsuarioResponse

class Token(BaseModel):
    access_token: str
    token_type: str 