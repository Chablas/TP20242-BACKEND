import os
from fastapi import APIRouter
from fastapi import BackgroundTasks, FastAPI
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from typing import List
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

class EmailSchema(BaseModel):
    email: List[EmailStr]

gestionar_emails = APIRouter()

conf = ConnectionConfig(
    MAIL_USERNAME =EMAIL,
    MAIL_PASSWORD = PASSWORD,
    MAIL_FROM = EMAIL,
    MAIL_PORT = 465,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

html = """
<body style="font-family: Arial, sans-serif; background-color: #f4f4f9; color: #333; margin: 0; padding: 0;">
    <div class="container" style="width: 100%; max-width: 600px; margin: 30px auto; padding: 20px; background-color: #fff; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div class="header" style="text-align: center; margin-bottom: 20px;">
            <!-- Imagen de logo de la empresa -->
            <img src="http://localhost:5173/src/assets/images/logo.jpg" alt="Logo Compusave" style="max-width: 150px; margin-bottom: 20px;">
            <h1 style="font-size: 24px; color: #9b4dca;">¡Gracias por confiar en Compusave!</h1>
        </div>
        <div class="message" style="font-size: 16px; line-height: 1.6;">
            <p>Estimado cliente,</p>
            <p>Queremos expresarte nuestro más sincero agradecimiento por elegir los servicios de <strong>Compusave</strong>. Estamos comprometidos en brindarte la mejor experiencia y soluciones tecnológicas para tus necesidades.</p>
            <p>Tu confianza es nuestra mayor recompensa, y nos sentimos muy orgullosos de tenerte como parte de nuestra familia. Siempre estamos aquí para ayudarte a mantener tus sistemas funcionando de manera óptima.</p>
            <p>Si tienes alguna consulta o necesitas soporte adicional, no dudes en contactarnos. ¡Estamos para ayudarte!</p>
            <p>Recuerda que puedes acceder a nuestro portal de soporte en cualquier momento.</p>
        </div>
        <div class="footer" style="text-align: center; margin-top: 30px; font-size: 14px; color: #777;">
            <p>Gracias nuevamente por ser parte de <strong>Compusave</strong>.</p>
            <p>Atentamente, <br><strong>El equipo de Compusave</strong></p>
            <p><a href="mailto:soporte@compusave.com" style="color: #9b4dca; text-decoration: none;">soporte@compusave.com</a></p>
            <!-- Botón para acceder al soporte -->
            <a href="https://www.compusave.com/soporte" style="display: inline-block; padding: 10px 20px; background-color: #9b4dca; color: #fff; text-decoration: none; border-radius: 4px; margin-top: 20px;">Ir a Soporte</a>
        </div>
    </div>
</body>
"""

@gestionar_emails.post("/email")
async def simple_send(email: EmailSchema) -> JSONResponse:
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"}) 