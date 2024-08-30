import random
a = int(input('Введите левую границу'))
b = int(input('Введите правую границу'))
c = []
c.append([x for x in range(a, b + 1) if x % 2 == 0])
print(c)