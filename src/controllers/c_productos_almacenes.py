from src.api.db.models.m_productos_almacenes import Producto_Almacen as Producto_AlmacenModel
from src.api.db.schemas.s_producto_almacen import ProductoAlmacenCreate
from src.api.db.models.m_bienes import Bien as BienModel
from src.api.db.models.m_almacenes import Almacen as AlmacenModel
from src.api.db.models.m_movimientos_almacenes import Movimiento_Almacen as Movimiento_AlmacenModel
from fastapi import HTTPException, status
from datetime import datetime
import pytz

LIMA_TZ = pytz.timezone("America/Lima")

def c_obtener_todos_los_historiales_de_movimiento(db):
    try:
        historiales_de_movimientos = db.query(Movimiento_AlmacenModel).all()
        array_datos = []
        for historial_movimiento in historiales_de_movimientos:
            array_datos.append(historial_movimiento)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_obtener_todos_los_stock(db):
    try:
        productos_en_almacenes = db.query(Producto_AlmacenModel).all()
        array_datos = []
        for producto_almacen in productos_en_almacenes:
            array_datos.append(producto_almacen)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_obtener_stock_de_un_producto_en_almacenes(db, producto_id:str):
    producto_id = producto_id.strip()
    if producto_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo producto_id está vacío")
    try:
        producto_en_almacenes = db.query(Producto_AlmacenModel).filter(Producto_AlmacenModel.producto_id==producto_id).all()
        array_datos = []
        for producto_almacen in producto_en_almacenes:
            array_datos.append(producto_almacen)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_obtener_stock_de_almacen(db, almacen_id:str):
    almacen_id = almacen_id.strip()
    if almacen_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo almacen_id está vacío")
    try:
        productos_en_almacen = db.query(Producto_AlmacenModel).filter(Producto_AlmacenModel.almacen_id==almacen_id).all()
        array_datos = []
        for producto_almacen in productos_en_almacen:
            array_datos.append(producto_almacen)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_aumentar_stock(db, entrada:ProductoAlmacenCreate):
    # Validaciones inicio
    if entrada.producto_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo producto_id está vacío")
    if entrada.almacen_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo almacen_id está vacío")
    if entrada.cantidad == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo cantidad está vacío")
    if entrada.cantidad < 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo cantidad tiene que ser mayor a 0")
    
    validacion = db.query(BienModel).filter(BienModel.id==entrada.producto_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El producto no existe")
    
    validacion = db.query(AlmacenModel).filter(AlmacenModel.id==entrada.almacen_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El almacen no existe")
    # Validaciones fin
    producto_almacen = db.query(Producto_AlmacenModel).filter(Producto_AlmacenModel.almacen_id==entrada.almacen_id,
                                                              Producto_AlmacenModel.producto_id==entrada.producto_id
                                                              ).first()
    if producto_almacen is None:
        try:
            datos = Producto_AlmacenModel(
                producto_id = entrada.producto_id,
                almacen_id = entrada.almacen_id,
                cantidad = entrada.cantidad,
            )
            db.add(datos)
            db.commit()
            datos = Movimiento_AlmacenModel(
                producto_id = entrada.producto_id,
                almacen_id = entrada.almacen_id,
                cantidad = entrada.cantidad,
                tipo_movimiento = "ENTRADA",
                created_at = datetime.now(LIMA_TZ).strftime("%Y-%m-%d %H:%M:%S")
            )
            db.add(datos)
            db.commit()
            return True
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

    if producto_almacen is not None:
        try:
            producto_almacen.cantidad += entrada.cantidad
            db.add(producto_almacen)
            db.commit()
            datos = Movimiento_AlmacenModel(
                producto_id = entrada.producto_id,
                almacen_id = entrada.almacen_id,
                cantidad = entrada.cantidad,
                tipo_movimiento = "ENTRADA",
                created_at = datetime.now(LIMA_TZ).strftime("%Y-%m-%d %H:%M:%S")
            )
            return True
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_disminuir_stock(db, entrada:ProductoAlmacenCreate):
    # Validaciones inicio
    if entrada.producto_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo producto_id está vacío")
    if entrada.almacen_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo almacen_id está vacío")
    if entrada.cantidad == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo cantidad está vacío")
    if entrada.cantidad < 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo cantidad tiene que ser mayor a 0")
    
    validacion = db.query(BienModel).filter(BienModel.id==entrada.producto_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El producto no existe")
    
    validacion = db.query(AlmacenModel).filter(AlmacenModel.id==entrada.almacen_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El almacen no existe")
    # Validaciones fin
    producto_almacen = db.query(Producto_AlmacenModel).filter(Producto_AlmacenModel.almacen_id==entrada.almacen_id,
                                                              Producto_AlmacenModel.producto_id==entrada.producto_id
                                                              ).first()
    if producto_almacen is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se puede retirar el stock")

    if producto_almacen is not None:
        producto_almacen.cantidad -= entrada.cantidad
        if producto_almacen.cantidad < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se puede retirar el stock")
        try:
            db.add(producto_almacen)
            db.commit()
            datos = Movimiento_AlmacenModel(
                producto_id = entrada.producto_id,
                almacen_id = entrada.almacen_id,
                cantidad = entrada.cantidad,
                tipo_movimiento = "SALIDA",
                created_at = datetime.now(LIMA_TZ).strftime("%Y-%m-%d %H:%M:%S")
            )
            db.add(datos)
            db.commit()
            return True
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")