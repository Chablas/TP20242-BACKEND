from src.api.db.models.m_productos import Producto as ProductoModel
from src.api.db.models.m_bienes import Bien as BienModel
from src.api.db.schemas.s_bien import BienCreate, BienResponse
from fastapi import HTTPException, status

def c_obtener_todos_los_bienes(db):
    try:
        bienes = db.query(BienModel).all()
        array_datos = []
        for bien in bienes:
            producto = db.query(ProductoModel).filter(ProductoModel.id==bien.producto_id).first()
            datos = BienResponse(
                id = bien.id,
                nombre = producto.nombre,
                informacion_general = producto.informacion_general,
                precio = producto.precio,
                garantia = producto.garantia,
                estado = producto.estado,
                marca = bien.marca,
                especificaciones_tecnicas = bien.especificaciones_tecnicas,
                producto_id = bien.producto_id,
            )
            array_datos.append(datos)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_crear_bien(db, entrada:BienCreate):
    # Validaciones inicio
    validacion = db.query(ProductoModel).filter(ProductoModel.nombre==entrada.nombre).first()
    if validacion is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del Bien ya existe")
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
        datos = BienModel(
            marca = entrada.marca,
            especificaciones_tecnicas = entrada.especificaciones_tecnicas,
            producto_id = datos.id,
        )
        db.add(datos)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")