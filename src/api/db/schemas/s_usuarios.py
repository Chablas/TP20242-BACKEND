from pydantic import BaseModel

class UsuarioCompleto(BaseModel):
    id: int
    email:str
    password: str
    islogged: bool
    class Config:
        orm_mode=True

class UsuarioCreate(BaseModel):
    email:str
    password: str
    class Config:
        orm_mode=True

class UsuarioLogin(BaseModel):
    username:str
    password: str
    class Config:
        orm_mode=True

class UsuarioSesion(BaseModel):
    email:str

class UsuarioResponse(BaseModel):
    email:str
    password: str
    islogged: bool
    class Config:
        orm_mode=True