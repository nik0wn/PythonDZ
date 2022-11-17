def info_human():
    human = []
    surname = input('Введите Фамилию: ')
    name = input('Введите Имя: ')
    phone_number = ' '
    while True:
        phone_number = input('Введите номер: ')
        if len(phone_number) == 11:
            break
        else:
            print('Номер должен состоять из 11 цифр')
    description = input('Введите описание: ')
    human.append(surname)
    human.append(name)
    human.append(phone_number)
    human.append(description)
    return human
