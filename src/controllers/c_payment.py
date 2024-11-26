from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os
import mercadopago
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno

# Configuración de MercadoPago
sdk = mercadopago.SDK(os.getenv('ACCESS_TOKEN_MERCADOPAGO'))

# Configuración de plantillas HTML
templates = Jinja2Templates(directory="templates")

# Modelo para validar la solicitud de pago
class PayerIdentification(BaseModel):
    type: str
    number: str

class Payer(BaseModel):
    email: str
    identification: PayerIdentification

class PaymentRequest(BaseModel):
    transaction_amount: float
    token: str
    installments: int
    payment_method_id: str
    issuer_id: str
    payer: Payer

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Renderiza la página principal.
    """
    return templates.TemplateResponse(
        "index.html", {"request": request, "public_key": os.getenv('PUBLIC_KEY_MERCADOPAGO')}
    )

@app.post("/process_payment", response_class=JSONResponse)
async def process_payment(payment_request: PaymentRequest):
    """
    Procesa el pago utilizando MercadoPago.
    """
    payment_data = {
        "transaction_amount": payment_request.transaction_amount,
        "token": payment_request.token,
        "installments": payment_request.installments,
        "payment_method_id": payment_request.payment_method_id,
        "issuer_id": payment_request.issuer_id,
        "payer": {
            "email": payment_request.payer.email,
            "identification": {
                "type": payment_request.payer.identification.type,
                "number": payment_request.payer.identification.number,
            },
        },
    }

    try:
        # Crear el pago en MercadoPago
        payment_response = sdk.payment().create(payment_data)
        payment = payment_response["response"]

        print("status =>", payment["status"])
        print("status_detail =>", payment["status_detail"])
        print("id =>", payment["id"])

        return JSONResponse(content=payment, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando el pago: {str(e)}")