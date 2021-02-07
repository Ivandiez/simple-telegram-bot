import telebot
from telebot import types

bot = telebot.TeleBot('')

name = ""
surname = ""
age = 0


# def get_text_message(message):
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, чем я могу Вам помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напишите Привет")
#     else:
#         bot.send_message(message.from_user.id, "Я Вас не понимаю, напишите /help.")
#
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/reg":
        bot.send_message(message.from_user.id, "Как Вас зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Напишите /reg")


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у Вас фамилия?")
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько Вам лет?');
    bot.register_next_step_handler(message, get_age);


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text="Да", callback_data="yes")
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text="Нет", callback_data="no")
        keyboard.add(key_no)
        if age == 1:
            question = "Вам " + str(age) + " год, Вас зовут " + name + " " + surname + "?"
        elif age == 2 or age == 3 or age == 4:
            question = "Вам " + str(age) + " года, Вас зовут " + name + " " + surname + "?"
        elif age == 11 or age == 12 or age == 13 or age == 14 or age == 15 or age == 16 \
                or age == 17 or age == 18 or age == 19:
            question = "Вам " + str(age) + " лет, Вас зовут " + name + " " + surname + "?"
        elif str(age).endswith("1"):
            question = "Вам " + str(age) + " год, Вас зовут " + name + " " + surname + "?"
        elif str(age).endswith("2") or str(age).endswith("3") or str(age).endswith("4"):
            question = "Вам " + str(age) + " года, Вас зовут " + name + " " + surname + "?"
        else:
            question = "Вам " + str(age) + " лет, Вас зовут " + name + " " + surname + "?"
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню : )');
    elif call.data == "no":
        #переспрашиваем
        bot.send_message(call.message.chat.id, "Введите данные заново.")


bot.polling(none_stop=True, interval=0)
