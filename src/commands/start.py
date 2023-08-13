from telebot.types import Message
from src.config_bot import Config as config

class Command(object):
    @classmethod
    def default(self, ctx: Message):
        message = f"¡Hola! ¿En qué puedo ayudarte?"
        if not config.secure_user(str(ctx.chat.id)):
            config.add_user(str(ctx.chat.id))
        return message