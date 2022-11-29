import delete
import write
import print1
import print2
import edit
import search
import telebot
from telebot import types
token = "5697577509:AAFC23GyXMEI2ngw01GRYYH3QiesZBRCFiY"
bot = telebot.TeleBot('5697577509:AAFC23GyXMEI2ngw01GRYYH3QiesZBRCFiY')

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1. Вывести все записи.")
    btn2 = types.KeyboardButton("2. Вывод определенных данных")
    btn3 = types.KeyboardButton("3. Добавить запись.")
    btn4 = types.KeyboardButton("4. Найти запись.")
    btn5 = types.KeyboardButton("5. Изменить запись.")
    btn6 = types.KeyboardButton("6. Удалить запись.")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, "Привет")
    

    # if value == 1:
    #     print1.print_fale()
    # if value == 2:
    #     print2.print_fale1()
    # elif value == 3:
    #    write.New_Entry()
    # elif value == 4:
    #     search.Search_Entry('bd.csv')
    # elif value == 5:
    #     edit.Edit_Entry('bd.csv')
    # elif value == 6:
    #     delete.delete_str('bd.csv')
    # elif value == 7:
    #     print('Ждем вас еще :)')
    #     break
