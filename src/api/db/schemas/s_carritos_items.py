from pydantic import BaseModel

class CarritoItemsCompleto(BaseModel):
    id: int
    carrito_id:int
    producto_id:int
    cantidad:int
    class Config:
        orm_mode=True

class CarritoItemsCreate(BaseModel):
    producto_id:int
    cantidad:int
    class Config:
        orm_mode=True

class CarritoItemsUpdate(BaseModel):
    id: int
    carrito_id:int
    producto_id:int
    cantidad:int
    class Config:
        orm_mode=True

class CarritoItemsResponse(BaseModel):
    id: int
    carrito_id:int
    producto_id:int
    cantidad:int
    class Config:
        orm_mode=True

class CarritoTotalResponse(BaseModel):
    id: int
    usuario_id:int
    total:float
    class Config:
        orm_mode=True