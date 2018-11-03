import telegram
from telegram.ext import Updater
import logging, math
from random import randint, shuffle
from telegram.ext import CommandHandler, MessageHandler, Filters

bot = telegram.Bot(token="")

print("I'm Online")

amigos = {}

updater = Updater(token="")
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def regalo(bot,bottom,top,admins):
	if top in amigos.keys():
		l = "Tu eres el senpai secreto de " + admins[bottom] + " (Lo puedes encontrar en: https://t.me/" + bottom + ")"
		bot.send_message(chat_id=amigos[top], text=l)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Holi, para inscribirse en el senapi secreto solo tienes que escribir /Padoru")

def postular(bot,update):
	if bot.get_chat(update.message.chat_id).username in amigos.keys():
		bot.send_message(chat_id=update.message.chat_id, text="Ya estas inscrito, no te preocupes.")
	else:
		amigos[bot.get_chat(update.message.chat_id).username] = update.message.chat_id
		bot.send_message(chat_id=update.message.chat_id, text="Postulaste al Senpai Secreto")
		backupamigos = open("amigos.txt","a")
		backupamigos.write(bot.get_chat(update.message.chat_id).username + ";;;" + str(update.message.chat_id))
		backupamigos.close()

def echo(bot, update):
	texto = bot.get_chat(update.message.chat_id).username + " Dijo " + update.message.text 
	bot.send_message(chat_id=update.message.chat_id, text=texto)

def otps(bot, update):

	print(bot.get_chat(update.message.chat_id).type)

	if bot.get_chat(update.message.chat_id).type == "private" or bot.get_chat(update.message.chat_id).type == "channel":
		bot.send_message(chat_id=update.message.chat_id, text="Este comando solo funciona en grupos o supergrupos")
		return

	perso = []
	admins = {}

	for i in bot.get_chat_administrators(update.message.chat_id):
		admins[i.user.username] = i.user.first_name

	todavia_no = True
	warn = "Falta que"

	for i in admins.keys():
		if i not in amigos.keys():
			#todavia_no = False
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
		bot.send_message(chat_id=update.message.chat_id, text="Porfa hablenme en https://t.me/Senapi_bot, para poder asignar senpais secretos.")

start_handler = CommandHandler('start', start)
otps_handler = CommandHandler("otps", otps)
post_handler = CommandHandler("Padoru",postular)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(otps_handler)
dispatcher.add_handler(post_handler)


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

backam = open("amigos.txt","r")
for am in backam:
	n,i = am.split(";;;")
	amigos[n] = i
backam.close()

updater.start_polling()



