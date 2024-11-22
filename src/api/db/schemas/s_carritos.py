from pydantic import BaseModel

class CarritoCompleto(BaseModel):
    id: int
    usuario_id:int
    total:float
    class Config:
        orm_mode=True

class CarritoCreate(BaseModel):
    usuario_id:int
    total:float
    class Config:
        orm_mode=True

class CarritoUpdate(BaseModel):
    usuario_id:int
    total:float
    class Config:
        orm_mode=True

class CarritoResponse(BaseModel):
    id: int
    usuario_id:int
    total:float
    class Config:
        orm_mode=True