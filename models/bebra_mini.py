# Локальная мини-модель 1.0
class BebraMini:
    def __init__(self):
        self.name = "BebraMini 1.0"

    def get_response(self, prompt: str) -> str:
        # Простейшая генерация текста (можно потом подключить transformers)
        return f"[Mini 1.0] Ответ на: {prompt}"