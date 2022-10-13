# Задайте список из n чисел последовательности (1+1/n)n и выведите на экран их сумму
number = int(input('N = '))
sum = 0
for i in range(1,number + 1):
    sum = (1 + 1 / i) ** i + sum
print(round(sum,2))