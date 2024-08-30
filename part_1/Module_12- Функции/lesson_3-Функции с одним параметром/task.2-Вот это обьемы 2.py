R = float(input("Введите радиус планеты: "))
def sphere_area():
	S = 4 * 3.14 * R ** 2
	print("Площадь планеты:", S)
	print()
def sphereVolume():
	V = 4/3 * 3.14 * R ** 3
	print("Объем планеты:", V)
	print()
sphere_area()
sphereVolume()