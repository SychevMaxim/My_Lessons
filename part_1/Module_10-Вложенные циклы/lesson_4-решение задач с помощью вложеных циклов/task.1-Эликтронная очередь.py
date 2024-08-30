people = int(input('Введите количество людей'))
for hour in range (people + 1):
	print("Идет час:  ", hour)
	for num in range(hour,people + 1):
		print("Номер в очереди: ", num)
	print()
print("Вся очередь обслужена")
