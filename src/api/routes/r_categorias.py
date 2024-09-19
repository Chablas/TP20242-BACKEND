from src.api.db.schemas.s_categorias import CategoriaCreate, CategoriaResponse
from src.api.db.schemas.s_response import BienMensajeDato, Mensaje
from src.controllers.c_categorias import c_crear_categoria, c_obtener_todos_las_categorias
from src.api.db.sesion import get_db
from src.auth.auth import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

gestionar_categorias = APIRouter()

@gestionar_categorias.get("/get/categorias", response_model=List[CategoriaResponse], name="Obtener todas las categorias")
async def r_obtener_categorias(db: Session = Depends(get_db)):
    array = c_obtener_todos_las_categorias(db)
    return array

@gestionar_categorias.post("/post/categoria", response_model=Mensaje, name="Crear una categoria")
async def r_crear_categoria(entrada: CategoriaCreate, db: Session = Depends(get_db)):#, user:dict=Depends(get_current_user)):
    if c_crear_categoria(db, entrada):
        respuesta = Mensaje(
            mensaje="Categoria creada exitosamente",
        )
        return respuesta