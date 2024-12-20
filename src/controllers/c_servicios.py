from src.api.db.models.m_productos import Producto as ProductoModel
from src.api.db.models.m_servicios import Servicio as ServicioModel
from src.api.db.schemas.s_servicio import ServicioCreate, ServicioUpdate, ServicioResponse
from fastapi import HTTPException, status
import os

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
                imagen = producto.imagen,

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

def c_obtener_servicio_por_id(db, id:int):
    try:
        servicio = db.query(ServicioModel).filter(ServicioModel.id==id).first()
        producto = db.query(ProductoModel).filter(ProductoModel.id==servicio.producto_id).first()
        datos = ServicioResponse(
            id = servicio.id,
            nombre = producto.nombre,
            informacion_general = producto.informacion_general,
            precio = producto.precio,
            garantia = producto.garantia,
            estado = producto.estado,
            imagen = producto.imagen,

            condiciones_previas = servicio.condiciones_previas,
            servicio_incluye = servicio.servicio_incluye,
            servicio_no_incluye = servicio.servicio_no_incluye,
            restricciones = servicio.restricciones,
            producto_id = servicio.producto_id,
        )
        return datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_crear_servicio(db, entrada:ServicioCreate):
    # Validaciones inicio
    entrada.nombre = entrada.nombre.strip()
    entrada.informacion_general = entrada.informacion_general.strip()
    entrada.garantia = entrada.garantia.strip()
    entrada.imagen = entrada.imagen.strip()
    entrada.condiciones_previas = entrada.condiciones_previas.strip()
    entrada.servicio_incluye = entrada.servicio_incluye.strip()
    entrada.servicio_no_incluye = entrada.servicio_no_incluye.strip()
    entrada.restricciones = entrada.restricciones.strip()
    if entrada.nombre == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo nombre está vacío")
    if entrada.informacion_general == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo informacion_general está vacío")
    if entrada.precio == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo precio está vacío")
    if entrada.precio <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo precio tiene que ser mayor a 0")
    if entrada.garantia == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo garantia está vacío")
    if entrada.estado == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo estado está vacío")
    if entrada.imagen == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo imagen está vacío")
    if entrada.condiciones_previas == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo condiciones_previas está vacío")
    if entrada.servicio_incluye == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo servicio_incluye está vacío")
    if entrada.servicio_no_incluye == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo servicio_no_incluye está vacío")
    if entrada.restricciones == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo restricciones está vacío")
    
    validacion = db.query(ProductoModel).filter(ProductoModel.nombre==entrada.nombre).first()
    if validacion is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del servicio ya existe")
    # Validaciones fin
    try:
        datos = ProductoModel(
            nombre = entrada.nombre,
            informacion_general = entrada.informacion_general,
            precio = entrada.precio,
            garantia = entrada.garantia,
            estado = entrada.estado,
            imagen = entrada.imagen,
        )
        db.add(datos)
        db.commit()
        db.refresh(datos)
        datos = ServicioModel(
            condiciones_previas = entrada.condiciones_previas,
            servicio_incluye = entrada.servicio_incluye,
            servicio_no_incluye = entrada.servicio_no_incluye,
            restricciones = entrada.restricciones,
            producto_id = datos.id,
        )
        db.add(datos)
        db.commit()
        db.refresh(datos)
        respuesta = datos.id
        return respuesta
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_añadir_imagen_servicio(db, id:int, imagen:str):
    # Validaciones inicio
    imagen = imagen.strip()
    if imagen == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo imagen está vacío")

    validacion = db.query(ServicioModel).filter(ServicioModel.id==id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El servicio no existe")
    validacion = db.query(ProductoModel).filter(validacion.producto_id==ProductoModel.id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El producto no existe")
    # Validaciones fin
    try:
        image_path = f".{validacion.imagen}"
        validacion.imagen = imagen
        db.commit()
        db.refresh(validacion)
        if os.path.exists(image_path):
            os.remove(image_path)
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_actualizar_servicio(db, id:int, entrada:ServicioUpdate):
    # Validaciones inicio
    entrada.nombre = entrada.nombre.strip()
    entrada.informacion_general = entrada.informacion_general.strip()
    entrada.garantia = entrada.garantia.strip()
    entrada.imagen = entrada.imagen.strip()
    entrada.condiciones_previas = entrada.condiciones_previas.strip()
    entrada.servicio_incluye = entrada.servicio_incluye.strip()
    entrada.servicio_no_incluye = entrada.servicio_no_incluye.strip()
    entrada.restricciones = entrada.restricciones.strip()
    if entrada.nombre == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo nombre está vacío")
    if entrada.informacion_general == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo informacion_general está vacío")
    if entrada.precio == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo precio está vacío")
    if entrada.precio <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo precio tiene que ser mayor a 0")
    if entrada.garantia == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo garantia está vacío")
    if entrada.estado == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo estado está vacío")
    if entrada.imagen == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo imagen está vacío")
    if entrada.condiciones_previas == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo condiciones_previas está vacío")
    if entrada.servicio_incluye == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo servicio_incluye está vacío")
    if entrada.servicio_no_incluye == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo servicio_no_incluye está vacío")
    if entrada.restricciones == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo restricciones está vacío")
    
    validacion=db.query(ServicioModel).filter(ServicioModel.id==id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El servicio no existe")
    validacion2=db.query(ProductoModel).filter(ProductoModel.nombre==entrada.nombre).first()
    if validacion2 is not None:
        if int(validacion2.id) != int(validacion.producto_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del servicio ya existe")
    # Validaciones fin
    try:
        servicio = db.query(ServicioModel).filter(ServicioModel.id==id).first()
        producto = db.query(ProductoModel).filter(ProductoModel.id==servicio.producto_id).first()
        producto.nombre = entrada.nombre
        producto.informacion_general = entrada.informacion_general
        producto.precio = entrada.precio
        producto.garantia = entrada.garantia
        producto.imagen = entrada.imagen
        producto.estado = entrada.estado
        db.commit()
        db.refresh(producto)

        servicio.condiciones_previas = entrada.condiciones_previas
        servicio.servicio_incluye = entrada.servicio_incluye
        servicio.servicio_no_incluye = entrada.servicio_no_incluye
        servicio.restricciones = entrada.restricciones
        
        servicio.producto_id = producto.id
        
        db.commit()
        db.refresh(servicio)
        respuesta = servicio.id
        return respuesta
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_eliminar_servicio(db, id:int):
    # Validaciones inicio
    validacion=db.query(ServicioModel).filter(ServicioModel.id==id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El servicio no existe")
    # Validaciones fin
    try:
        servicio = db.query(ServicioModel).filter(ServicioModel.id==id).first()
        db.delete(servicio)
        db.commit()
        producto = db.query(ProductoModel).filter(ProductoModel.id==servicio.producto_id).first()
        db.delete(producto)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")