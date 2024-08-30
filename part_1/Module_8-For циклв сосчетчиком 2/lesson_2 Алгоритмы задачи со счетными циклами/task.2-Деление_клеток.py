count_cell = 1
TotalHours = int(input("Сколько времени будет длиться наблюдение ? "))
hours = 0
for num in range(1, TotalHours // 3 + 1):
	print("Количество часов:", TotalHours)
	hours += 1 * 3
	print("Прошло часов: ", hours)
	print("количество клеток: ", count_cell)
	count_cell *= 2
	print("Осталось часов: ", TotalHours - hours)