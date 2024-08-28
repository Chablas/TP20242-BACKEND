from src.api.db.models.m_almacenes import Almacen as AlmacenModel
from src.api.db.schemas.s_almacen import AlmacenCreate, AlmacenResponse
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