from src.api.db.schemas.s_producto_almacen import ProductoAlmacenCreate, ProductoAlmacenCompleto, ProductoAlmacenResponse
from src.api.db.schemas.s_response import BienMensajeDato, Mensaje
from src.controllers.c_productos_almacenes import c_aumentar_stock
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_productos_almacenes = APIRouter()

@gestionar_productos_almacenes.put("/put/stock", response_model=Mensaje, name="Actualizar stock de un producto en un almacen")
async def r_actualizar_producto_almacen(entrada: ProductoAlmacenCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_aumentar_stock(db, entrada):
        respuesta = Mensaje(
            detail="Stock actualizado exitosamente",
        )
        return respuesta