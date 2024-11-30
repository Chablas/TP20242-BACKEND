from src.api.db.schemas.s_categorias import CategoriaCreate, CategoriaResponse, CategoriaUpdate
from src.api.db.schemas.s_response import Mensaje, MensajeID
from src.controllers.c_categorias import c_crear_categoria, c_obtener_todos_las_categorias, c_actualizar_categoria, c_eliminar_categoria, c_obtener_categoria_por_id, c_añadir_imagen_categoria
from src.controllers.c_imagenes import subir_imagen
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List
#Cargado de imagenes
from fastapi import File, UploadFile

gestionar_categorias = APIRouter()

@gestionar_categorias.get("/get/categorias", response_model=List[CategoriaResponse], name="Obtener todas las categorias")
async def r_obtener_categorias(db: Session = Depends(get_db)):
    array = c_obtener_todos_las_categorias(db)
    return array

@gestionar_categorias.get("/get/categoria/{id}", response_model=CategoriaResponse, name="Obtener una categoria por su id")
async def r_obtener_categoria_por_id(id:str, db: Session = Depends(get_db)):
    return c_obtener_categoria_por_id(db, id)

@gestionar_categorias.post("/post/categoria", response_model=MensajeID, name="Crear una categoria")
async def r_crear_categoria(entrada: CategoriaCreate, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):#
    respuesta_id = c_crear_categoria(db, entrada)
    respuesta = MensajeID(
        detail=respuesta_id,
    )
    return respuesta
    
@gestionar_categorias.put("/put/categoria/{id}", response_model=MensajeID, name="Actualizar una categoria")
async def r_actualizar_categoria(id:str, entrada: CategoriaUpdate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    respuesta_id = c_actualizar_categoria(db, id, entrada)
    respuesta = MensajeID(
        detail=respuesta_id,
    )
    return respuesta
    
@gestionar_categorias.put("/put/categoria/subir_imagen/{id}", response_model=Mensaje, name="Asignar una imagen a una categoría")
async def create_upload_file(id:int, file:UploadFile=File(...), db: Session = Depends(get_db)):
    imagen_ruta = await subir_imagen(file)
    if c_añadir_imagen_categoria(db, id, imagen_ruta):
        respuesta = Mensaje(
            detail="Imagen cargada exitosamente",
        )
        return respuesta
    
@gestionar_categorias.delete("/delete/categoria/{id}", response_model=Mensaje, name="Eliminar una categoria")
async def r_eliminar_categoria(id:str, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_eliminar_categoria(db, id):
        respuesta = Mensaje(
            detail="Categoria eliminada exitosamente",
        )
        return respuesta