from src.api.db.models.m_roles import Rol as RolModel
from src.api.db.schemas.s_roles import RolCreate, RolUpdate, RolResponse
from fastapi import HTTPException, status

def c_obtener_todos_los_roles(db):
    try:
        roles = db.query(RolModel).all()
        array_datos = []
        for rol in roles:
            array_datos.append(rol)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_crear_rol(db, entrada:RolCreate):
    # Validaciones inicio
    entrada.nombre = entrada.nombre.strip()
    entrada.nombre = entrada.nombre.upper()
    if entrada.nombre == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo nombre está vacío")
    validacion = db.query(RolModel).filter(RolModel.nombre==entrada.nombre).first()
    if validacion is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del rol ya existe")
    # Validaciones fin
    try:
        datos = RolModel(
            nombre = entrada.nombre,
        )
        db.add(datos)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_actualizar_rol(db, id:str, entrada:RolUpdate):
    # Validaciones inicio
    entrada.nombre = entrada.nombre.strip()
    entrada.nombre = entrada.nombre.upper()
    if entrada.nombre == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo nombre está vacío")
    validacion=db.query(RolModel).filter(RolModel.id==id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El rol no existe")
    validacion2 = db.query(RolModel).filter(RolModel.nombre==entrada.nombre).first()
    if validacion2 is not None:
        if validacion2.id != validacion.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del rol ya existe")
    # Validaciones fin
    try:
        rol = db.query(RolModel).filter(RolModel.id==id).first()
        rol.nombre = entrada.nombre
        db.commit()
        db.refresh(rol)
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_eliminar_rol(db, id:str):
    # Validaciones inicio
    validacion=db.query(RolModel).filter(RolModel.id==id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El rol no existe")
    # Validaciones fin
    try:
        rol = db.query(RolModel).filter(RolModel.id==id).first()
        db.delete(rol)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")