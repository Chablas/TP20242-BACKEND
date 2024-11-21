from src.api.db.schemas.s_categorias import CategoriaCreate, CategoriaResponse, CategoriaUpdate
from src.api.db.schemas.s_response import BienMensajeDato, Mensaje
from src.controllers.c_categorias import c_crear_categoria, c_obtener_todos_las_categorias, c_actualizar_categoria, c_eliminar_categoria, c_obtener_categoria_por_id, c_añadir_imagen_categoria
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List
#Cargado de imagenes
import secrets
from PIL import Image
from fastapi import File, UploadFile

gestionar_categorias = APIRouter()

@gestionar_categorias.get("/get/categorias", response_model=List[CategoriaResponse], name="Obtener todas las categorias")
async def r_obtener_categorias(db: Session = Depends(get_db)):
    array = c_obtener_todos_las_categorias(db)
    return array

@gestionar_categorias.get("/get/categoria/{id}", response_model=CategoriaResponse, name="Obtener una categoria por su id")
async def r_obtener_categoria_por_id(id:str, db: Session = Depends(get_db)):
    return c_obtener_categoria_por_id(db, id)

@gestionar_categorias.post("/post/categoria", response_model=Mensaje, name="Crear una categoria")
async def r_crear_categoria(entrada: CategoriaCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_crear_categoria(db, entrada):
        respuesta = Mensaje(
            detail="Categoria creada exitosamente",
        )
        return respuesta
    
@gestionar_categorias.put("/put/categoria/{id}", response_model=Mensaje, name="Actualizar una categoria")
async def r_actualizar_categoria(id:str, entrada: CategoriaUpdate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_actualizar_categoria(db, id, entrada):
        respuesta = Mensaje(
            detail="Categoria actualizada exitosamente",
        )
        return respuesta
    
@gestionar_categorias.put("/put/categoria/subir_imagen/{id}", response_model=Mensaje, name="Asignar una imagen a una categoría")
async def create_upload_file(id:int, file:UploadFile=File(...), db: Session = Depends(get_db)):
    FILEPATH = "./static/images"
    filename = file.filename
    extension = filename.split(".")[1]
    if extension not in ["png", "jpg", "jpeg", "jpe", "jif", "jfif"]:
        respuesta = Mensaje(
            detail="Extensión de archivo de imagen no aceptado. Los formatos válidos son: png, jpg, jpeg, jpe, jif, jfif",
        )
        return respuesta
    token_name = secrets.token_hex(10)+"."+extension
    generated_name = FILEPATH + token_name
    file_content = await file.read()
    with open (generated_name, "wb") as file:
        file.write(file_content)
    img  = Image.open(generated_name)
    #img = img.resize(size=(200,200))
    img.save(generated_name)
    file.close()
    if c_añadir_imagen_categoria(db, id, generated_name[1:]):
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