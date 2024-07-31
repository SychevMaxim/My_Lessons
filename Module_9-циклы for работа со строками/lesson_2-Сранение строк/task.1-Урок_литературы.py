count_two = 0
for number in range(1, 5 + 1, 1):
	answer = input("Кто написал произведение Евгений Онегин")
	if answer == "Пушкин" or answer == "пушкин":
		print("Угадал")
		break
	else:
		print("Неправильно, Два!")
		count_two += 1
print("Количество двоек:", count_two)
