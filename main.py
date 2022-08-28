#project - GeneratorStikes , Author - Maksymenko Kyrylo

import telebot
from generatorST import stiker
from sorterStiker import sort
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
        path = stiker(f"{message.chat.id}\\{param}",message.chat.id)
    
    bot.send_sticker(message.chat.id, open(path, 'rb'))
    os.remove(path)
    print("[INFO] Send/dell fin")


@bot.message_handler(content_types=['document'])
def handle_text_doc(message):
    file_name = message.document.file_name
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f"source\\temp\\{file_name}", 'wb') as new_file:
        new_file.write(downloaded_file)
    sort(file_name,message.chat.id)
    
    

bot.infinity_polling()


	