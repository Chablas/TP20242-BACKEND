from src.api.db.schemas.s_producto_almacen import ProductoAlmacenCreate, ProductoAlmacenCompleto, ProductoAlmacenResponse
from src.api.db.schemas.s_response import BienMensajeDato, Mensaje, ProductoAlmacenResponse
from src.controllers.c_productos_almacenes import c_aumentar_stock, c_disminuir_stock, c_obtener_todos_los_stock, c_obtener_stock_de_un_producto_en_almacenes, c_obtener_stock_de_almacen
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_productos_almacenes = APIRouter()

@gestionar_productos_almacenes.get("/get/stock", response_model=List[ProductoAlmacenResponse], name="Obtener todos los stocks")
async def r_obtener_productos_almacenes(db: Session = Depends(get_db)):
    array = c_obtener_todos_los_stock(db)
    return array

@gestionar_productos_almacenes.get("/get/almacen/{id}", response_model=List[ProductoAlmacenResponse], name="Obtener los almacenes que contienen cierto producto")
async def r_obtener_stock_de_almacen(almacen_id:str, db: Session = Depends(get_db)):
    array = c_obtener_stock_de_almacen(db, almacen_id)
    return array

@gestionar_productos_almacenes.get("/get/producto/{id}", response_model=List[ProductoAlmacenResponse], name="Obtener todo el stock de un almacén")
async def r_obtener_stock_de_un_producto_en_almacenes(producto_id:str, db: Session = Depends(get_db)):
    array = c_obtener_stock_de_un_producto_en_almacenes(db, producto_id)
    return array

@gestionar_productos_almacenes.put("/put/stock/aumentar", response_model=Mensaje, name="Aumentar stock de un producto en un almacen")
async def r_aumentar_producto_almacen(entrada: ProductoAlmacenCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_aumentar_stock(db, entrada):
        respuesta = Mensaje(
            detail="Stock actualizado exitosamente",
        )
        return respuesta

@gestionar_productos_almacenes.put("/put/stock/disminuir", response_model=Mensaje, name="Disminuir stock de un producto en un almacen")
async def r_disminuir_producto_almacen(entrada: ProductoAlmacenCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_disminuir_stock(db, entrada):
        respuesta = Mensaje(
            detail="Stock actualizado exitosamente",
        )
        return respuesta