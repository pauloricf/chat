from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    nome: str
    email: str

class UserResponse(BaseModel):  
    id: int
    username: str
    nome: str
    email: str

    class Config:
        from_attributes = True