from src.api.db.schemas.s_servicio import ServicioCreate, ServicioResponse
from src.api.db.schemas.s_response import ServicioMensajeDato, Mensaje
from src.controllers.c_servicios import c_obtener_todos_los_servicios, c_crear_servicio
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_servicios = APIRouter()

@gestionar_servicios.get("/get/servicios", response_model=List[ServicioResponse], name="Obtener todos los servicios")
async def r_obtener_servicios(db: Session = Depends(get_db)):
    array = c_obtener_todos_los_servicios(db)
    return array

@gestionar_servicios.post("/post/servicio", response_model=Mensaje, name="Crear un servicio")
async def r_crear_servicio(entrada: ServicioCreate, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    if c_crear_servicio(db, entrada):
        respuesta = Mensaje(
            mensaje="Producto creado exitosamente",
        )
        return respuesta