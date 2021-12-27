import datetime
import telebot
from telebot import types
import pyowm

bot = telebot.TeleBot("1591290167:AAHJIsUlsncApxtnhxd7LfQqPIucsW1FYqk")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message.chat.id,  "welcome, bro")
	murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
	butt1 = types.KeyboardButton("menu")
	butt2 = types.KeyboardButton("exit")
	murkup.add(butt1, butt2)
	bot.send_message(message.chat.id, "choose one" , reply_markup=markup)

@bot.message_handler(content_types=['text'])
def button(message):
	if message.text == "menu":
		keyboard = types.InlineKeyboardMarkup()
		horoskop = types.InlineKeyboardButton(text = "Horoskope", callback_data="horoskope")
		exchange_rate = types.InlineKeyboardButton(text ="exchange_rate", callback_data= "money")
		exect_time = types.InlineKeyboardButton(text = "exect time", callback_data="time")
		keyboard.add(horoskop,exchange_rate,exect_time)
		bot.send_message(message.chat.id, "this is menu choose what you wanna do", reply_markup = keyboard)


	elif message.text == "exit":
		bot.send_message(message.chat.id, "have a nice day")


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
	if call.data =="horoscope":
		keyboard2 = types.InlineKeyboardMarkup()
		aries = types.InlineKeyboardButton(text = "Aries", callback_data="aries")
		taurus = types.InlineKeyboardButton(text = "Taurus", callback_data="taurus")
		gemini = types.InlineKeyboardButton(text = "Gemini", callback_data="gemini")
		cancer = types.InlineKeyboardButton(text = "Cancer", callback_data="cancer")
		leo = types.InlineKeyboardButton(text = "Leo", callback_data="leo")
		virgo = types.InlineKeyboardButton(text = "Virgo", callback_data="virgo")
		libra = types.InlineKeyboardButton(text = "Libra", callback_data="libra")
		scorpio = types.InlineKeyboardButton(text = "Scorpio", callback_data="scorpio")
		sagittarius = types.InlineKeyboardButton(text = "Sagittarius", callback_data="sagittarius")
		capricorn = types.InlineKeyboardButton(text = "Capricorn", callback_data="capricorn")
		aquarius = types.InlineKeyboardButton(text = "Aquarius", callback_data="aquarius")
		pisces = types.InlineKeyboardButton(text = "Pisces", callback_data="pisces")
		keyboard2.add(aries,taurus,gemini,cancer,leo,virgo,libra,scorpio,sagittarius,capricorn,aquarius,pisces)
		bot.send_message(message.chat.id, "choose your one", reply_markup = keyboard2)

		@bot.callback_query_handler(func=lambda call: True)
		def horoskope_answer(call):
			if call.data == "aries":
				bot.send_message(message.chat.id, "Some deeply buried feelings about your mother and family could come up from the past today and need release. Don't be afraid to show your pain and anger. If you're embarrassed to do it around others, Aries, stay home and deal with it. This is a positive development. By the end of the day you might feel as if a large weight has been lifted from your shoulders.")
			elif call.data == "taurus":
				bot.send_message(message.chat.id, "Group activities in your neighborhood could lead to positive changes in your community. You will enjoy exchanging ideas and information with others, Taurus, and could come away from these activities feeling exhilarated. It might be a good idea to walk home, or perhaps go for coffee or a movie afterward. If you let the ideas buzz until bedtime, you might not be able to sleep.")
			elif call.data == "gemini":
				bot.send_message(message.chat.id, "Today you might find yourself in the public eye. Acknowledgment for work well done could come your way. It might also involve an increase in income. This could be job related or simply a community project that you've been working on and accomplished successfully. Enjoy your 15 minutes of fame, Gemini, even though you might find it a bit disconcerting.")
			elif call.data =="cancer":
				bot.send_message(message.chat.id, "Expanding your horizons is the key for today, Cancer. Communications received from distant states or foreign lands could have you entertaining the idea of traveling to those places. Learning is very much on your mind. You're probably curious about different cultures, ideas, and perspectives. Even though you might not make definite plans for travel now, you're apt to at least consider it.")
			elif call.data =="leo":
				bot.send_message(message.chat.id, " Some very intense dreams could take you back to the past, perhaps your childhood or past lives. Write down any dreams you remember, Leo. They might not make sense to you now, but if you go back and analyze them later, you're likely to find that they reveal a lot about you that you weren't previously aware of. They might even inspire new projects of some kind. Think about them carefully.")
			elif call.data == "virgo":
				bot.send_message(message.chat.id, "An old friend you haven't seen for a while could suddenly reappear, and you might view this person in a different light as a potential business partner, source of inspiration, or even a romantic possibility. If this is your inclination, Virgo, don't write it off without giving it some careful consideration. Partnerships formed today are likely to lead to success.")
			elif call.data == "libra":
				bot.send_message(message.chat.id, "You're a service-oriented person by nature, Libra, and today the opportunity to spend time serving those in need could well present itself. This could be in a professional capacity or helping someone close who's having troubles of some kind. This particular situation won't last long, but it's likely to change your life in a positive way. Don't resist. Go with the flow.")
			elif call.data == "scorpio":
				bot.send_message(message.chat.id, "If you've been hoping for a lucky break, Scorpio, this is the day it might come, especially if it involves love and romance. Or you might have been hoping for acknowledgment on the job, in the field of education, or by someone who means a lot to you. Whatever breaks come your way are likely to move you emotionally. You won't be the same. Have a great day.")	
			elif call.data == "sagittarius":
				bot.send_message(message.chat.id, "Changes in your home could take place now. These are positive, Sagittarius, though they might seem a bit overwhelming. Some could even be described as upheavals. Perhaps someone moves in or out. It could even involve moving to a new place, redecorating, refurbishing, or perhaps adopting a pet. At the very least, expect some emotional changes within yourself.")
			elif call.data == "capricorn":
				bot.send_message(message.chat.id, "Some great news could change your life forever. It might involve a new partnership of some kind or opportunities in your community. At the least, Capricorn, it could involve changes in your outlook and attitudes about life. You could spend a lot of time on the phone with friends and acquaintances. You will probably want to schedule a romantic evening with your partner.")
			elif call.data == "aquarius":
				bot.send_message(message.chat.id, "Some changes regarding your career could make a difference in your resources. This could involve a pending raise or promotion or opportunities for freelance work outside the job. It might imply a new job, perhaps in a creative field. Whatever work you do is likely to seem more emotionally rewarding than it has been, Aquarius. This should boost your spirits considerably.")
			elif call.data == "pisces":
				bot.send_message(message.chat.id, "Today you're likely to feel especially romantic and sexy, and anxious to get together with a love partner. This doesn't mean you aren't in the mood for socializing in general. In fact, you may look forward to meeting with friends. You should be feeling especially creative, and you could spend a lot of your day either planning or working on projects.")

	elif call.data == "money":
		bot.send_message(message.chat.id, "1 dollar == 28.22 ua\n1 euro == 34.08 ua\n1 bitcoin == 1,021,865.28 ua")
	
	elif call.data == "time":
		bot.send_message(message.chat.id, datetime.datetime.now())

	








bot.polling()