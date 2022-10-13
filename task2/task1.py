# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input('Введите число: ')
sum = 0
for i in range(len(number)):
    if(number[i] != '.'):
        sum = sum + int(number[i])
print(sum)