import json

class Config(object):
    token = ''

    @classmethod
    def see_users(self):
        with open("src/db.json", "r+") as f:
            f_json: dict = json.load(f)

            return len([value for value in f_json.keys()])
    
    @classmethod
    def secure_user(self, chat_id: str):
        with open("src/db.json", "r+") as f:
            f_json: dict = json.load(f)

            if chat_id not in f_json.keys():
                return False
            return True

    @classmethod
    def add_user(self, chat_id: str):
        with open("src/db.json", "r+") as f:
            f_json = json.load(f)

            f_json[chat_id] = {'Ai': 'GetGpt', 'Model': 'gpt-3.5-turbo'}
            f.seek(0)
            f.write(json.dumps(f_json, indent = 2))
            f.truncate()
    
    @classmethod
    def setup_Ai(self, chat_id: str, Ai: str, model: str):
        with open("src/db.json", "r+") as f:
            f_json = json.load(f)

            f_json[chat_id] = {'Ai': Ai, 'Model': model}
            f.seek(0)
            f.write(json.dumps(f_json, indent = 2))
            f.truncate()
            