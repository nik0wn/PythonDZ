# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
text = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
p = ''
for i in text:
    if i not in p:
        print(f"{text.count(i)}{i}",end= '')
        p += i