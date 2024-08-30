a = int(input("Введите начальную точку"))
b = int(input("введите второе число"))
def number():
	count_number = 0
	summ = 0
	count = 0
	while count_number != b + 1:
		if count_number >= a and count_number <= b:
			count += 1
			summ += count_number
			count_number += 1


		else:
			count_number += 1
	print(summ / count)
number()

