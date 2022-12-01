import log
import telebot
from telebot import types

token = "5844681447:AAHIwFBwqRrK5VHHzikHVZARjLqadCuEYRg"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def Menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1. Сложить")
    btn2 = types.KeyboardButton("2. Вычесть")
    btn3 = types.KeyboardButton("3. Умножить")
    btn4 = types.KeyboardButton("4. Разделить")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def Fun(message):
    if (message.text == "1. Сложить"):
        bot.send_message(message.chat.id, "Введите два числа через пробел")
        bot.register_next_step_handler(message, Get_Suma)
    if (message.text == "2. Вычесть"):
        bot.send_message(message.chat.id, "Введите два числа через пробел")
        bot.register_next_step_handler(message, Get_Minus)
    if (message.text == "3. Умножить"):
        bot.send_message(message.chat.id, "Введите два числа через пробел")
        bot.register_next_step_handler(message, Get_Multiplications)
    if (message.text == "4. Разделить"):
        bot.send_message(message.chat.id, "Введите два числа через пробел")
        bot.register_next_step_handler(message, Get_Division)

def Get_Suma(message):
    numbers = list(map(float,message.text.split(" ")))
    result = numbers[0] + numbers[1]
    bot.send_message(message.chat.id, "Результат:")
    bot.send_message(message.chat.id, result)
    log.Suma_log(numbers[0], numbers[1], result)
    Menu(message)
    bot.register_next_step_handler(message,Fun)

def Get_Minus(message):
    numbers = list(map(float,message.text.split(" ")))
    result = numbers[0] - numbers[1]
    bot.send_message(message.chat.id, "Результат:")
    bot.send_message(message.chat.id, result)
    log.Minus_log(numbers[0], numbers[1], result)
    Menu(message)
    bot.register_next_step_handler(message,Fun)

def Get_Multiplications(message):
    numbers = list(map(float,message.text.split(" ")))
    result = numbers[0] * numbers[1]
    bot.send_message(message.chat.id, "Результат:")
    bot.send_message(message.chat.id, result)
    log.Multiplications_log(numbers[0], numbers[1], result)
    Menu(message)
    bot.register_next_step_handler(message,Fun)

def Get_Division(message):
    numbers = list(map(float,message.text.split(" ")))
    result = numbers[0] / numbers[1]
    bot.send_message(message.chat.id, "Результат:")
    bot.send_message(message.chat.id, result)
    log.Division_log(numbers[0], numbers[1], result)
    Menu(message)
    bot.register_next_step_handler(message,Fun)
    
bot.polling(non_stop= True)