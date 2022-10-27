import telebot
from telebot import types

token = '5608814459:AAGktPtlA98mfqpwfj-KZREIE3jev6wGulA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}!\nВыполните команду "/button" чтобы увидеть больше</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item1 = types.KeyboardButton('Start')
    item2 = types.KeyboardButton('Help')
    item3 = types.KeyboardButton("finish")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Кнопки', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'И тебе не хворать!', parse_mode='html')
    elif message.text == 'ID':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
    elif message.text == "Start":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("finish")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
    elif message.text == "finish":
        bot.send_message(message.chat.id, 'Спасибо! Надеюсь, когда-нибудь снова сможем поговорить.')



bot.polling(none_stop=True)