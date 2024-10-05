from src.api.db.models.m_proveedores import Proveedor as ProveedorModel
from src.api.db.schemas.s_proveedor import ProveedorCreate, ProveedorResponse, ProveedorUpdate
from fastapi import HTTPException, status

def c_obtener_todos_los_proveedores(db):
    try:
        proveedores = db.query(ProveedorModel).all()
        array_datos = []
        for proveedor in proveedores:
            array_datos.append(proveedor)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_crear_proveedor(db, entrada:ProveedorCreate):
    # Validaciones inicio
    if entrada.nombre == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo nombre está vacío")
    if entrada.ruc == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo ruc está vacío")
    if entrada.direccion == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo direccion está vacío")
    if entrada.correo == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo correo está vacío")
    if entrada.telefono == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo telefono está vacío")
    validacion = db.query(ProveedorModel).filter(ProveedorModel.nombre==entrada.nombre).first()
    if validacion is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del proveedor ya existe")
    # Validaciones fin
    try:
        datos = ProveedorModel(
            nombre = entrada.nombre,
            ruc = entrada.ruc,
            direccion = entrada.direccion,
            correo = entrada.correo,
            telefono = entrada.telefono,
        )
        db.add(datos)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_actualizar_proveedor(db, id:str, entrada:ProveedorUpdate):
    # Validaciones inicio
    if entrada.nombre == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo nombre está vacío")
    if entrada.ruc == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo ruc está vacío")
    if entrada.direccion == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo direccion está vacío")
    if entrada.correo == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo correo está vacío")
    if entrada.telefono == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo telefono está vacío")
    validacion=db.query(ProveedorModel).filter(ProveedorModel.id==id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El proveedor no existe")
    if validacion.nombre == entrada.nombre:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del proveedor ya existe")
    # Validaciones fin
    try:
        proveedor = db.query(ProveedorModel).filter(ProveedorModel.id==id).first()
        proveedor.nombre = entrada.nombre
        proveedor.ruc = entrada.ruc
        proveedor.direccion = entrada.direccion
        proveedor.correo = entrada.correo
        proveedor.telefono = entrada.telefono
        db.commit()
        db.refresh(proveedor)
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_eliminar_proveedor(db, id:str):
    # Validaciones inicio
    validacion=db.query(ProveedorModel).filter(ProveedorModel.id==id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El proveedor no existe")
    # Validaciones fin
    try:
        proveedor = db.query(ProveedorModel).filter(ProveedorModel.id==id).first()
        db.delete(proveedor)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")