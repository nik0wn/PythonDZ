# Задайте последовательность чисел.
#  Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
number = [int(number) for number in input('Введите минимум 2 числа: ').split()]
temp = []
for i in number:
    if i not in temp:
        temp.append(i)
temp.sort()
print(temp)
