from pydantic import BaseModel

class AlmacenCompleto(BaseModel):
    id: int
    nombre:str
    ubicacion:str
    class Config:
        orm_mode=True

class AlmacenCreate(BaseModel):
    nombre:str
    ubicacion:str
    class Config:
        orm_mode=True

class AlmacenResponse(BaseModel):
    id: int
    nombre:str
    ubicacion:str
    class Config:
        orm_mode=True