import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('7699876081:AAE_C3i2trjHhfkxwmdwZ1qkG_3u-2Jesbw')

#Команда site
@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://pstu.ru/')
#Команда start
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет!, {message.from_user.first_name}')
#Фото для пользователя
@bot.message_handler(commands=['photo'])
def getphoto(message):
    file = open('./photo.jpeg', 'rb')
    bot.send_photo(message.chat.id, file)
#Команда help
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Это бот созданный для учебных целей')
#Фото от пользователя
@bot.message_handler(content_types=['setphoto'])
def setphoto(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn2 = types.InlineKeyboardButton('Именить текст', callback_data='edit')
    markup.row(btn1, btn2)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
#Текст от пользователя
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет!, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, f'Отлично!, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'чем занимаешься?':
        bot.send_message(message.chat.id, 'С тобой общаюсь:)!')
    elif message.text.lower() == 'открой сайт политеха':
        webbrowser.open('https://pstu.ru/')
    elif message.text.lower() == 'открой сайт гугл':
        webbrowser.open('https://www.google.ru/')
    elif message.text.lower() == 'открой ютуб':
        webbrowser.open('https://www.youtube.com/')
    elif message.text.lower() == 'скинь фото':
        file = open('./photo.jpeg', 'rb')
        bot.send_photo(message.chat.id, file)
    elif message.text.lower() == 'скинь музыку':
        file2 = open('./po_polyam.mp3', 'rb')
        bot.send_audio(message.chat.id, file2)
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

#Программа будет постоянно выполняться
bot.polling(none_stop=True)