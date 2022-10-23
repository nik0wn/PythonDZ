# Вычислить число c заданной точностью d
def Number():
    try:
        x = abs(int(input('Введите целоое число от 1 до 10: ')))

    except:
        print('Целое число введено неверно')
        return Number
numberN = Number()
while not (1 <= numberN <= 10):
    numberN = Number()
d = 10 ** (-numberN)
Pi = 0
x = 1
sign = 1
while True:
    a = 4/x
    Pi += sign * a
    if a < d:
        break
    sign = -sign
    x += 2