from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import engine, Base
from routes.userRoutes import user_router, login, get_me, get_users, create_user
from routes.messageRoutes import message_router

app = FastAPI()

# Configuração de CORS global
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique o domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Base.metadata.create_all(bind=engine)

# Rotas de autenticação e usuário SEM prefixo /api
app.add_api_route("/login", login, methods=["POST"])
app.add_api_route("/me", get_me, methods=["GET"])
app.add_api_route("/users", get_users, methods=["GET"])
app.add_api_route("/register", create_user, methods=["POST"])

# Rotas de usuário e mensagem com prefixo /api
app.include_router(user_router, prefix="/api", tags=["api"])
app.include_router(message_router, prefix="/api", tags=["api"])


@app.get("/")
def read_root():
  return {"message": "Hello, World!"}
