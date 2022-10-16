# Реализуйте алгоритм перемешивания списка.
import random
number = int(input('N = '))
list1 = []
for i in range(number):
    list1.append(random.randint(1,100))
print(list1)
random.shuffle(list1)
print(list1)