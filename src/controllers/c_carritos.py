from src.api.db.models.m_carritos import Carrito as CarritoModel
from src.api.db.models.m_carritos_items import Carrito_Items as Carrito_ItemsModel
from src.api.db.models.m_usuarios import Usuario as UsuarioModel
from src.api.db.models.m_productos import Producto as ProductoModel
from src.api.db.schemas.s_carritos import CarritoCompleto, CarritoCreate, CarritoUpdate, CarritoResponse
from src.api.db.schemas.s_carritos_items import CarritoItemsCompleto, CarritoItemsCreate, CarritoItemsUpdate, CarritoItemsResponse
from fastapi import HTTPException, status

def c_obtener_total_de_carrito_por_usuario_id(db, id:int):
    try:
        carrito = db.query(CarritoModel).filter(CarritoModel.usuario_id==id).first()
        return carrito
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_ver_items_de_carrito_por_usuario(db, usuario_id:int):
    try:
        carrito = db.query(CarritoModel).filter(CarritoModel.usuario_id==usuario_id).first()
        carritoitems = db.query(Carrito_ItemsModel).filter(Carrito_ItemsModel.carrito_id==carrito.id).all()
        array_datos = []
        for item in carritoitems:
            array_datos.append(item)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_añadir_item_a_carrito(db, usuario_id:int, entrada:CarritoItemsCreate):
    # Validaciones inicio
    if entrada.producto_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo producto_id está vacío")
    if entrada.cantidad == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo cantidad está vacío")
    if entrada.cantidad <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La cantidad tiene que ser mayor que 0")
    if usuario_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo usuario_id está vacío")

    validacion = db.query(UsuarioModel).filter(UsuarioModel.id==usuario_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe")
    producto = db.query(ProductoModel).filter(ProductoModel.id==entrada.producto_id).first()
    if producto is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El producto no existe")
    # Validaciones fin
    carrito = db.query(CarritoModel).filter(CarritoModel.usuario_id==usuario_id).first()
    try:
        if carrito is not None:
            validacion = db.query(Carrito_ItemsModel).filter(Carrito_ItemsModel.carrito_id==carrito.id, Carrito_ItemsModel.producto_id==entrada.producto_id).first()
            if validacion is not None:
                validacion.cantidad += entrada.cantidad
                db.commit()
                carrito.total += (entrada.cantidad * producto.precio)
                db.commit()
            if validacion is None:
                datos = Carrito_ItemsModel(
                    carrito_id = carrito.id,
                    producto_id = entrada.producto_id,
                    cantidad = entrada.cantidad,
                )
                db.add(datos)
                db.commit()
                carrito.total += (entrada.cantidad * producto.precio)
                db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_quitar_item_a_carrito(db, usuario_id:int, entrada:CarritoItemsCreate):
    # Validaciones inicio
    if entrada.producto_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo producto_id está vacío")
    if entrada.cantidad == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo cantidad está vacío")
    if entrada.cantidad <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La cantidad tiene que ser mayor que 0")
    if usuario_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo usuario_id está vacío")
    validacion = db.query(UsuarioModel).filter(UsuarioModel.id==usuario_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe")
    producto = db.query(ProductoModel).filter(ProductoModel.id==entrada.producto_id).first()
    if producto is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El producto no existe")
    carrito = db.query(CarritoModel).filter(CarritoModel.usuario_id==usuario_id).first()
    if carrito is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El carrito no existe")
    if carrito is not None:
        validacion = db.query(Carrito_ItemsModel).filter(Carrito_ItemsModel.carrito_id==carrito.id, Carrito_ItemsModel.producto_id==entrada.producto_id).first()
        if validacion is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La cantidad de items no puede ser menor a 0")
        if validacion is not None:
            validacion.cantidad -= entrada.cantidad
            if validacion.cantidad < 0:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La cantidad de items no puede ser menor a 0")
    # Validaciones fin
    try:
        if validacion.cantidad == 0:
            db.delete(validacion)
        carrito.total -= (entrada.cantidad * producto.precio)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")