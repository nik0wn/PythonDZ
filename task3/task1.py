# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random
list1 = []
sum = 0
print('На нечётных позициях элементы: ',  end = '')
for i in range(5):
    list1.append(random.randrange(20,100))
    if (i % 2 != 0):
        print(list1[i], end = ' ')
        sum += list1[i]
print('\nsum = ', sum)