from telebot.types import Message
from src.config_bot import Config as config
from api import ai, models

class Command(object):
    @classmethod
    def default(self, ctx: Message):
        if not len(ctx.text.split()) == 3:
            return "Por favor, ingrese los tres valores requeridos: /config <Ai> <Modelo>"
        
        Ai, model = ctx.text.split()[1:]
        list_ai = [ai.lower() for ai in ai]

        if not Ai.lower() in list_ai:
            return "La Ai que proporciona no está disponible."
        
        if model not in [model.name for model in models]:
            return "El modelo que proporciona no está disponible."
        
        i = list_ai.index(Ai.lower())
        config.setup_Ai(str(ctx.chat.id), Ai=ai[i], model=model)
        return "Los cambios se realizaron con éxito."
        