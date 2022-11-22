import delete
import write
import print1
import print2
import edit
import search

while True:
    print("База данных сотрудников.\n")
    print('1. Вывести все записи.\n2. Вывод определенных данных\n3. Добавить запись.\n4. Найти запись.\n5. Изменить запись.\n6. Удалить запись.\n7. Выход.\n')
    value = int(input("Выберите действие: "))
    if value == 1:
        print1.print_fale()
    if value == 2:
        print2.print_fale1()
    elif value == 3:
       write.New_Entry()
    elif value == 4:
        search.Search_Entry('bd.csv')
    elif value == 5:
        edit.Edit_Entry('bd.csv')
    elif value == 6:
        delete.delete_str('bd.csv')
    elif value == 7:
        print('Ждем вас еще :)')
        break
