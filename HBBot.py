import telebot 

bot = telebot.TeleBot('1396056288:AAFvLocEmnwVFxI9jEKXwE0lUntZq_8cZPg')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])                  #Декоратор
def start_message(message):
    bot.send_message(message.chat.id, "Привет, пуська", reply_markup = keyboard1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':                          #Сообщение пользователя
        bot.send_message(message.chat.id, 'Слався Кей')   #Ответа бота на сообщение выше
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, Кей')

bot.polling()