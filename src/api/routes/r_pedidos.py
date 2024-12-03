from src.api.db.schemas.s_response import Mensaje
from src.api.db.schemas.s_pedido import MercadoPagoCreate
from src.controllers.c_pedido import c_crear_pedido
from src.controllers.c_mercadopago import c_crear_preferencia
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_pedidos = APIRouter()

@gestionar_pedidos.post("/post/pedido/{usuario_id}", response_model=Mensaje, name="Crear un pedido")
async def r_crear_pedido(usuario_id:int, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    if c_crear_pedido(db, usuario_id):
        respuesta = Mensaje(
            detail="Pedido creado exitosamente",
        )
        return respuesta
    
@gestionar_pedidos.post("/post/crear_preferencia", response_model=Mensaje, name="Crear una preferencia para MercadoPago")
async def r_crear_preferencia(entrada: MercadoPagoCreate, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    respuesta_id = c_crear_preferencia(db, entrada)
    respuesta = Mensaje(
        detail=respuesta_id,
    )
    return respuesta