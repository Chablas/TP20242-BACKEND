from pydantic import BaseModel

class BienCompleto(BaseModel):
    id: int
    marca:str
    especificaciones_tecnicas:str
    producto_id:int
    class Config:
        orm_mode=True

class BienCreate(BaseModel):
    nombre:str
    informacion_general:str
    precio:float
    garantia:str
    estado:bool
    imagen: str

    marca:str
    especificaciones_tecnicas:str
    categoria_id:int
    class Config:
        orm_mode=True

class BienUpdate(BaseModel):
    nombre:str
    informacion_general:str
    precio:float
    garantia:str
    estado:bool
    imagen: str

    marca:str
    especificaciones_tecnicas:str
    categoria_id:int
    class Config:
        orm_mode=True

class BienResponse(BaseModel):
    id: int
    nombre:str
    informacion_general:str
    precio:float
    garantia:str
    estado:bool
    imagen: str
    
    marca:str
    especificaciones_tecnicas:str
    producto_id:int
    categoria_id:int
    class Config:
        orm_mode=True