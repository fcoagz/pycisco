from api import ai, models

models = [model.name for model in models]

class Command(object):
    @classmethod
    def default(self):
        message = "Estas son las Inteligencias Artificiales disponibles:\n\n"
        message += f"- {ai[0]}: {models[-1]}\n- {ai[1]}: {models[-1]}\n- {ai[2]}: {models[-1]}\n- {ai[3]}: {', '.join(models[:3])}\n- {ai[4]}: {models[-1]}"

        return message