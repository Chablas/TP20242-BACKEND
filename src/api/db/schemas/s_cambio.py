from pydantic import BaseModel

class CambioCompleto(BaseModel):
    id: int
    abbr_primary:str
    abbr_secondary:str
    compra:float
    venta:float
    class Config:
        orm_mode=True