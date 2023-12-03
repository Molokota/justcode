import telebot, env

bot = telebot.TeleBot(env.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello World!')

@bot.message_handler(commands=['info'])
def start(message):
    bot.send_message(message.chat.id, 'Информация о боте')

bot.polling()