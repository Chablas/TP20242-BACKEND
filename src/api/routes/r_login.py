from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from src.api.db.schemas.s_token import Token, Usuario
from src.auth.auth import authenticate_user, create_access_token, get_current_user_2
from src.api.db.sesion import get_db
from src.auth.auth import bcrypt_context
from typing import List, Annotated
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from src.api.db.schemas.s_usuarios import UsuarioSesion, UsuarioCreate, UsuarioResponse, UsuarioLogin

login_router = APIRouter(
    prefix="/auth"
)

@login_router.post("/token", response_model=Token)
async def login_for_access_token(entrada: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(entrada.username, entrada.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Usuario no válido.')
    token = create_access_token(user.email, user.id, timedelta(minutes=20))
    return {'access_token': token, 'token_type':'bearer'}

@login_router.get("/validar_usuario/yo", response_model=Usuario, name="Validar el usuario actual")
async def r_obtener_usuario(usuario: Usuario = Depends(get_current_user_2)):
    return usuario