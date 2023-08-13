import json
import telebot
from telebot.types import Message

from src.commands.start import Command as start
from src.commands.help import Command as help
from src.commands.model import Command as model
from src.commands.users import Command as users
from src.commands.config import Command as config
from src.config_bot import Config as botConfig
from src.keep_alive import keep_alive

from api import Api
from ratelimiter import RateLimiter

bot = telebot.TeleBot(token=botConfig.token)

@bot.message_handler(commands=['start'])
def message_handle_start(message: Message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, start.default(message))

@bot.message_handler(commands=['help'])
def message_handle_help(message: Message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, help.default(message))

@bot.message_handler(commands=['model'])
def message_handle_model(message: Message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, model.default())

@bot.message_handler(commands=['config'])
def message_handle_config(message: Message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, config.default(message))

@bot.message_handler(commands=['users'])
def message_handle_model(message: Message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, users.default())

@bot.message_handler(content_types=['text'])
@RateLimiter(max_calls=15, period=60)
def message_handle_text(message: Message):
    bot.send_chat_action(message.chat.id, 'typing', timeout=5)
    with open("src/db.json", 'r') as f:
        f_json = json.load(f)
        communication = []
        
        for chat_id in f_json:
            if str(message.chat.id) in chat_id:
                communication.extend(list(f_json[chat_id].values()))
        communication.append(message.text)
        try:
            response = Api.get_message(*communication)
            bot.send_message(message.chat.id, response)
        except:
            bot.send_message(message.chat.id, "la inteligencia artificial que usa actualmente esta en reposo, espera unas horas a que responda. Ve a /model para configurar la Ai")

if __name__ == '__main__':
    keep_alive()
    bot.infinity_polling()