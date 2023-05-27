import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


API_TOKEN = ...
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    return bot.send_message(message.chat.id, 'Добро пожаловать в музыкальный магазин. Список инструментов: /list')


@bot.message_handler(commands=['list'])
def instruments(message):
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(KeyboardButton('Гитара'))
    keyboard.add(KeyboardButton('Пианино'))
    keyboard.add(KeyboardButton('Барабаны'))
    return bot.send_message(message.chat.id, 'Выберите музыкальный инструмент', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def buy(message):
    keyboard = InlineKeyboardMarkup()
    if message.text == 'Гитара':
        keyboard.add(InlineKeyboardButton('Купить (100$)', callback_data='_guitar'))
        with open('photos/guitar.jpg', 'rb') as img:
            return bot.send_photo(message.chat.id, img, reply_markup=keyboard)
    if message.text == 'Пианино':
        keyboard.add(InlineKeyboardButton('Купить (500$)', callback_data='_piano'))
        with open('photos/piano.jpg', 'rb') as img:
            return bot.send_photo(message.chat.id, img, reply_markup=keyboard)
    if message.text == 'Барабаны':
        keyboard.add(InlineKeyboardButton('Купить (300$)', callback_data='_drums'))
        with open('photos/drums.jpg', 'rb') as img:
            return bot.send_photo(message.chat.id, img, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == '_guitar':
        return bot.send_message(call.message.chat.id, 'Вы купили гитару')
    if call.data == '_piano':
        return bot.send_message(call.message.chat.id, 'Вы купили пианино')
    if call.data == '_drums':
        return bot.send_message(call.message.chat.id, 'Вы купили барабаны')


bot.infinity_polling()
