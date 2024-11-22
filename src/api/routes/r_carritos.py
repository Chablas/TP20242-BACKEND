from src.api.db.schemas.s_carritos_items import CarritoItemsCreate
from src.api.db.schemas.s_response import Mensaje
from src.controllers.c_carritos import c_añadir_item_a_carrito
from src.controllers.c_imagenes import subir_imagen
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List
#Cargado de imagenes

gestionar_carritos = APIRouter()

@gestionar_carritos.put("/put/carritos_items/{usuario_id}", response_model=Mensaje, name="Añadir un item a un carrito de un usuario")
async def r_añadir_item_a_carrito(usuario_id:int, entrada: CarritoItemsCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_añadir_item_a_carrito(db, usuario_id, entrada):
        respuesta = Mensaje(
            detail="Carrito actualizado exitosamente",
        )
        return respuesta