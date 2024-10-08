from src.api.db.schemas.s_almacen import AlmacenCreate, AlmacenResponse, AlmacenUpdate
from src.api.db.schemas.s_response import AlmacenMensajeDato, Mensaje
from src.controllers.c_almacenes import c_obtener_todos_los_almacenes, c_crear_almacen, c_actualizar_almacen, c_eliminar_almacen
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_almacenes = APIRouter()

@gestionar_almacenes.get("/get/almacenes", response_model=List[AlmacenResponse], name="Obtener todos los almacenes")
async def r_obtener_almacenes(db: Session = Depends(get_db)):
    array = c_obtener_todos_los_almacenes(db)
    return array

@gestionar_almacenes.post("/post/almacen", response_model=Mensaje, name="Crear un almacen")
async def r_crear_almacen(entrada: AlmacenCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_crear_almacen(db, entrada):
        respuesta = Mensaje(
            detail="Almacen creado exitosamente",
        )
        return respuesta
    
@gestionar_almacenes.put("/put/almacen/{id}", response_model=Mensaje, name="Actualizar un almacén")
async def r_actualizar_almacen(id:str, entrada: AlmacenUpdate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_actualizar_almacen(db, id, entrada):
        respuesta = Mensaje(
            detail="Almacén actualizado exitosamente",
        )
        return respuesta
    
@gestionar_almacenes.delete("/delete/almacen/{id}", response_model=Mensaje, name="Eliminar un almacén")
async def r_eliminar_almacen(id:str, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_eliminar_almacen(db, id):
        respuesta = Mensaje(
            detail="Almacén eliminado exitosamente",
        )
        return respuesta