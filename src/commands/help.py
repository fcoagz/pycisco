from telebot.types import Message

help_message = """
Hola {0}!. PyCisco es un bot de Telegram que te permite comunicarte con una inteligencia artificial de forma gratuita (por el momento). El bot comprende el mensaje que le envías y utiliza herramientas de lenguaje natural para analizar el sentimiento del mensaje. Fue desarrollado por Francisco Griman. 

Comandos disponibles:
- /start: Muestra un mensaje de bienvenida del bot.
- /model: Muestra los modelos de lenguaje disponibles para la configuración.
- /config: Configura la inteligencia artificial y el modelo de lenguaje que deseas utilizar. Ejemplo: /config <AI> <Modelo>. El bot detectará automáticamente los cambios y los guardará en la base de datos.
"""

class Command(object):
    @classmethod
    def default(self, ctx: Message):
        return help_message.format(ctx.from_user.first_name)