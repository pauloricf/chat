from pydantic import BaseModel


class MessageCreate(BaseModel):
  content: str
  from_user_id: int
  to_user_id: int
  class Config:
    from_attributes = True
    
class MessageResponse(BaseModel):
  id: int
  content: str
  from_user_id: int
  to_user_id: int

  class Config:
    from_attributes = True