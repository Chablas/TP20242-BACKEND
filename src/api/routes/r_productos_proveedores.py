from src.api.db.schemas.s_proveedor_bien import ProveedorBienCreate, ProveedorBienDelete, ProveedorBienResponse
from src.api.db.schemas.s_response import  Mensaje, ProductoAlmacenResponse
from src.api.db.schemas.s_movimiento import HistorialMovimientoResponse
from src.controllers.c_proveedores_bienes import c_obtener_proveedores_de_un_producto, c_añadir_producto_a_proveedor, c_obtener_productos_de_proveedor, c_obtener_todos_los_productos_de_los_proveedores, c_quitar_producto_a_proveedor
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_proveedores_bienes = APIRouter()

@gestionar_proveedores_bienes.get("/get/bienes_proveedor/all", response_model=List[ProveedorBienResponse], name="Obtener todos bienes de todos los proveedores")
async def r_obtener_todos_los_productos_de_los_proveedores(db: Session = Depends(get_db)):
    array = c_obtener_todos_los_productos_de_los_proveedores(db)
    return array

@gestionar_proveedores_bienes.get("/get/bienes_proveedor/{bien_id}", response_model=List[ProveedorBienResponse], name="Obtener todos los proveedores que ofrecen un bien")
async def r_obtener_proveedores_de_un_producto(bien_id:int, db: Session = Depends(get_db)):
    array = c_obtener_proveedores_de_un_producto(db, bien_id)
    return array

@gestionar_proveedores_bienes.get("/get/bienes_proveedor/{proveedor_id}", response_model=List[ProveedorBienResponse], name="Obtener los bienes que que ofrece un proveedor")
async def r_obtener_productos_de_proveedor(proveedor_id:int, db: Session = Depends(get_db)):
    array = c_obtener_productos_de_proveedor(db, proveedor_id)
    return array

@gestionar_proveedores_bienes.put("/put/bienes_proveedor/agregar", response_model=Mensaje, name="Añadir un bien a un proveedor")
async def r_añadir_producto_a_proveedor(entrada: ProveedorBienCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_añadir_producto_a_proveedor(db, entrada):
        respuesta = Mensaje(
            detail="Stock actualizado exitosamente",
        )
        return respuesta

@gestionar_proveedores_bienes.put("/put/bienes_proveedor/quitar", response_model=Mensaje, name="Quitar un bien a un proveedor")
async def r_disminuir_producto_almacen(entrada: ProveedorBienDelete, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_quitar_producto_a_proveedor(db, entrada):
        respuesta = Mensaje(
            detail="Stock actualizado exitosamente",
        )
        return respuesta