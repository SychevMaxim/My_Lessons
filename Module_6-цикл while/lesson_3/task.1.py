print('\nЗадача task.1. .\n')

# РЕШЕНИЕ
# Представим, что у нас далёкое будущее и мы можем заниматься спортом на планетах со странными перепадами температур.
# Спортсмен бегает по стадиону до тех пор, пока температура на улице больше 15 градусов.
# Он пробегает 20 метров, затем температура падает на два градуса,
# и, если уже в этот момент она стала меньше либо равна 15 градусам, спорт сразу заканчивается.
# Если же всё в порядке, то он проходит пешком ещё 10 метров. Затем всё это повторяется.

# Напишите программу, которая спрашивает у пользователя, сколько на улице градусов, и, исходя из (погоды,
# считает) количество
# пройденных по стадиону метров и выводит ответ на экран.
# =============================





# region {===== Основной код =====}

temperatur = int(input("Сколько градусов на улице? "))
meter = 0

while temperatur != 15:

	print("пробежал  20 метров")
	meter += 20

	if temperatur <= 15:
		break

	temperatur -= 2
	meter += 10

	print("прошел  10 метров")
	print("Текущее расстояние:", meter)

print(meter)

# endregion {===== Основной код =====}