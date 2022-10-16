# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = int(input('N = '))
temp = ''
while (number != 0) :
    temp = str(number % 2) + temp
    number //= 2
print(temp)