def eqw():
	a = float(input("Введите первое число"))
	b = float(input("Введите второе число"))
	c = float(input("Введите третье число"))
	if c - (a+b) < 1e-15:
		print("True")
	else:
		print("False")
eqw()