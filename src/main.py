from fastapi import FastAPI
from src.api.routes.r_almacenes import gestionar_almacenes
from src.api.routes.r_bienes import gestionar_bienes
from src.api.routes.r_servicios import gestionar_servicios
from src.api.routes.r_usuarios import gestionar_usuarios
from src.api.routes.r_login import login_router

description = """
Para consumir los servicios con símbolo de candado primero debes autenticarte con una cuenta.
"""

app = FastAPI(
    title="API de Compusave",
    description=description,
)

app.include_router(login_router)
app.include_router(gestionar_usuarios, tags=["Gestionar Usuarios"])
app.include_router(gestionar_almacenes, tags=["Gestionar Almacenes"])
app.include_router(gestionar_bienes, tags=["Gestionar Bienes"])
app.include_router(gestionar_servicios, tags=["Gestionar Servicios"])