from pydantic import BaseModel

class HistorialMovimientoResponse(BaseModel):
    id: int
    producto_id:int
    almacen_id:int
    cantidad:int
    tipo_movimiento: str
    created_at:str
    class Config:
        orm_mode = True