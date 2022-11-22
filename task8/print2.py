def print_fale1():
    temp = []
    size = []
    while True: 
        temp = int(input(' 1. ID\n 2. Фамилмя\n 3. Имя\n 4. Отчество\n 5. Номер телефона\n 6. Отдел\n 7. Должность\n 8. Выход\n Введите номер поля которые хотите вывесте: '))
        if (temp == 8):
            print('\n')
            break
        size.append(temp)
    with open('bd.csv', encoding='utf-8') as data:
        for line in data:
            for i in range(len(size)):
                print(line.split(',')[size[i] -1])