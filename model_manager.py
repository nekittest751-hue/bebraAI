from models.bebra_mini import BebraMini
from models.bebra_standard import BebraStandard

class ModelManager:
    def __init__(self):
        self.models = {
            "Mini 1.0": BebraMini(),
            "Standard 1.0": BebraStandard()
        }

    def get_model(self, name: str):
        return self.models.get(name, self.models["Standard 1.0"])
