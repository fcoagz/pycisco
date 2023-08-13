from src.config_bot import Config as config

class Command(object):
    @classmethod
    def default(self):
        message = f"Estos serían los usuarios activos: {config.see_users()}"
        return message