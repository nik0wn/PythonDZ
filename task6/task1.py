import task_rand as pk
numbers_list = pk.rand_list()
result_list = list(filter(lambda n: numbers_list.count(n) == 1, numbers_list))
print(f'Для последовательности {numbers_list}, \n   список уникальных элементов {result_list}')