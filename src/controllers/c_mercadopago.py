from fastapi import HTTPException, status
from src.api.db.schemas.s_pedido import MercadoPagoCreate
import mercadopago
from dotenv import load_dotenv
import os

load_dotenv()  # Cargar variables de entorno
ACCESS_TOKEN_MERCADOPAGO = os.getenv("ACCESS_TOKEN_MERCADOPAGO")

def c_crear_preferencia(db, entrada:MercadoPagoCreate):
    try:
        print("1")
        sdk = mercadopago.SDK(ACCESS_TOKEN_MERCADOPAGO)
        print("2")
        request_options = mercadopago.config.RequestOptions()
        print("3")
        preference_data = {
            "items": [{
                "title": entrada.title,
                "quantity": entrada.quantity,
                "unit_price": entrada.price,
                "currency_id": "PEN",
            }],
            "back_urls": {
                "success": "https://compusave-frontend.onrender.com/",
                "failure": "https://compusave-frontend.onrender.com/",
                "pending": "https://compusave-frontend.onrender.com/",
            },
            "auto_return": "approved",
        }
        print("4")
        preference_response = sdk.preference().create(preference_data)
        print(preference_response)
        print("5")
        print(preference_response["response"]["id"])
        print("6")
        return preference_response["response"]["id"]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")