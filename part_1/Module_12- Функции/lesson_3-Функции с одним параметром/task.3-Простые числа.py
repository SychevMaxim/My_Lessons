n = int(input("Введите число: "))

for number in range(2, n):
	if n / number == 0:
		n = True
	elif n / number != 0:
		n = False


if n == True:
	print("Нет, это число не простое!")
elif n == False:
	print("Да, это число простое!")