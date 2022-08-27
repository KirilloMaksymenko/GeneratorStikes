#project - GeneratorStikes , Author - Maksymenko Kyrylo

import telebot
from generatorST import stiker
import os

bot = telebot.TeleBot("5630183536:AAERV3wkiOcjUP_UlAYR_0VHkZdXSECwxv4")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "/creat")  

@bot.message_handler(commands=['creat'])
def send_welcome(message):
    param = str(message.text).replace("/creat","").replace(" ","")
    if param == "":
        path = stiker("default",message.chat.id)
    else:
        path = stiker(param,message.chat.id)
    
    bot.send_sticker(message.chat.id, open(path, 'rb'))
    os.remove(path)
    print("[INFO] Send/dell fin")

bot.infinity_polling()


	