from src.api.db.schemas.s_bien import BienCreate, BienResponse, BienUpdate
from src.api.db.schemas.s_response import BienMensajeDato, Mensaje
from src.controllers.c_bienes import c_obtener_todos_los_bienes, c_crear_bien, c_actualizar_bien, c_eliminar_bien
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