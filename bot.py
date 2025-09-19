import telebot


api = 'Your Telegram Bot Token'

 

bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])

def send_welcome(message):

    bot.reply_to(message, 'Welcome, Teelgram Bot')

 

print('Bot Running....')

bot.polling()
