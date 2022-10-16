# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
number= int(input('N = '))
list1 = []
fib1 = 0 
fib2 = 1
list1.insert(0,fib1)
list1.insert(0,fib2)
for i in range(1,number):
    fib1, fib2 = fib2, fib1 - fib2
    list1.insert(0,fib2)
fib1 = fib2 = 1
list1.append(fib1)
list1.append(fib2)
for i in range(2,number):
    fib1, fib2 = fib2, fib1 + fib2
    list1.append(fib2)
print(list1)