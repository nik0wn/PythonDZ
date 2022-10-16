# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import random
i = 0
sum = 1
file = open('file.txt', 'w')
while(i < 3):
    file.write(str(random.randint(1,10)))
    file.write('\n')
    i+=1
file.close()
number = int(input('N = '))
listN = []
for i in range(-number, number + 1):
    listN.append(i)
print(listN)
file = open('file.txt', 'r')
for i in file:
    sum *= listN[int(i)]
file.close()
print(sum)