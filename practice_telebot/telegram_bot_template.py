import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


API_TOKEN = ...
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    ...


@bot.message_handler(commands=['list'])
def instruments(message):
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(KeyboardButton(...))
    keyboard.add(KeyboardButton(...))
    keyboard.add(KeyboardButton(...))
    return bot.send_message(message.chat.id, ..., reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def buy(message):
    keyboard = InlineKeyboardMarkup()
    if message.text == ...:
        keyboard.add(InlineKeyboardButton(..., callback_data=...))
        with open(..., 'rb') as img:
            return bot.send_photo(message.chat.id, img, reply_markup=keyboard)
    if message.text == ...:
        keyboard.add(InlineKeyboardButton(..., callback_data=...))
        with open(..., 'rb') as img:
            return bot.send_photo(message.chat.id, img, reply_markup=keyboard)
    if message.text == ...:
        keyboard.add(InlineKeyboardButton(..., callback_data=...))
        with open('photos/drums.jpg', 'rb') as img:
            return bot.send_photo(message.chat.id, img, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == ...:
        return bot.send_message(call.message.chat.id, ...)
    if call.data == ...:
        return bot.send_message(call.message.chat.id, ...)
    if call.data == ...:
        return bot.send_message(call.message.chat.id, ...)


bot.infinity_polling()
