from src.api.db.models.m_proveedores_bienes import Proveedor_Bien as Proveedor_BienModel
from src.api.db.schemas.s_proveedor_bien import ProveedorBienCreate, ProveedorBienDelete
from src.api.db.models.m_bienes import Bien as BienModel
from src.api.db.models.m_proveedores import Proveedor as ProveedorModel
from fastapi import HTTPException, status

def c_obtener_todos_los_productos_de_los_proveedores(db):
    try:
        bienes_de_proveedores = db.query(Proveedor_BienModel).all()
        array_datos = []
        for bien_de_proveedor in bienes_de_proveedores:
            array_datos.append(bien_de_proveedor)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_obtener_proveedores_de_un_producto(db, bien_id:int):
    if bien_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo bien_id está vacío")
    try:
        proveedores_del_bien = db.query(Proveedor_BienModel).filter(Proveedor_BienModel.bien_id==bien_id).all()
        array_datos = []
        for proveedor_del_bien in proveedores_del_bien:
            array_datos.append(proveedor_del_bien)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_obtener_productos_de_proveedor(db, proveedor_id:int):
    if proveedor_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo proveedor_id está vacío")
    try:
        productos_del_proveedor = db.query(Proveedor_BienModel).filter(Proveedor_BienModel.proveedor_id==proveedor_id).all()
        array_datos = []
        for producto_proveedor in productos_del_proveedor:
            array_datos.append(producto_proveedor)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_añadir_producto_a_proveedor(db, entrada:ProveedorBienCreate):
    # Validaciones inicio
    entrada.codigo = entrada.codigo.strip()
    if entrada.precio == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo precio está vacío")
    if entrada.precio <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo precio tiene que ser positivo")
    if entrada.proveedor_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo proveedor_id está vacío")
    if entrada.bien_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo bien_id está vacío")
    if entrada.codigo == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo codigo está vacío")
    validacion = db.query(ProveedorModel).filter(ProveedorModel.id==entrada.proveedor_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El proveedor no existe")
    validacion = db.query(BienModel).filter(BienModel.id==entrada.bien_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El bien no existe")
    validacion = db.query(Proveedor_BienModel).filter(Proveedor_BienModel.proveedor_id==entrada.proveedor_id, Proveedor_BienModel.bien_id==entrada.bien_id).first()
    if validacion is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El proveedor ya tiene asignado el producto")
    # Validaciones fin
    try:
        datos = Proveedor_BienModel(
            codigo = entrada.codigo,
            precio = entrada.precio,
            proveedor_id = entrada.proveedor_id,
            bien_id = entrada.bien_id,
        )
        db.add(datos)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_quitar_producto_a_proveedor(db, entrada:ProveedorBienDelete):
    # Validaciones inicio
    if entrada.proveedor_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo proveedor_id está vacío")
    if entrada.bien_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo bien_id está vacío")
    validacion = db.query(ProveedorModel).filter(ProveedorModel.id==entrada.proveedor_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El proveedor no existe")
    validacion = db.query(BienModel).filter(BienModel.id==entrada.bien_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El bien no existe")
    validacion = db.query(Proveedor_BienModel).filter(Proveedor_BienModel.proveedor_id==entrada.proveedor_id, Proveedor_BienModel.bien_id==entrada.bien_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El proveedor no tiene asignado el producto")
    # Validaciones fin
    try:
        db.delete(validacion)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")