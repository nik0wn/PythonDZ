import random
list1 = []
sum = 0
print('На нечётных позициях элементы: ',  end = '')
for i in range(random.randrange(10,20)):
    list1.append(random.randrange(20,100))
    if (list1[i] % 2 != 0):
        print(list1[i], end = ' ')
        sum += list1[i]
print('\nsum = ', sum)