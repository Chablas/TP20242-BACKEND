from pydantic import BaseModel

class OrdenVentaCompleto(BaseModel):
    id: int
    usuario_id:int
    total:float
    class Config:
        orm_mode=True

class OrdenVentaCreate(BaseModel):
    id: int
    usuario_id:int
    class Config:
        orm_mode=True