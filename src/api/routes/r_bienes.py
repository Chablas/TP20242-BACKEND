from src.api.db.schemas.s_bien import BienCreate, BienResponse
from src.api.db.schemas.s_response import BienMensajeDato, Mensaje
from src.controllers.c_bienes import c_obtener_todos_los_bienes, c_crear_bien
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_bienes = APIRouter()

@gestionar_bienes.get("/get/bienes", response_model=List[BienResponse], name="Obtener todos los bienes")
async def r_obtener_bienes(db: Session = Depends(get_db)):
    array = c_obtener_todos_los_bienes(db)
    return array

@gestionar_bienes.post("/post/bien", response_model=Mensaje, name="Crear un bien")
async def r_crear_bien(entrada: BienCreate, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    if c_crear_bien(db, entrada):
        respuesta = Mensaje(
            mensaje="Producto creado exitosamente",
        )
        return respuesta