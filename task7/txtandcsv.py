from person import info_human as lg
info = lg()

def csv_fail ():
    file = 'Person.csv'
    with open (file, 'a+', encoding = 'utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def txt_fail ():
    file = 'Person.txt'
    with open (file, 'a+', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')