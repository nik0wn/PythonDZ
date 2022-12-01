import delete
import write
import print1
import print2
import edit
import search
import telebot
from telebot import types

token = "5844681447:AAHIwFBwqRrK5VHHzikHVZARjLqadCuEYRg"
bot = telebot.TeleBot(token)

person = []

@bot.message_handler(commands=["start"])
def Menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1. Вывести все записи.")
    btn2 = types.KeyboardButton("2. Вывод определенных данных")
    btn3 = types.KeyboardButton("3. Добавить запись.")
    btn4 = types.KeyboardButton("4. Найти запись.")
    btn5 = types.KeyboardButton("5. Изменить запись.")
    btn6 = types.KeyboardButton("6. Удалить запись.")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, "Привет как дела", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def Fun_Menu(message):
    if (message.text == "1. Вывести все записи."):
        list1 = print1.print_fale()
        for i in list1:
            bot.send_message(message.chat.id,i)
    elif(message.text == "3. Добавить запись."):
        bot.send_message(message.chat.id,"Введите ID")
        bot.register_next_step_handler(message, Get_ID)
        write.New_Entry()

def Get_ID(message):
    IDm = message.text
    global person
    person.append(IDm)
    bot.send_message(message.chat.id,"Введите фамилию")



bot.polling(non_stop= True)