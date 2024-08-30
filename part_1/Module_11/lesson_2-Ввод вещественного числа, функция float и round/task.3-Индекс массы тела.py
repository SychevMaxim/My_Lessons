height = float(input("Введите рост: "))
width = float(input("Введите вес: "))
imt = round(height / width, 2)

if imt <= 18:
	print("Недостаток веса")

elif imt <= 21:
	print("норма")

elif imt <= 30:
	print("переизбыток веса")

else:
	print("Ожирение")