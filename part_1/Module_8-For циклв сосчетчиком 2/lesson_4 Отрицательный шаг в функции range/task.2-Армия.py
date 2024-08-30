count_soldier = int(input("Введите количество солдатов в шеренге: "))
count_rules = int(input("Введите количество правил в уставе: "))
for number in range(count_soldier, 0, -4):
	print("текущий солдат", number)
	answer = int(input("Сколько правил в воинском уставе? "))
	if answer != count_rules:
		print("Неправильно")
		print(number * 10, "Отжиманий")
	else:
		print("Правильно")