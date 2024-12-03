from fastapi import HTTPException, status
from src.api.db.schemas.s_pedido import MercadoPagoCreate
import mercadopago
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()  # Cargar variables de entorno
ACCESS_TOKEN_MERCADOPAGO = os.getenv("ACCESS_TOKEN_MERCADOPAGO")

def c_crear_preferencia(db, entrada:List[MercadoPagoCreate]):
    try:
        sdk = mercadopago.SDK(ACCESS_TOKEN_MERCADOPAGO)
        request_options = mercadopago.config.RequestOptions()
        items = []
        for item in entrada:
            objeto = {
                "title": item.title,
                "quantity": item.quantity,
                "unit_price": item.price,
                "currency_id": "PEN",
            }
            items.append(objeto)
        preference_data = {
            "items": items,
            "back_urls": {
                "success": "https://compusave-frontend.onrender.com/",
                "failure": "https://compusave-frontend.onrender.com/",
                "pending": "https://compusave-frontend.onrender.com/",
            },
            "auto_return": "approved",
        }
        preference_response = sdk.preference().create(preference_data)
        return preference_response["response"]["id"]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")