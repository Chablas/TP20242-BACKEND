from src.api.db.schemas.s_orden_venta import OrdenVentaCreate
from src.api.db.schemas.s_response import Mensaje
from src.controllers.c_ordenes_venta import c_crear_orden_venta
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_ordenes_venta = APIRouter()

@gestionar_ordenes_venta.post("/post/orden_compra", response_model=Mensaje, name="Crear una orden")
async def r_crear_orden_compra(entrada: OrdenVentaCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_crear_orden_venta(db, entrada):
        respuesta = Mensaje(
            detail="Orden creada exitosamente",
        )
        return respuesta
    
@gestionar_ordenes_venta.post("/post/process_payment", response_model=Mensaje, name="Procesar pago")
async def r_procesar_pago(entrada: OrdenVentaCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_crear_orden_venta(db, entrada):
        respuesta = Mensaje(
            detail="Orden creada exitosamente",
        )
        return respuesta