from src.api.db.models.m_productos import Producto as ProductoModel
from src.api.db.models.m_categorias import Categoria as CategoriaModel
from src.api.db.models.m_bienes import Bien as BienModel
from src.api.db.schemas.s_bien import BienCreate, BienUpdate, BienResponse
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
                imagen = producto.imagen,

                marca = bien.marca,
                especificaciones_tecnicas = bien.especificaciones_tecnicas,
                producto_id = bien.producto_id,
                categoria_id = bien.categoria_id,
            )
            array_datos.append(datos)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_crear_bien(db, entrada:BienCreate):
    # Validaciones inicio
    if entrada.nombre == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo nombre está vacío")
    if entrada.informacion_general == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo informacion_general está vacío")
    if entrada.precio == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo precio está vacío")
    if entrada.garantia == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo garantia está vacío")
    if entrada.estado == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo estado está vacío")
    if entrada.imagen == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo imagen está vacío")
    if entrada.marca == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo marca está vacío")
    if entrada.especificaciones_tecnicas == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo especificaciones_tecnicas está vacío")
    if entrada.categoria_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo categoria_id está vacío")

    validacion = db.query(ProductoModel).filter(ProductoModel.nombre==entrada.nombre).first()
    if validacion is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre del Bien ya existe")
    validacion_categoria_id=db.query(CategoriaModel).filter(CategoriaModel.id==entrada.categoria_id).first()
    if validacion_categoria_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La categoria_id no existe")
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
        datos = BienModel(
            marca = entrada.marca,
            especificaciones_tecnicas = entrada.especificaciones_tecnicas,
            producto_id = datos.id,
            categoria_id = entrada.categoria_id,
        )
        db.add(datos)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_actualizar_bien(db, id:str, entrada:BienUpdate):
    # Validaciones inicio
    if entrada.nombre == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo nombre está vacío")
    if entrada.informacion_general == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo informacion_general está vacío")
    if entrada.precio == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo precio está vacío")
    if entrada.garantia == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo garantia está vacío")
    if entrada.estado == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo estado está vacío")
    if entrada.imagen == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo imagen está vacío")
    if entrada.marca == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo marca está vacío")
    if entrada.especificaciones_tecnicas == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo especificaciones_tecnicas está vacío")
    if entrada.categoria_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo categoria_id está vacío")
    validacion=db.query(BienModel).filter(BienModel.id==id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El bien no existe")
    validacion_categoria_id=db.query(CategoriaModel).filter(CategoriaModel.id==entrada.categoria_id).first()
    if validacion_categoria_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La categoria_id no existe")
    # Validaciones fin
    try:
        bien = db.query(BienModel).filter(BienModel.id==id).first()
        producto = db.query(ProductoModel).filter(ProductoModel.id==bien.producto_id).first()
        producto.nombre = entrada.nombre
        producto.informacion_general = entrada.informacion_general
        producto.precio = entrada.precio
        producto.garantia = entrada.garantia
        producto.imagen = entrada.imagen
        producto.estado = entrada.estado
        db.commit()
        db.refresh(producto)
        bien.marca = entrada.marca
        bien.especificaciones_tecnicas = entrada.especificaciones_tecnicas
        bien.producto_id = producto.id
        bien.categoria_id = entrada.categoria_id
        db.commit()
        db.refresh(bien)
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_eliminar_bien(db, id:str):
    # Validaciones inicio
    validacion=db.query(BienModel).filter(BienModel.id==id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El bien no existe")
    # Validaciones fin
    try:
        bien = db.query(BienModel).filter(BienModel.id==id).first()
        db.delete(bien)
        db.commit()
        producto = db.query(ProductoModel).filter(ProductoModel.id==bien.producto_id).first()
        db.delete(producto)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")