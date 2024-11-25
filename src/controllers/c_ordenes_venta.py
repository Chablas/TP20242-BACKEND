from src.api.db.models.m_ordenes_venta import Orden_Venta as Orden_VentaModel
from src.api.db.models.m_carritos import Carrito as CarritoModel
from src.api.db.models.m_carritos_items import Carrito_Items as Carrito_ItemsModel
from src.api.db.models.m_usuarios import Usuario as UsuarioModel
from src.api.db.schemas.s_orden_venta import OrdenVentaCreate
from fastapi import HTTPException, status
import os

def c_crear_orden_venta(db, entrada:OrdenVentaCreate):
    # Validaciones inicio
    if entrada.usuario_id == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo usuario_id está vacío")
    validacion = db.query(UsuarioModel).filter(UsuarioModel.id==entrada.usuario_id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe")
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe")
    # Validaciones fin
    try:
        datos = Orden_VentaModel(
            usuario_id = entrada.usuario_id,
            total = entrada.descripcion,
        )
        db.add(datos)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")