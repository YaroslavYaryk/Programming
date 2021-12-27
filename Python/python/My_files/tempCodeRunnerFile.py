import telebot
from telebot import types

bot = telebot.TeleBot("1505993685:AAG1i0UryPjRjrnxthZTkrD1GRk0h_Xk3xs")

my_id = 534224726


@bot.message_handler(commands=['start'])
def butt(message):
    bot.send_message(message.chat.id, "welcome " + str(message.from_user.username))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    btn1 = types.KeyboardButton('Enter data')
    btn2 = types.KeyboardButton("Exit")
    btn3 = types.KeyboardButton("About")

    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Press the button to see what happen', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def butt_send(message):
    if message.text == 'Enter data':
        bot.send_message(message.chat.id, "name surname, середній бал")
        bot.register_next_step_handler(message, new_funk)
    elif message.text == "Exit":
        bot.send_message(message.chat.id, "walk away , fucking trash")
    elif message.text == "About":
        about = "This bot was created by @yaryk31 in order to know what points everybody got before anonsing original list of student"
        bot.send_message(message.chat.id, about)
    bot.forward_message(my_id, message.chat.id, message.message_id)


def new_funk(message):
    bot.send_message(message.chat.id, "thanks for your answer!!!")
    keyboard = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text="Yes", callback_data="yes")
    item_no = types.InlineKeyboardButton(text="No", callback_data="no")
    keyboard.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'do you like this bot?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == "yes":
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='https://cutt.ly/CjYD0gZ'))
        bot.send_message(call.message.chat.id, "you have to", reply_markup=markup2)
        bot.send_message(call.message.chat.id, '4149499345111965')
    elif call.data == "no":
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='https://cutt.ly/CjYD0gZ'))
        bot.send_message(call.message.chat.id, "You're like", reply_markup=markup1)


bot.polling(none_stop=True)
