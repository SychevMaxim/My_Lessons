n = int(input("Сколько чисел будет"))
numeral = int(input("какую цифру считать"))
count_num = 0
while numeral < 0 or numeral > 9:
	numeral = int(input("Цифра должна быть в диапазоне от 0 до 9! Введите новую цифру"))

for num in range(n):
	number = int(input("Введите число:"))
	while number > 0:
		if number % 10 == numeral:
			count_num += 1
		number //= 10
print("Цифер", numeral, "В последовательности:", count_num)