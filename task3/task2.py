# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
list1 = []
for i in range(random.randrange(4,10)):
    list1.append(random.randrange(2,10))
print(list1)
temp = 1
for i in range(len(list1)):
    if(i < len(list1) / 2 - 1):
        print(list1[i] * list1[len(list1)- temp])
        temp +=1