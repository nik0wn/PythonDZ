# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random
list1 = []
min = 10
max = 0
for i in range(random.randrange(2,10)):
    list1.append(random.uniform(1,5))
for i in range(len(list1)):
    list1[i] = list1[i] % 1
    if (list1[i] > max):
        max = round(list1[i],2)
    if (list1[i] < min):
        min = round(list1[i],2)
print(max - min)