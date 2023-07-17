import pyquotegen
import telebot



API_TOKEN = '6032893870:AAGhM3l6W-W8t9TsCyRMC2-mntJ1EUhEKHM'
bot = telebot.TeleBot(API_TOKEN)
# Get a random quote
quote = pyquotegen.get_quote()


# Get a quote by specific category
quote_by_category = pyquotegen.get_quote("inspirational")



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	 # bot.send_message(message.chat.id,message.text)
	   bot.send_message(message.chat.id,quote_by_category)
	   bot.send_message("helo")
#Handle The '/ask'
@bot.message_handler(commands=['ask'])
def first_process(message):
	bot.send_message(message.chat.id,"Send Me your Question")
	bot.register_next_step_handler(message,second_process)
def again_send(message):
  bot.register_next_step_handler(message,second_process)
def second_process(message):
  bot.send_message(message.chat.id,get_response(message.text))
  again_send(message)

 
bot.infinity_polling()
