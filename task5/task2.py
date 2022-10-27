# Создайте программу для игры с конфетами человек против человека.
import random
totalСonvention = 2021 
oneMotion = random.randrange(1,10)
if (oneMotion % 2 == 0):
    while(totalСonvention > 0):
        print('Ход бота')
        konf = random.randint(1,10);
        print(konf)
        if(konf % 2 == 0):
            konf+=5
        else:
            konf+=3
        totalСonvention -= konf
        if (totalСonvention <= 0):
            print("Выиграл бот")
            break
        print(f"Осталось конфет {totalСonvention}")
        player = int(input('Ход игрока\n Введите число: '))
        totalСonvention-= player
        if (totalСonvention <= 0):
            print("Выиграл игрок")
            break
else:
    while(totalСonvention > 0):
        player = int(input('Ход игрока\n Введите число: '))
        totalСonvention-= player
        if (totalСonvention <= 0):
            print("Выиграл игрок")
            break
        print('Ход бота')
        konf = random.randint(1,10);
        if(konf % 2 == 0):
            konf+=5
        else:
            konf+=3
        totalСonvention -= konf
        if (totalСonvention <= 0):
            print("Выиграл бот")
            break
        print(f"Осталось конфет {totalСonvention}")