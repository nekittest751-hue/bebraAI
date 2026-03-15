# Локальная стандартная модель 1.0
class BebraStandard:
    def __init__(self):
        self.name = "BebraStandard 1.0"

    def get_response(self, prompt: str) -> str:
        # Больше слов, чуть сложнее
        return f"[Standard 1.0] Я обдумал ваш запрос: {prompt}. Вот примерный ответ."