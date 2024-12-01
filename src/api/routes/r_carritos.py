from src.api.db.schemas.s_carritos_items import CarritoItemsCreate, CarritoItemsResponse, CarritoTotalResponse
from src.api.db.schemas.s_response import Mensaje
from src.controllers.c_carritos import c_añadir_item_a_carrito, c_ver_items_de_carrito_por_usuario, c_quitar_item_a_carrito, c_obtener_total_de_carrito_por_usuario_id
from src.controllers.c_imagenes import subir_imagen
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List
#Cargado de imagenes

gestionar_carritos = APIRouter()

@gestionar_carritos.get("/get/carritos_items/{usuario_id}", response_model=List[CarritoItemsResponse], name="Obtener los items de un carrito por id de usuario")
async def r_ver_items_de_carrito_por_usuario(usuario_id:int, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    array = c_ver_items_de_carrito_por_usuario(db, usuario_id)
    return array

@gestionar_carritos.get("/get/carrito/total/{usuario_id}", response_model=CarritoTotalResponse, name="Obtener el total de un carrito por id de usuario")
async def r_obtener_total_de_carrito_por_usuario_id(usuario_id:int, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    respuesta = c_obtener_total_de_carrito_por_usuario_id(db, usuario_id)
    return respuesta

@gestionar_carritos.put("/put/carritos_items/añadir/{usuario_id}", response_model=Mensaje, name="Añadir un item a un carrito de un usuario")
async def r_añadir_item_a_carrito(usuario_id:int, entrada: CarritoItemsCreate, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    if c_añadir_item_a_carrito(db, usuario_id, entrada):
        respuesta = Mensaje(
            detail="Carrito actualizado exitosamente",
        )
        return respuesta
    
@gestionar_carritos.put("/put/carritos_items/quitar/{usuario_id}", response_model=Mensaje, name="Quitar un item a un carrito de un usuario")
async def r_quitar_item_a_carrito(usuario_id:int, entrada: CarritoItemsCreate, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    if c_quitar_item_a_carrito(db, usuario_id, entrada):
        respuesta = Mensaje(
            detail="Carrito actualizado exitosamente",
        )
        return respuesta