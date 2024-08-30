def number_1():

	x1 = int(input("Введите первую точку "))
	y1 = int(input("Введите вторую точку "))

	coordinate = abs(y1 - x1)

	print("Расстояние до точки:", coordinate)

def number_2():

	x1 = int(input("Введите x первой точки "))
	y1 = int(input("Введите y первой точки "))

	x2 = int(input("Введите x второй точки "))
	y2 = int(input("Введите y второй точки "))

	coordinate = (x2 - x1), (y2 - y1)

	print("Расстояние до точки:", coordinate)

answer = int(input("1 - расстояние от себя до точки, 2 - расстояние от точки до точки"))

if answer == 1:
	number_1()

elif answer == 2:
	number_2()

else:
	print("Ошибка ввода")