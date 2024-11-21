from pydantic import BaseModel

class RolCompleto(BaseModel):
    id: int
    nombre:str
    class Config:
        orm_mode=True

class RolCreate(BaseModel):
    nombre:str
    class Config:
        orm_mode=True

class RolUpdate(BaseModel):
    nombre:str
    class Config:
        orm_mode=True

class RolResponse(BaseModel):
    id: int
    nombre:str
    class Config:
        orm_mode=True