from src.api.db.models.m_productos_almacenes import Producto_Almacen as Producto_AlmacenModel
from src.api.db.schemas.s_producto_almacen import ProductoAlmacenCreate, ProductoAlmacenCompleto, ProductoAlmacenResponse
from src.api.db.models.m_productos import Producto as ProductoModel
from src.api.db.models.m_almacenes import Almacen as AlmacenModel
from fastapi import HTTPException, status
"""
def c_añadir_producto_almacen(db, entrada:ProductoAlmacenCreate):
    # Validaciones inicio
    entrada.producto_id = entrada.producto_id.strip()
    entrada.almacen_id = entrada.almacen_id.strip()
    entrada.cantidad = entrada.cantidad.strip()
    if entrada.producto_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo producto_id está vacío")
    if entrada.almacen_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo almacen_id está vacío")
    if entrada.cantidad == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo cantidad está vacío")
    
    validacion = db.query(ProductoModel).filter(ProductoModel.id==entrada.producto_id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El producto no existe")
    
    validacion = db.query(AlmacenModel).filter(AlmacenModel.id==entrada.almacen_id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El almacen no existe")
    # Validaciones fin
    producto_almacen = db.query(AlmacenModel).filter(AlmacenModel.id==entrada.almacen_id).first()
    try:
        datos = Producto_AlmacenModel(
            producto_id = entrada.producto_id,
            almacen_id = entrada.almacen_id,
            cantidad = entrada.cantidad + cantidad,
        )
        db.add(datos)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_actualizar_categoria(db, id:str, entrada:CategoriaUpdate):
    # Validaciones inicio
    entrada.nombre = entrada.nombre.strip()
    entrada.descripcion = entrada.descripcion.strip()
    entrada.imagen = entrada.imagen.strip()
    if entrada.nombre == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo nombre está vacío")
    if entrada.descripcion == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo descripcion está vacío")
    if entrada.imagen == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo imagen está vacío")
    validacion=db.query(CategoriaModel).filter(CategoriaModel.id==id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="La categoría no existe")
    validacion2 = db.query(CategoriaModel).filter(CategoriaModel.nombre==entrada.nombre).first()
    if validacion2 is not None:
        if validacion2.id != validacion.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre de la categoria ya existe")
    # Validaciones fin
    try:
        categoria = db.query(CategoriaModel).filter(CategoriaModel.id==id).first()
        categoria.nombre = entrada.nombre
        categoria.descripcion = entrada.descripcion
        categoria.imagen = entrada.imagen
        db.commit()
        db.refresh(categoria)
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_eliminar_categoria(db, id:str):
    # Validaciones inicio
    validacion=db.query(CategoriaModel).filter(CategoriaModel.id==id).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="La categoría no existe")
    # Validaciones fin
    try:
        categoria = db.query(CategoriaModel).filter(CategoriaModel.id==id).first()
        db.delete(categoria)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
"""