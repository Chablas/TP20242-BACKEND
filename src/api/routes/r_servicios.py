from src.api.db.schemas.s_servicio import ServicioCreate, ServicioResponse, ServicioUpdate
from src.api.db.schemas.s_response import Mensaje, MensajeID
from src.controllers.c_servicios import c_obtener_todos_los_servicios, c_crear_servicio, c_actualizar_servicio, c_eliminar_servicio, c_obtener_servicio_por_id
from src.controllers.c_servicios import c_añadir_imagen_servicio
from src.controllers.c_imagenes import subir_imagen
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List
#Cargado de imagenes
from fastapi import File, UploadFile

gestionar_servicios = APIRouter()

@gestionar_servicios.get("/get/servicios", response_model=List[ServicioResponse], name="Obtener todos los servicios")
async def r_obtener_servicios(db: Session = Depends(get_db)):
    array = c_obtener_todos_los_servicios(db)
    return array

@gestionar_servicios.get("/get/servicio/{id}", response_model=ServicioResponse, name="Obtener un servicio por su id")
async def r_obtener_servicio_por_id(id:int, db: Session = Depends(get_db)):
    return c_obtener_servicio_por_id(db, id)

@gestionar_servicios.post("/post/servicio", response_model=MensajeID, name="Crear un servicio")
async def r_crear_servicio(entrada: ServicioCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    respuesta_id = c_crear_servicio(db, entrada)
    respuesta = MensajeID(
        detail=respuesta_id,
    )
    return respuesta
    
@gestionar_servicios.put("/put/servicio/{id}", response_model=Mensaje, name="Actualizar un servicio")
async def r_actualizar_servicio(id:int, entrada: ServicioUpdate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_actualizar_servicio(db, id, entrada):
        respuesta = Mensaje(
            detail="Servicio actualizado exitosamente",
        )
        return respuesta
    
@gestionar_servicios.put("/put/servicio/subir_imagen/{id}", response_model=Mensaje, name="Asignar una imagen a un servicio")
async def create_upload_file(id:int, file:UploadFile=File(...), db: Session = Depends(get_db)):
    imagen_ruta = await subir_imagen(file)
    if c_añadir_imagen_servicio(db, id, imagen_ruta):
        respuesta = Mensaje(
            detail="Imagen cargada exitosamente",
        )
        return respuesta
    
@gestionar_servicios.delete("/delete/servicio/{id}", response_model=Mensaje, name="Eliminar un servicio")
async def r_eliminar_servicio(id:int, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_eliminar_servicio(db, id):
        respuesta = Mensaje(
            detail="Servicio eliminado exitosamente",
        )
        return respuesta