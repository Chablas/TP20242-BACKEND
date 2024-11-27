from src.api.db.schemas.s_bien import BienCreate, BienResponse, BienUpdate
from src.api.db.schemas.s_response import Mensaje, MensajeID
from src.controllers.c_bienes import c_obtener_todos_los_bienes, c_crear_bien, c_actualizar_bien, c_eliminar_bien, c_añadir_imagen_bien, c_obtener_bien_por_id
from src.controllers.c_imagenes import subir_imagen
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List
#Cargado de imagenes
from fastapi import File, UploadFile

gestionar_bienes = APIRouter()

@gestionar_bienes.get("/get/bienes", response_model=List[BienResponse], name="Obtener todos los bienes")
async def r_obtener_bienes(db: Session = Depends(get_db)):
    array = c_obtener_todos_los_bienes(db)
    return array

@gestionar_bienes.get("/get/bien/{id}", response_model=BienResponse, name="Obtener un bien por su id")
async def r_obtener_bien_por_id(id:int, db: Session = Depends(get_db)):
    return c_obtener_bien_por_id(db, id)

@gestionar_bienes.post("/post/bien", response_model=MensajeID, name="Crear un bien")
async def r_crear_bien(entrada: BienCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    respuesta_id = c_crear_bien(db, entrada)
    respuesta = MensajeID(
        detail=respuesta_id,
    )
    return respuesta
    
@gestionar_bienes.put("/put/bien/{id}", response_model=MensajeID, name="Actualizar un bien")
async def r_actualizar_bien(id:int, entrada: BienUpdate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    respuesta_id = c_actualizar_bien(db, id, entrada)
    respuesta = MensajeID(
        detail=respuesta_id,
    )
    return respuesta
    
@gestionar_bienes.put("/put/bien/subir_imagen/{id}", response_model=Mensaje, name="Asignar una imagen a un bien")
async def create_upload_file(id:int, file:UploadFile=File(...), db: Session = Depends(get_db)):
    imagen_ruta = await subir_imagen(file)
    if c_añadir_imagen_bien(db, id, imagen_ruta):
        respuesta = Mensaje(
            detail="Imagen cargada exitosamente",
        )
        return respuesta
    
@gestionar_bienes.delete("/delete/bien/{id}", response_model=Mensaje, name="Eliminar un bien")
async def r_eliminar_bien(id:int, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_eliminar_bien(db, id):
        respuesta = Mensaje(
            detail="Bien eliminado exitosamente",
        )
        return respuesta