import telebot
import pprint
import time

token = '6565535139:AAHNbWTCvVozktkxFE6g1F4_TBX22ttFtaY'

bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, text='Как твои дела? Чем могу помочь')
@bot.message_handler(commands=['timer'])
def say(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i+1)

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)
    file_ID = 'CAACAgIAAxkBAAMbZfhi_wGnwgq-DL6Z0jce-RwwzWEAAoEYAALXw_hIxqzFnBJJ1oc0BA'
    bot.send_sticker(message.chat,id,file_ID)

@bot.message_handler(commands=['say'])
def say(message):
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, text=f'***{text.upper()}!***')
@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, text='Текст содержит слово плохой')
        return
    text = message.text[::-1]
    bot.reply_to(message, text)

bot.polling()



