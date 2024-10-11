from src.api.db.models.m_usuarios import Usuario as UsuarioModel
from src.auth.auth import bcrypt_context
from src.api.db.schemas.s_usuarios import UsuarioCreate, UsuarioSesion, UsuarioResponse
from fastapi import HTTPException, status

def c_obtener_todos_los_usuarios(db):
    try:
        usuarios = db.query(UsuarioModel).all()
        array_datos = []
        for usuario in usuarios:
            array_datos.append(usuario)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_obtener_usuario_por_email(db, entrada):
    # Validaciones inicio
    usuario=db.query(UsuarioModel).filter(UsuarioModel.email==entrada).first()
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El email no existe")
    # Validaciones fin
    try:
        respuesta = UsuarioResponse(
            email=usuario.email,
            password=usuario.password,
            islogged=usuario.islogged
        )
        return respuesta
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def crear_usuario(db, entrada:UsuarioCreate):
    # Validaciones inicio
    validacion = db.query(UsuarioModel).filter(UsuarioModel.email==entrada.email).first()
    if validacion is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El email ya existe")
    # Validaciones fin
    try:
        usuario = UsuarioModel(email=entrada.email, password=bcrypt_context.hash(entrada.password))
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_login(db, entrada:UsuarioSesion):
    # Validaciones inicio
    usuario=db.query(UsuarioModel).filter(UsuarioModel.email==entrada.email).first()
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El email no existe")
    # Validaciones fin
    try:
        query_result = db.query(UsuarioModel).filter(UsuarioModel.email==entrada.email).first()
        if query_result:
            query_result.islogged = True
            db.commit()
            return True
        else:
            return False
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_logout(db, entrada:UsuarioSesion):
    # Validaciones inicio
    usuario=db.query(UsuarioModel).filter(UsuarioModel.email==entrada.email).first()
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El email no existe")
    # Validaciones fin
    try:
        query_result = db.query(UsuarioModel).filter(UsuarioModel.email==entrada.email).first()
        if query_result:
            query_result.islogged = False
            db.commit()
            return True
        else:
            return False
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")