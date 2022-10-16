# Задайте список из n чисел последовательности (1+1/n)n и выведите на экран их сумму
number = int(input('N = '))
list1 = []
for i in range(1,number + 1):
    list1.append( (1 + 1 / i) ** i)
print(list1)
print(round(sum(list1),2))