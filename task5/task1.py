# Напишите программу, удаляющую из текста все слова, содержащие "абв".
search1_text = 'а'
search2_text = 'б'
search3_text = 'в'
text = input("Введите текст:")
list1 = [i for i in text.split() if (search1_text and search2_text and search3_text) not in i]
print(list1)
