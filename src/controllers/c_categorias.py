from src.api.db.models.m_categorias import Categoria as CategoriaModel
from src.api.db.schemas.s_categorias import CategoriaCreate, CategoriaResponse
from fastapi import HTTPException, status

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

def c_crear_categoria(db, entrada:CategoriaCreate):
    # Validaciones inicio
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
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")