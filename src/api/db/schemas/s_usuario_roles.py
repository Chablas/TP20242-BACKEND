from pydantic import BaseModel

class UsuarioRolCompleto(BaseModel):
    id: int
    usuario_id:int
    rol_id:int
    class Config:
        orm_mode=True

class UsuarioRolCreate(BaseModel):
    usuario_id:int
    rol_id:int
    class Config:
        orm_mode=True

class UsuarioRolDelete(BaseModel):
    usuario_id:int
    rol_id:int
    class Config:
        orm_mode=True

class UsuarioRolUpdate(BaseModel):
    usuario_id:int
    rol_id:int
    class Config:
        orm_mode=True

class UsuarioRolResponse(BaseModel):
    usuario_id:int
    rol_id:int
    class Config:
        orm_mode=True