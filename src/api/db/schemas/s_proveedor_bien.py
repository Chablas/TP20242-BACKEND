from pydantic import BaseModel

class ProveedorBienCompleto(BaseModel):
    id: int
    precio:float
    codigo:str
    proveedor_id:int
    bien_id:int
    class Config:
        orm_mode=True

class ProveedorBienCreate(BaseModel):
    precio:float
    codigo:str
    proveedor_id:int
    bien_id:int
    class Config:
        orm_mode=True

class ProveedorBienDelete(BaseModel):
    proveedor_id:int
    bien_id:int
    class Config:
        orm_mode=True

class ProveedorBienResponse(BaseModel):
    id: int
    precio:float
    codigo:str
    proveedor_id:int
    bien_id:int
    class Config:
        orm_mode=True