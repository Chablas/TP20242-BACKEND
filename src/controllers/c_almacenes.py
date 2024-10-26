from src.api.db.models.m_almacenes import Almacen as AlmacenModel
from src.api.db.schemas.s_almacen import AlmacenCreate, AlmacenResponse, AlmacenUpdate
from fastapi import HTTPException, status

def c_obtener_todos_los_almacenes(db):
    try:
        almacenes = db.query(AlmacenModel).all()
        array_datos = []
        for almacen in almacenes:
            array_datos.append(almacen)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_crear_almacen(db, entrada:AlmacenCreate):
    # Validaciones inicio
    entrada.nombre = entrada.nombre.strip()
    entrada.ubicacion = entrada.ubicacion.strip()
    if entrada.nombre == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El campo nombre está vacío")
    if entrada.ubicacion == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El campo ubicación está vacío")

    validacion = db.query(AlmacenModel).filter(AlmacenModel.nombre==entrada.nombre).first()
    if validacion is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del Almacén ya existe")
    # Validaciones fin
    try:
        datos = AlmacenModel(
            nombre = entrada.nombre,
            ubicacion = entrada.ubicacion,
        )
        db.add(datos)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_actualizar_almacen(db, id:str, entrada:AlmacenUpdate):
    # Validaciones inicio
    entrada.nombre = entrada.nombre.strip()
    entrada.ubicacion = entrada.ubicacion.strip()
    if entrada.nombre == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El campo nombre está vacío")
    if entrada.ubicacion == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El campo ubicación está vacío")
    
    validacion=db.query(AlmacenModel).filter(AlmacenModel.id==id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El almacén no existe")
    validacion=db.query(AlmacenModel).filter(AlmacenModel.nombre==entrada.nombre).first()
    if validacion is not None:
        if validacion.id != entrada.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del Almacén ya existe")
    # Validaciones fin
    try:
        almacen = db.query(AlmacenModel).filter(AlmacenModel.id==id).first()
        almacen.nombre = entrada.nombre
        almacen.ubicacion = entrada.ubicacion
        db.commit()
        db.refresh(almacen)
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_eliminar_almacen(db, id:str):
    # Validaciones inicio
    validacion=db.query(AlmacenModel).filter(AlmacenModel.id==id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El almacén no existe")
    # Validaciones fin
    try:
        almacen = db.query(AlmacenModel).filter(AlmacenModel.id==id).first()
        db.delete(almacen)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")