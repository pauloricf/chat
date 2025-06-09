from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from services.messageService import create_message_service, get_messages_between_users_service
from dependencies import get_db
from schemas.messageSchema import MessageCreate, MessageResponse
from models import Message
import jwt

message_router = APIRouter()

@message_router.post("/messages", response_model=MessageResponse)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    return create_message_service(message.content, message.from_user_id, message.to_user_id, db)

@message_router.get("/messages/{user_id}", response_model=list[MessageResponse])
def get_messages_with_user(user_id: int, request: Request, db: Session = Depends(get_db)):
    auth = request.headers.get('authorization')
    if not auth or not auth.startswith('Bearer '):
        raise HTTPException(status_code=401, detail='Token ausente')
    token = auth.split(' ')[1]
    try:
        payload = jwt.decode(token, 'supersecretkey', algorithms=['HS256'])
        my_id = payload.get('user_id')
    except Exception:
        raise HTTPException(status_code=401, detail='Token inválido')
    messages = get_messages_between_users_service(my_id, user_id, db)
    return messages or []
