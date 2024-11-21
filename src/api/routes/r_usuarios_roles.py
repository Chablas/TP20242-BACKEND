from src.api.db.schemas.s_usuario_roles import UsuarioRolCreate, UsuarioRolResponse, UsuarioRolDelete
from src.api.db.schemas.s_response import BienMensajeDato, Mensaje
from src.controllers.c_usuarios_roles import c_obtener_todos_los_usuarios_roles, c_añadir_rol_a_usuario, c_obtener_roles_de_usuario, c_obtener_usuarios_de_rol, c_quitar_rol_a_usuario
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_usuarios_roles = APIRouter()

@gestionar_usuarios_roles.get("/get/usuario_rol/all", response_model=List[UsuarioRolResponse], name="Obtener todas roles asignados a todos los usuarios")
async def r_obtener_todos_los_usuarios_roles(db: Session = Depends(get_db)):
    array = c_obtener_todos_los_usuarios_roles(db)
    return array

@gestionar_usuarios_roles.get("/get/usuario_rol/rol/{rol_id}", response_model=List[UsuarioRolResponse], name="Obtener todos los usuarios con un rol en específico")
async def r_obtener_usuarios_de_rol(rol_id:int, db: Session = Depends(get_db)):
    return c_obtener_usuarios_de_rol(db, rol_id)

@gestionar_usuarios_roles.get("/get/usuario_rol/usuario/{usuario_id}", response_model=List[UsuarioRolResponse], name="Obtener todos los roles asignados a un usuario en específico")
async def r_obtener_roles_de_usuario(usuario_id:int, db: Session = Depends(get_db)):
    return c_obtener_roles_de_usuario(db, usuario_id)

@gestionar_usuarios_roles.post("/post/usuario_rol", response_model=Mensaje, name="Añadir un rol a un usuario")
async def r_añadir_rol_a_usuario(entrada: UsuarioRolCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_añadir_rol_a_usuario(db, entrada):
        respuesta = Mensaje(
            detail="Rol añadido exitosamente",
        )
        return respuesta
    
@gestionar_usuarios_roles.delete("/delete/usuario_rol", response_model=Mensaje, name="Quitar un rol a un usuario")
async def r_eliminar_rol_a_usuario(entrada:UsuarioRolDelete, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_quitar_rol_a_usuario(db, entrada):
        respuesta = Mensaje(
            detail="Rol quitado exitosamente",
        )
        return respuesta