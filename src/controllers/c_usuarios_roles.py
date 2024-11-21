from src.api.db.models.m_usuarios_roles import Usuario_Rol as Usuario_RolModel
from src.api.db.models.m_roles import Rol as RolModel
from src.api.db.models.m_usuarios import Usuario as UsuarioModel
from src.api.db.schemas.s_usuario_roles import UsuarioRolCreate, UsuarioRolDelete
from fastapi import HTTPException, status
from datetime import datetime

def c_obtener_todos_los_usuarios_roles(db):
    try:
        usuarios_roles = db.query(Usuario_RolModel).all()
        array_datos = []
        for usuarios_rol in usuarios_roles:
            array_datos.append(usuarios_rol)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_obtener_usuarios_de_rol(db, rol_id:int):
    if rol_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo rol_id está vacío")
    validacion = db.query(RolModel).filter(RolModel.id==rol_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El rol no existe")
    try:
        rol_usuarios = db.query(Usuario_RolModel).filter(Usuario_RolModel.rol_id==rol_id).all()
        array_datos = []
        for rol_usuario in rol_usuarios:
            array_datos.append(rol_usuario)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_obtener_roles_de_usuario(db, usuario_id:int):
    if usuario_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo usuario_id está vacío")
    validacion = db.query(UsuarioModel).filter(UsuarioModel.id==usuario_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe")
    try:
        usuario_roles = db.query(Usuario_RolModel).filter(Usuario_RolModel.usuario_id==usuario_id).all()
        array_datos = []
        for usuario_rol in usuario_roles:
            array_datos.append(usuario_rol)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_añadir_rol_a_usuario(db, entrada:UsuarioRolCreate):
    # Validaciones inicio
    if entrada.usuario_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo usuario_id está vacío")
    if entrada.rol_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo rol_id está vacío")
    validacion = db.query(UsuarioModel).filter(UsuarioModel.id==entrada.usuario_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe")
    validacion = db.query(RolModel).filter(RolModel.id==entrada.rol_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El rol no existe")
    validacion = db.query(Usuario_RolModel).filter(Usuario_RolModel.usuario_id==entrada.usuario_id, Usuario_RolModel.rol_id==entrada.rol_id).first()
    if validacion is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario ya posee ese rol")
    # Validaciones fin
    try:
        datos = Usuario_RolModel(
            usuario_id = entrada.usuario_id,
            rol_id = entrada.rol_id,
        )
        db.add(datos)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_quitar_rol_a_usuario(db, entrada:UsuarioRolDelete):
    # Validaciones inicio
    if entrada.usuario_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo usuario_id está vacío")
    if entrada.rol_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo rol_id está vacío")
    validacion = db.query(UsuarioModel).filter(UsuarioModel.id==entrada.usuario_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe")
    validacion = db.query(RolModel).filter(RolModel.id==entrada.rol_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El rol no existe")
    validacion = db.query(Usuario_RolModel).filter(Usuario_RolModel.usuario_id==entrada.usuario_id, Usuario_RolModel.rol_id==entrada.rol_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no posee ese rol")
    # Validaciones fin
    try:
        db.delete(validacion)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")