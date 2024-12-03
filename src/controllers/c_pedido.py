from src.api.db.models.m_pedidos import Pedido as PedidoModel
from src.api.db.models.m_pedidos_detalle import PedidosDetalle as PedidosDetalleModel
from src.api.db.models.m_carritos_items import Carrito_Items as Carrito_ItemsModel
from src.api.db.models.m_carritos import Carrito as CarritoModel
from src.api.db.models.m_usuarios import Usuario as UsuarioModel
from src.api.db.schemas.s_pedido import PedidoCreate
from fastapi import HTTPException, status
import os
from datetime import datetime
import pytz

LIMA_TZ = pytz.timezone("America/Lima")

def c_crear_pedido(db, usuario_id:int, entrada:PedidoCreate):
    # Validaciones inicio
    if entrada.total == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo total está vacío")
    validacion = db.query(UsuarioModel).filter(UsuarioModel.id==usuario_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe")
    carrito = db.query(CarritoModel).filter(CarritoModel.usuario_id==usuario_id).first()
    if carrito is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El carrito no existe")
    carritoItems = db.query(Carrito_ItemsModel).filter(Carrito_ItemsModel.carrito_id==carrito.id).all()
    if carritoItems == []:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El carrito no tiene items")
    # Validaciones fin
    try:
        datos = PedidoModel(
            usuario_id = usuario_id,
            total = carrito.total,
            estado = "EN ESPERA",
            created_at = datetime.now(LIMA_TZ).strftime("%Y-%m-%d %H:%M:%S")
        )
        db.add(datos)
        db.commit()
        db.refresh(datos)
        for item in carritoItems:
            datos2 = PedidosDetalleModel(
                pedido_id = datos.id,
                producto_id = item.producto_id,
                cantidad = item.cantidad
            )
            db.add(datos2)
            db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")