from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from db import engine, Base, SessionLocal
from routes.userRoutes import user_router, login, get_me, get_users, create_user
from routes.messageRoutes import message_router
from services.messageService import create_message_service

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

# Gerenciador simples de conexões WebSocket
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            # Salva a mensagem no banco
            db = SessionLocal()
            try:
                create_message_service(
                    content=data["content"],
                    from_user_id=data["from_user_id"],
                    to_user_id=data["to_user_id"],
                    db=db
                )
            finally:
                db.close()
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.get("/")
def read_root():
  return {"message": "Hello, World!"}
