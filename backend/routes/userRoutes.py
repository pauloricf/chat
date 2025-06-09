from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas.userSchema import UserCreate, UserResponse
from services.userService import (
    create_user_service,
    get_users_service,
    get_user_service,
    update_user_service,
    delete_user_service,
)
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import datetime
from models import User

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

user_router = APIRouter()
security = HTTPBearer()

@user_router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(user, db)

@user_router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return get_users_service(db)

@user_router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_service(user_id, db)

@user_router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user_service(user_id, user, db)

@user_router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user_service(user_id, db)

@user_router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):
    email = data.get("email")
    password = data.get("password")
    user = db.query(User).filter(User.email == email).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    payload = {
        "user_id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"token": token}

@user_router.get("/me")
def get_me(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return {"id": user.id, "nome": user.nome, "email": user.email}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido")

# Exportar handlers para uso direto no main.py
__all__ = ["user_router", "login", "get_me", "get_users"]