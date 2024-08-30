N = list(input('Введите список'))
a = int(input("Введите левую границу"))
b = int(input('Введите правую границу'))
lst = ''
lst += str(N[:a])
lst += str(N[b::])
print(lst)