from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from model_manager import ModelManager
import json
import os

app = FastAPI(title="bebraAI 1.0")

# Настройка CORS
frontend_url = os.getenv("FRONTEND_URL", "*")  # Можно "*" для теста
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем фронтенд
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Менеджер моделей
model_manager = ModelManager()

# История чата
os.makedirs("data", exist_ok=True)
chat_history_file = "data/chat_history.json"
try:
    with open(chat_history_file, "r", encoding="utf-8") as f:
        chat_history = json.load(f)
except:
    chat_history = []

@app.get("/")
def home():
    return {"message": "bebraAI 1.0 работает на Render!"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    model_name = data.get("model", "Standard 1.0")

    model = model_manager.get_model(model_name)
    response = model.get_response(message)

    chat_history.append({"user": message, "model": model_name, "response": response})

    with open(chat_history_file, "w", encoding="utf-8") as f:
        json.dump(chat_history, f, ensure_ascii=False, indent=2)

    return {"response": response}
