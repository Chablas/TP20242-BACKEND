from pydantic import BaseModel

class ProveedorCompleto(BaseModel):
    id: int
    nombre:str
    ruc:int
    direccion:str
    correo:str
    telefono:int
    class Config:
        orm_mode=True

class ProveedorCreate(BaseModel):
    nombre:str
    ruc:int
    direccion:str
    correo:str
    telefono:int
    class Config:
        orm_mode=True

class ProveedorUpdate(BaseModel):
    nombre:str
    ruc:int
    direccion:str
    correo:str
    telefono:int
    class Config:
        orm_mode=True

class ProveedorResponse(BaseModel):
    id: int
    nombre:str
    ruc:int
    direccion:str
    correo:str
    telefono:int
    class Config:
        orm_mode=True