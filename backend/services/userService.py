from sqlalchemy.orm import Session
from models import User
from schemas.userSchema import UserCreate
from fastapi import HTTPException

def create_user_service(user: UserCreate, db: Session):
    db_user = db.query(User).filter((User.email == user.email) | (User.username == user.username)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Usuário ou e-mail já cadastrado")
    new_user = User(
        username=user.username,
        password=user.password,
        nome=user.nome,
        email=user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users_service(db: Session):
    return db.query(User).all()

def get_user_service(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

def update_user_service(user_id: int, user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db_user.nome = user.nome
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user_service(user_id: int, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(db_user)
    db.commit()
    return {"message": "Usuário deletado com sucesso"}