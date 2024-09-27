from pydantic import BaseModel

class ServicioCompleto(BaseModel):
    id: int
    condiciones_previas:str
    servicio_incluye:str
    servicio_no_incluye:str
    restricciones:str
    producto_id:int
    class Config:
        orm_mode=True

class ServicioCreate(BaseModel):
    nombre:str
    informacion_general:str
    precio:float
    garantia:str
    estado:bool
    imagen: str

    condiciones_previas:str
    servicio_incluye:str
    servicio_no_incluye:str
    restricciones:str
    class Config:
        orm_mode=True

class ServicioUpdate(BaseModel):
    nombre:str
    informacion_general:str
    precio:float
    garantia:str
    estado:bool
    imagen: str

    condiciones_previas:str
    servicio_incluye:str
    servicio_no_incluye:str
    restricciones:str
    class Config:
        orm_mode=True

class ServicioResponse(BaseModel):
    id: int
    nombre:str
    informacion_general:str
    precio:float
    garantia:str
    estado:bool
    imagen: str

    condiciones_previas:str
    servicio_incluye:str
    servicio_no_incluye:str
    restricciones:str
    producto_id:int
    class Config:
        orm_mode=True