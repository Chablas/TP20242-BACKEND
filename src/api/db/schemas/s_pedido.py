from pydantic import BaseModel

class PedidoCompleto(BaseModel):
    id: int
    usuario_id:int
    total:float
    class Config:
        orm_mode=True

class PedidoCreate(BaseModel):
    total:float
    class Config:
        orm_mode=True

class PedidoDetalleCreate(BaseModel):
    pedido_id:int
    producto_id:int
    cantidad:int
    class Config:
        orm_mode=True