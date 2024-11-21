from src.api.db.schemas.s_bien import BienCreate, BienResponse, BienUpdate
from src.api.db.schemas.s_response import BienMensajeDato, Mensaje
from src.controllers.c_bienes import c_obtener_todos_los_bienes, c_crear_bien, c_actualizar_bien, c_eliminar_bien, c_añadir_imagen_bien
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter, Form, File, UploadFile, HTTPException, status
from fastapi.params import Depends, Body
from sqlalchemy.orm import Session
from typing import List
#Cargado de imagenes
import secrets
from PIL import Image
import json

gestionar_bienes = APIRouter()

@gestionar_bienes.put("/uploadfile/producto/{bien_id}")
async def create_upload_file(bien_id:int, file:UploadFile=File(...), db: Session = Depends(get_db)):
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
    if c_añadir_imagen_bien(db, bien_id, generated_name[1:]):
        respuesta = Mensaje(
            detail="Imagen cargada exitosamente",
        )
        return respuesta

@gestionar_bienes.get("/get/bienes", response_model=List[BienResponse], name="Obtener todos los bienes")
async def r_obtener_bienes(db: Session = Depends(get_db)):
    array = c_obtener_todos_los_bienes(db)
    return array

@gestionar_bienes.post("/post/bien", response_model=Mensaje, name="Crear un bien")
async def r_crear_bien(entrada: BienCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_crear_bien(db, entrada):
        respuesta = Mensaje(
            detail="Bien creado exitosamente",
        )
        return respuesta
    
@gestionar_bienes.put("/put/bien/{id}", response_model=Mensaje, name="Actualizar un bien")
async def r_actualizar_bien(id:str, entrada: BienUpdate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_actualizar_bien(db, id, entrada):
        respuesta = Mensaje(
            detail="Bien actualizado exitosamente",
        )
        return respuesta
    
@gestionar_bienes.delete("/delete/bien/{id}", response_model=Mensaje, name="Eliminar un bien")
async def r_eliminar_bien(id:str, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_eliminar_bien(db, id):
        respuesta = Mensaje(
            detail="Bien eliminado exitosamente",
        )
        return respuesta