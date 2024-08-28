from src.api.db.schemas.s_divisa import DivisaCreate, DivisaCambioUpdate, DivisaResponse, CambioResponseAll
from src.api.db.schemas.s_response import DivisaMensajeDato, Mensaje, CambioMensajeDato
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from src.controllers.c_divisa import c_obtener_divisa_por_abbr, crear_divisa, actualizar_tipo_cambio_divisa, c_tipo_cambio_divisa_por_abbr, c_obtener_todas_las_divisas, c_tipo_cambio_divisas
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_divisas = APIRouter()

@gestionar_divisas.get("/get/divisas", response_model=List[DivisaResponse], name="Obtener todas las divisas")
async def obtener_usuarios(db: Session = Depends(get_db)):
    array = c_obtener_todas_las_divisas(db)
    return array

@gestionar_divisas.get("/get/divisa/{abbr}", response_model=DivisaMensajeDato, name="Obtener una divisa por su abreviación")
async def obtener_usuarios(abbr:str, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    divisa = c_obtener_divisa_por_abbr(db, abbr)
    respuesta = DivisaMensajeDato(
        mensaje = "Divisa obtenida exitosamente",
        dato = divisa,
    )
    return respuesta

@gestionar_divisas.post("/post/divisa", response_model=Mensaje, name="Crear una divisa")
async def crear_nueva_divisa(entrada: DivisaCreate, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    if crear_divisa(db, entrada):
        respuesta = Mensaje(
            mensaje="Divisa creada exitosamente",
        )
        return respuesta

@gestionar_divisas.get("/get/all/tipo_cambio/", response_model=List[CambioResponseAll], name="Obtener los tipos de cambio de todas las divisas respecto a otra")
async def obtener_tipo_de_cambio_de_todas_las_divisa(db: Session = Depends(get_db)):
    array = c_tipo_cambio_divisas(db)
    return array

@gestionar_divisas.get("/get/{abbr_primary}/tipo_cambio/{abbr_secondary}", response_model=CambioMensajeDato, name="Obtener los tipos de cambio de una divisa respecto a otra")
async def obtener_tipo_de_cambio_divisa(abbr_primary:str, abbr_secondary:str, db: Session = Depends(get_db)):
    divisa = c_tipo_cambio_divisa_por_abbr(db, abbr_primary, abbr_secondary)
    respuesta = CambioMensajeDato(
        mensaje = "Tipos de cambio obtenidos exitosamente",
        dato = divisa,
    )
    return respuesta

@gestionar_divisas.put("/put/divisa/tipo_cambio", response_model=Mensaje, name="Actualizar los tipos de cambio de una divisa respecto a otra")
async def actualizar_tipo_cambio(entrada: DivisaCambioUpdate, db: Session = Depends(get_db), user:dict=Depends(get_current_user)):
    if actualizar_tipo_cambio_divisa(db, entrada):
        respuesta = Mensaje(
            mensaje="Divisa actualizada exitosamente",
        )
        return respuesta