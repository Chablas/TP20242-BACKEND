from pydantic import BaseModel

class CategoriaCompleto(BaseModel):
    id: int
    nombre:str
    descripcion:str
    imagen:str
    class Config:
        orm_mode=True

class CategoriaCreate(BaseModel):
    nombre:str
    descripcion:str
    imagen:str
    class Config:
        orm_mode=True

class CategoriaResponse(BaseModel):
    id: int
    nombre:str
    descripcion:str
    imagen:str
    class Config:
        orm_mode=True