def largest_number(count_task):
	largest_number = 0
	for x in range(count_task):
		number = int(input("Введите число"))
		if number > largest_number:
			largest_number = number
	return largest_number
count_task = int(input("Введите количество задач: "))
largest_number = largest_number(count_task)
print("Первая задача на обработку:", largest_number)