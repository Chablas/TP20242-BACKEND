from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from src.api.db.models.m_usuarios import Usuario
from src.api.db.schemas.s_usuarios import UsuarioSesion, UsuarioCreate
from src.api.db.schemas.s_response import UsuarioMensajeDato, Mensaje
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from src.controllers.c_usuarios import crear_usuario, c_login, c_logout, c_obtener_usuario_por_email
from typing import List

gestionar_usuarios = APIRouter()
"""
@gestionar_usuarios.get("/get/usuarios", response_model=List[UsuarioCompleto], name="Obtener todos los usuarios")
async def obtener_usuarios(db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    usuarios=db.query(Usuario).all()
    return 
"""
@gestionar_usuarios.get("/get/usuario/{email}", response_model=UsuarioMensajeDato, name="Obtener un usuario por su correo")
async def obtener_usuarios(email:str, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    respuesta = c_obtener_usuario_por_email(db, email)
    response = UsuarioMensajeDato(
        detail= 'Usuario obtenido exitosamente',
        dato=respuesta
    )
    return response

@gestionar_usuarios.post("/post/usuarios", response_model=Mensaje, name="Crear un usuario")
async def crear_nuevo_usuario(entrada: UsuarioCreate, db: Session = Depends(get_db)):
    if crear_usuario(db, entrada):
        respuesta = Mensaje(
            detail = "Usuario creado exitosamente"
        )
        return respuesta
    else:
        respuesta = Mensaje(
            detail = "Error en la base de datos"
        )
        return respuesta
    
@gestionar_usuarios.put('/put/login', response_model=Mensaje, name="Activar sesión")
async def actualizar_is_logged(entrada:UsuarioSesion, db: Session = Depends(get_db)):
    if c_login(db, entrada):
        respuesta = Mensaje(
            detail = "Inicio de sesión exitoso"
        )
        return respuesta
    else:
        respuesta = Mensaje(
            detail = "Error en la base de datos"
        )
        return respuesta
    
@gestionar_usuarios.put('/put/logout', response_model=Mensaje, name="Desactivar sesión")
async def actualizar_is_logged(entrada:UsuarioSesion, db: Session = Depends(get_db)):
    if c_logout(db, entrada):
        respuesta = Mensaje(
            detail = "Cierre de sesión exitoso"
        )
        return respuesta
    else:
        respuesta = Mensaje(
            detail = "Error en la base de datos"
        )
        return respuesta