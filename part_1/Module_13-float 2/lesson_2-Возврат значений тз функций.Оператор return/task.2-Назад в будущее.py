import math
def Gcd(a, b):
	Nod = math.gcd(a, b)
	return  Nod

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
Nod = Gcd(a, b)
print("НОД =", Nod)