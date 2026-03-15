from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from model_manager import ModelManager
import json
import os

app = FastAPI(title="bebraAI 1.0")

# Разрешаем CORS для фронтенда Render
frontend_url = os.getenv("FRONTEND_URL", "*")  # можно указать домен фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url],  # или ["*"] для теста
    allow_methods=["*"],
    allow_headers=["*"],
)

model_manager = ModelManager()

# История чата
try:
    with open("data/chat_history.json", "r", encoding="utf-8") as f:
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

    with open("data/chat_history.json", "w", encoding="utf-8") as f:
        json.dump(chat_history, f, ensure_ascii=False, indent=2)

    return {"response": response}