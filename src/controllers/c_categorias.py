from src.api.db.models.m_categorias import Categoria as CategoriaModel
from src.api.db.schemas.s_categorias import CategoriaCreate, CategoriaResponse, CategoriaUpdate
from fastapi import HTTPException, status
import os

def c_obtener_todos_las_categorias(db):
    try:
        categorias = db.query(CategoriaModel).all()
        array_datos = []
        for categoria in categorias:
            array_datos.append(categoria)
        return array_datos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_obtener_categoria_por_id(db, id:str):
    try:
        categoria = db.query(CategoriaModel).filter(CategoriaModel.id==id).first()
        return categoria
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_crear_categoria(db, entrada:CategoriaCreate):
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
    validacion = db.query(CategoriaModel).filter(CategoriaModel.nombre==entrada.nombre).first()
    if validacion is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre de la categoria ya existe")
    # Validaciones fin
    try:
        datos = CategoriaModel(
            nombre = entrada.nombre,
            descripcion = entrada.descripcion,
            imagen = entrada.imagen,
        )
        db.add(datos)
        db.commit()
        db.refresh(datos)
        respuesta = datos.id
        return respuesta
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_añadir_imagen_categoria(db, id:str, imagen:str):
    # Validaciones inicio
    imagen = imagen.strip()
    if imagen == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El campo imagen está vacío")

    validacion = db.query(CategoriaModel).filter(CategoriaModel.id==id).first()
    if validacion is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La categoría no existe")
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
        respuesta = categoria.id
        return respuesta
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