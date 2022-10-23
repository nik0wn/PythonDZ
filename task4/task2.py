# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
number = int(input('N = '))
delit = 2
while(number > 1):
    if(number % delit == 0):
        number /= delit
        print(delit)
    else:
        delit+=1