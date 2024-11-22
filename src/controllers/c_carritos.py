from src.api.db.models.m_carritos import Carrito as CarritoModel
from src.api.db.models.m_carritos_items import Carrito_Items as Carrito_ItemsModel
from src.api.db.models.m_usuarios import Usuario as UsuarioModel
from src.api.db.models.m_productos import Producto as ProductoModel
from src.api.db.schemas.s_carritos import CarritoCompleto, CarritoCreate, CarritoUpdate, CarritoResponse
from src.api.db.schemas.s_carritos_items import CarritoItemsCompleto, CarritoItemsCreate, CarritoItemsUpdate, CarritoItemsResponse
from fastapi import HTTPException, status

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
        if carrito is None:
            datos = CarritoModel(
                usuario_id = usuario_id,
                total = 0,
            )
            db.add(datos)
            db.commit()
            db.refresh()
            datos = Carrito_ItemsModel(
                carrito_id = datos.id,
                producto_id = entrada.producto_id,
                cantidad = entrada.cantidad,
            )
        if carrito is not None:
            datos = Carrito_ItemsModel(
                carrito_id = carrito.id,
                producto_id = entrada.producto_id,
                cantidad = entrada.cantidad,
            )
            db.add(datos)
            db.commit()
            db.refresh()
            total = entrada.cantidad * producto.precio
            carrito.total = total
            db.commit()
            db.refresh()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")