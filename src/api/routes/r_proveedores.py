from src.api.db.schemas.s_proveedor import ProveedorCreate, ProveedorResponse, ProveedorUpdate
from src.api.db.schemas.s_response import BienMensajeDato, Mensaje
from src.controllers.c_proveedores import c_crear_proveedor, c_obtener_todos_los_proveedores, c_actualizar_proveedor, c_eliminar_proveedor
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_proveedores = APIRouter()

@gestionar_proveedores.get("/get/proveedores", response_model=List[ProveedorResponse], name="Obtener todos los proveedores")
async def r_obtener_proveedores(db: Session = Depends(get_db)):
    array = c_obtener_todos_los_proveedores(db)
    return array

@gestionar_proveedores.post("/post/proveedor", response_model=Mensaje, name="Crear un proveedor")
async def r_crear_proveedor(entrada: ProveedorCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_crear_proveedor(db, entrada):
        respuesta = Mensaje(
            detail="Proveedor creado exitosamente",
        )
        return respuesta
    
@gestionar_proveedores.put("/put/proveedor/{id}", response_model=Mensaje, name="Actualizar un proveedor")
async def r_actualizar_proveedor(id:str, entrada: ProveedorUpdate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_actualizar_proveedor(db, id, entrada):
        respuesta = Mensaje(
            detail="Proveedor actualizado exitosamente",
        )
        return respuesta
    
@gestionar_proveedores.delete("/delete/proveedor/{id}", response_model=Mensaje, name="Eliminar un proveedor")
async def r_eliminar_proveedor(id:str, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_eliminar_proveedor(db, id):
        respuesta = Mensaje(
            detail="Proveedor eliminado exitosamente",
        )
        return respuesta