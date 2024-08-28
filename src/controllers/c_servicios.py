from src.api.db.models.m_productos import Producto as ProductoModel
from src.api.db.models.m_servicios import Servicio as ServicioModel
from src.api.db.schemas.s_servicio import ServicioCreate, ServicioResponse
from fastapi import HTTPException, status

def c_obtener_todos_los_servicios(db):
    try:
        servicios = db.query(ServicioModel).all()
        array_datos = []
        for servicio in servicios:
            producto = db.query(ProductoModel).filter(ProductoModel.id==servicio.producto_id).first()
            datos = ServicioResponse(
                id = servicio.id,
                nombre = producto.nombre,
                informacion_general = producto.informacion_general,
                precio = producto.precio,
                garantia = producto.garantia,
                estado = producto.estado,
                condiciones_previas = servicio.condiciones_previas,
                servicio_incluye = servicio.servicio_incluye,
                servicio_no_incluye = servicio.servicio_no_incluye,
                restricciones = servicio.restricciones,
                producto_id = servicio.producto_id,
            )
            array_datos.append(datos)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_crear_servicio(db, entrada:ServicioCreate):
    # Validaciones inicio
    validacion = db.query(ProductoModel).filter(ProductoModel.nombre==entrada.nombre).first()
    if validacion is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del Servicio ya existe")
    # Validaciones fin
    try:
        datos = ProductoModel(
            nombre = entrada.nombre,
            informacion_general = entrada.informacion_general,
            precio = entrada.precio,
            garantia = entrada.garantia,
            estado = entrada.estado,
        )
        db.add(datos)
        db.commit()
        db.refresh(datos)
        datos = ServicioModel(
            condiciones_previas = entrada.nombre,
            servicio_incluye = entrada.servicio_incluye,
            servicio_no_incluye = entrada.servicio_no_incluye,
            restricciones = entrada.restricciones,
            producto_id = datos.id,
        )
        db.add(datos)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")