def print_fale():
    with open('bd.csv', encoding = 'utf-8') as data:
        for line in data:
            print(line.replace(',', ''), '\n')