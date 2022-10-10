from math import sqrt


a1 = float(input())
a2 = float(input())
b1 = float(input())
b2 = float(input())
ab = sqrt((b1 - a1) ** 2 + (b2 - a2) ** 2)
print(round(ab,2))
