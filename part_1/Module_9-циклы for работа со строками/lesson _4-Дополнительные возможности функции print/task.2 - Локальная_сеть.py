number = int(input("Введите число"))
step = int(input("Введите шаг"))
summ = 0
print("\n Ip areas:", end=" ")
for symbal in range(3):
	print(number, end=".")
	summ += number
	number += step