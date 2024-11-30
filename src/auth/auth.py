from fastapi import HTTPException, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi.params import Depends
from src.api.db.models.m_usuarios import Usuario as UsuarioModel
from datetime import timedelta, datetime
from jose import JWTError, jwt
from typing import Annotated
from sqlalchemy.orm import Session
from src.api.db.sesion import get_db
from src.api.db.schemas.s_token import Usuario
import bcrypt

SECRET_KEY = 'AS7FD6SGF7F69GH7FG9H8798F76G9F8DG6SF79H8S79H87FG9H8SGF798J798M7NVB979V87E9'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def authenticate_user(username: str, password: str, db):
    try:
        user =db.query(UsuarioModel).filter(UsuarioModel.email==username).first()
        if not user:
            return False
        if not bcrypt_context.verify(password, user.password):
            return False
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token:Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Usuario inválido')
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Usuario inválido')
    
async def get_current_user_2(token:Annotated[str, Depends(oauth2_bearer)], db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario inválido")
        
        user = db.query(UsuarioModel).get(user_id)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado")

        return Usuario(email=user.email, id=user.id)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario inválido")