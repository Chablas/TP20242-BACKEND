from src.api.db.schemas.s_categorias import CategoriaCreate, CategoriaResponse, CategoriaUpdate
from src.api.db.schemas.s_response import Mensaje
from src.controllers.c_pedido import c_crear_pedido
from src.controllers.c_imagenes import subir_imagen
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_pedidos = APIRouter()

@gestionar_pedidos.post("/post/pedido/{usuario_id}", response_model=Mensaje, name="Crear un pedido")
async def r_crear_pedido(entrada: CategoriaCreate, usuario_id:int, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    if c_crear_pedido(db, usuario_id, entrada):
        respuesta = Mensaje(
            detail="Pedido creado exitosamente",
        )
        return respuesta