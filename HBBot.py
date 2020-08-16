import telebot 

bot = telebot.TeleBot('1396056288:AAFvLocEmnwVFxI9jEKXwE0lUntZq_8cZPg')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 
'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')

@bot.message_handler(commands=['start'])                               #Декоратор
def start_message(message):
    bot.send_message(message.chat.id, "Выберите месяц", reply_markup = keyboard1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Январь':                                       #Сообщение пользователя
        bot.send_message(message.chat.id, '05 - Января - Алексей К')   #Ответа бота на сообщение выше
        bot.send_message(message.chat.id, '08 - Января - Жанна')
        bot.send_message(message.chat.id, '11 - Января - Ксюша')
        bot.send_message(message.chat.id, '16 - Января - Настя')
        bot.send_message(message.chat.id, '27 - Января - Костя')
    elif message.text == 'Февраль':
        bot.send_message(message.chat.id, '22 - Февраля - Франц Елисей')
        bot.send_message(message.chat.id, '23 - Февраля - Алексей')
        bot.send_message(message.chat.id, '25 - Февраля - Егор')
    elif message.text == 'Март':
        bot.send_message(message.chat.id, '09 - Марта - т.Люба')
        bot.send_message(message.chat.id, '11 - Марта - Татьяна')
    elif message.text == 'Апрель':
        bot.send_message(message.chat.id, '30 - Апреля - Настя')
    elif message.text == 'Май':
        bot.send_message(message.chat.id, '06 - Мая - Рощикова Арина')
        bot.send_message(message.chat.id, '13 - Мая - Франц Екатерина')
    elif message.text == 'Июнь':
        bot.send_message(message.chat.id, '09 - Июня - Саша')
        bot.send_message(message.chat.id, '09 - Июня - Нина')
        bot.send_message(message.chat.id, '12 - Июня - Вова')
        bot.send_message(message.chat.id, '09 - Июня - Гусельникова Галина')
    elif message.text == 'Июль':
        bot.send_message(message.chat.id, '07 - Июля - Кристина')
        bot.send_message(message.chat.id, '07 - Июля - Гусельников Владимир Алексеевич')
        bot.send_message(message.chat.id, '15 - Июля - д.Сергей')
        bot.send_message(message.chat.id, '22 - Июля - Вика')
    elif message.text == 'Август':
        bot.send_message(message.chat.id, '04 - Августа - Вова')
        bot.send_message(message.chat.id, '04 - Августа - Ирина')
        bot.send_message(message.chat.id, '05 - Августа - Ксюша')
        bot.send_message(message.chat.id, '06 - Августа - Леша')
        bot.send_message(message.chat.id, '06 - Августа - Елена')
        bot.send_message(message.chat.id, '08 - Августа - д.Саша')
        bot.send_message(message.chat.id, '27 - Августа - Татьяна')
        bot.send_message(message.chat.id, '27 - Августа - Алексей')
    elif message.text == 'Сентябрь':
        bot.send_message(message.chat.id, '03 - Сентября - Тимофей')
        bot.send_message(message.chat.id, '11 - Сентября - Настя')
        bot.send_message(message.chat.id, '11 - Сентября - Виктор')
    elif message.text == 'Октябрь':
        bot.send_message(message.chat.id, '05 - Октября - Гусельников Станислав')
        bot.send_message(message.chat.id, '21 - Октября - т.Нина')
    elif message.text == 'Ноябрь':
        bot.send_message(message.chat.id, '03 - Ноября - Денис Ш.')
        bot.send_message(message.chat.id, '09 - Ноября - Сергей.')
        bot.send_message(message.chat.id, '09 - Ноября - Люба')
        bot.send_message(message.chat.id, '12 - Ноября - Гусельников Михаил')
        bot.send_message(message.chat.id, '17 - Ноября - Рощикова Милана')
        bot.send_message(message.chat.id, '30 - Ноября - Алексей Ш.')
    elif message.text == 'Декабрь':
        bot.send_message(message.chat.id, '04 - Декабря - Лена (Леша)')
        bot.send_message(message.chat.id, '12 - Декабря - Ирина')
        bot.send_message(message.chat.id, '22 - Декабря - Виктор')
        bot.send_message(message.chat.id, '29 - Декабря - Гусельникова Елена')
        
bot.polling()