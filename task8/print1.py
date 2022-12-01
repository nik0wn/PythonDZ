def print_fale():
    list1 = []
    with open('bd.csv', encoding = 'utf-8') as data:
        for line in data:
            list1.append(line.replace(',', ''))
    return list1