# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
number = int(input("Введите число: "))
if(number >=1 and number <=7):
    if(number >= 6 and number <=7):
        print("Выходной")
    else:
        print("Рабочий")
    