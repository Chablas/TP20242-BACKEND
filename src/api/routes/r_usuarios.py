from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from src.api.db.models.m_usuarios import Usuario
from src.api.db.schemas.s_usuarios import UsuarioSesion, UsuarioCreate, UsuarioResponse, UsuarioLogin
from src.api.db.schemas.s_response import UsuarioMensajeDato, Mensaje, Token
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user, create_access_token, authenticate_user
from src.controllers.c_usuarios import crear_usuario, c_login, c_logout, c_obtener_usuario_por_email, c_obtener_todos_los_usuarios
from typing import List
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

gestionar_usuarios = APIRouter()

@gestionar_usuarios.get("/get/usuarios", response_model=List[UsuarioResponse], name="Obtener todos los usuarios")
async def r_obtener_usuarios(db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    array = c_obtener_todos_los_usuarios(db)
    return array

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
    
@gestionar_usuarios.post("/api/token", response_model=Token, name="Generar token")
async def r_devolver_token(entrada: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    usuario = authenticate_user(entrada.username, entrada.password, db)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Credenciales inválidas")
    token = create_access_token(usuario.email, usuario.id, timedelta(minutes=20))
    respuesta = Token(
        access_token = token,
        token_type = "bearer"
    )
    return respuesta