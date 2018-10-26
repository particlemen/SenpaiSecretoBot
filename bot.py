import telegram
from telegram.ext import Updater
import logging, math
from random import randint, shuffle
from telegram.ext import CommandHandler, MessageHandler, Filters

bot = telegram.Bot(token="791339326:AAFIaGE7FVv7R3f1QzU6E5T6s7mGndXIY50")

print(bot.get_me())

amigos = {}

updater = Updater(token="791339326:AAFIaGE7FVv7R3f1QzU6E5T6s7mGndXIY50")
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def regalo(bot,bottom,top,admins):
	if top in amigos.keys():
		l = "Tu eres el senpai secreto de " + admins[bottom] + " (Lo puedes encontrar en: https://t.me/" + bottom + ")"
		bot.send_message(chat_id=amigos[top], text=l)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Holi, tiene pololi?")

def echo(bot, update):
	amigos[bot.get_chat(update.message.chat_id).username] = update.message.chat_id
	texto = bot.get_chat(update.message.chat_id).username + " Dijo " + update.message.text 
	bot.send_message(chat_id=update.message.chat_id, text=texto)
	print(bot.get_chat(update.message.chat_id))

def otps(bot, update):
	perso = []
	admins = {}
	for i in bot.get_chat_administrators(update.message.chat_id):
		admins[i.user.username] = i.user.first_name

	todavia_no = True
	warn = "Falta que"

	for i in admins.keys():
		if i not in amigos.keys():
			todavia_no = False
			warn = warn + ", " + admins[i] 

	if todavia_no:

		bot.send_message(chat_id=update.message.chat_id, text="Holi, soy el bot Fujoshi, mis otps son:")
		seme = list(admins.keys())
		shuffle(seme)
		uke = []
		amor = ""
		for i in seme:
			flag = True
			while flag:
				bottom = randint(0,len(seme) - 1)
				if seme[bottom] not in uke and seme[bottom] != i:
					flag = False
			amor = amor + admins[i] + " + " + admins[seme[bottom]] + " 😍 \n"
			regalo(bot,seme[bottom],i,admins)
			uke.append(seme[bottom])	

		bot.send_message(chat_id=update.message.chat_id, text=amor)

	else:
		bot.send_message(chat_id=update.message.chat_id, text=warn + " me hablen.")
		bot.send_message(chat_id=update.message.chat_id, text="Porfa hablen, para poder asignar senpais secretos.")

start_handler = CommandHandler('start', start)
otps_handler = CommandHandler("otps", otps)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(otps_handler)


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

updater.start_polling()



