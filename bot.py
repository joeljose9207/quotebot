import pyquotegen

# Get a random quote
quote = pyquotegen.get_quote()


# Get a quote by specific category
quote_by_category = pyquotegen.get_quote("inspirational")



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	 # bot.send_message(message.chat.id,message.text)
	   bot.send_message(message.chat.id,quote_by_category)
