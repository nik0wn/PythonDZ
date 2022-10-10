# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
number = int(input("Введите число: "))
if(number >= 1 and number <=4):
    if(number == 1):
        print("x = ∞ \ny = ∞")
    elif(number == 2):
        print("x = -∞ \ny = ∞")
    elif(number == 3):
        print("x = -∞ \ny = -∞")
    else:
        print("x = ∞ \ny = -∞")