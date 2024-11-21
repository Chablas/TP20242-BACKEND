from src.api.db.schemas.s_roles import RolCreate, RolResponse, RolUpdate
from src.api.db.schemas.s_response import BienMensajeDato, Mensaje
from src.controllers.c_roles import c_actualizar_rol, c_crear_rol, c_eliminar_rol, c_obtener_todos_los_roles
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_roles = APIRouter()

@gestionar_roles.get("/get/roles", response_model=List[RolResponse], name="Obtener todos los roles")
async def r_obtener_roles(db: Session = Depends(get_db)):
    array = c_obtener_todos_los_roles(db)
    return array

@gestionar_roles.post("/post/rol", response_model=Mensaje, name="Crear un rol")
async def r_crear_rol(entrada: RolCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_crear_rol(db, entrada):
        respuesta = Mensaje(
            detail="Rol creado exitosamente",
        )
        return respuesta
    
@gestionar_roles.put("/put/rol/{id}", response_model=Mensaje, name="Actualizar un rol")
async def r_actualizar_rol(id:str, entrada: RolUpdate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_actualizar_rol(db, id, entrada):
        respuesta = Mensaje(
            detail="Categoria actualizada exitosamente",
        )
        return respuesta
    
@gestionar_roles.delete("/delete/rol/{id}", response_model=Mensaje, name="Eliminar un rol")
async def r_eliminar_rol(id:str, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_eliminar_rol(db, id):
        respuesta = Mensaje(
            detail="Rol eliminado exitosamente",
        )
        return respuesta