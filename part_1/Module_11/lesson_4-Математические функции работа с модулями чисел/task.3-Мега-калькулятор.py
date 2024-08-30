import math
count_number = 1
numbers = float(input("Введите число"))
while True:
	if count_number == 1:

		print(int(numbers))
		count_number += 1

	elif count_number == 2:

		print(round(numbers))
		count_number += 1

	elif count_number == 3:

		print(numbers % 10)
		count_number += 1

	elif count_number == 4:

		print(math.sqrt(numbers))
		count_number += 1

	elif count_number == 5:

		print(numbers ** numbers)
		count_number += 1

	elif count_number == 6:

		print(math.log(numbers))
		count_number += 1

	elif count_number == 7:

		print(math.log2(numbers))
		count_number += 1

	elif count_number == 8:

		print(math.log10(numbers))
		count_number += 1

	elif count_number == 9:

		print(math.sin(numbers), math.cos(numbers))

		count_number += 1
		break