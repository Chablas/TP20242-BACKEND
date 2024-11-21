from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes.r_almacenes import gestionar_almacenes
from src.api.routes.r_bienes import gestionar_bienes
from src.api.routes.r_servicios import gestionar_servicios
from src.api.routes.r_usuarios import gestionar_usuarios
from src.api.routes.r_categorias import gestionar_categorias
from src.api.routes.r_proveedores import gestionar_proveedores
from src.api.routes.r_login import login_router
from src.api.routes.r_email import gestionar_emails
from src.api.routes.r_productos_almacenes import gestionar_productos_almacenes
from src.api.routes.r_roles import gestionar_roles
from src.api.routes.r_usuarios_roles import gestionar_usuarios_roles
from src.api.routes.r_productos_proveedores import gestionar_proveedores_bienes

description = """
Para consumir los servicios con símbolo de candado primero debes autenticarte con una cuenta.
"""

app = FastAPI(
    title="API de Compusave",
    description=description,
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(login_router)
app.include_router(gestionar_almacenes, tags=["Gestionar Almacenes"])
app.include_router(gestionar_bienes, tags=["Gestionar Bienes"])
app.include_router(gestionar_proveedores_bienes, tags=["Gestionar Bienes de Proveedores"])
app.include_router(gestionar_categorias, tags=["Gestionar Categorías"])
app.include_router(gestionar_emails, tags=["Gestionar Emails"])
app.include_router(gestionar_proveedores, tags=["Gestionar Proveedores"])
app.include_router(gestionar_roles, tags=["Gestionar Roles"])
app.include_router(gestionar_usuarios_roles, tags=["Gestionar Roles de Usuarios"])
app.include_router(gestionar_servicios, tags=["Gestionar Servicios"])
app.include_router(gestionar_productos_almacenes, tags=["Gestionar Stock"])
app.include_router(gestionar_usuarios, tags=["Gestionar Usuarios"])