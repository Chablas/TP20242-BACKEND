from src.api.db.models.m_productos_almacenes import Producto_Almacen as Producto_AlmacenModel
from src.api.db.schemas.s_producto_almacen import ProductoAlmacenCreate, ProductoAlmacenCompleto, ProductoAlmacenResponse
from src.api.db.models.m_productos import Producto as ProductoModel
from src.api.db.models.m_bienes import Bien as BienModel
from src.api.db.models.m_almacenes import Almacen as AlmacenModel
from fastapi import HTTPException, status

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
                cantidad = entrada.cantidad
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
            return True
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")