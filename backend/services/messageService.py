from hmac import new
from sqlalchemy.orm import Session
from models import Message


def create_message_service(content: str, from_user_id: int, to_user_id: int, db: Session):
    new_message = Message(content=content, from_user_id=from_user_id, to_user_id=to_user_id)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message


def get_messages_between_users_service(user1_id: int, user2_id: int, db: Session):
    return db.query(Message).filter(
        ((Message.from_user_id == user1_id) & (Message.to_user_id == user2_id)) |
        ((Message.from_user_id == user2_id) & (Message.to_user_id == user1_id))
    ).order_by(Message.id).all()