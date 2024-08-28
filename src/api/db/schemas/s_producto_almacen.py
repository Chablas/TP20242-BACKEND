from pydantic import BaseModel

class ProductoAlmacenCompleto(BaseModel):
    id: int
    producto_id:int
    almacen_id:int
    cantidad:int
    class Config:
        orm_mode=True

class ProductoAlmacenCreate(BaseModel):
    producto_id:int
    almacen_id:int
    cantidad:int
    class Config:
        orm_mode=True

class ProductoAlmacenResponse(BaseModel):
    id: int
    producto_id:int
    almacen_id:int
    cantidad:int
    class Config:
        orm_mode=True