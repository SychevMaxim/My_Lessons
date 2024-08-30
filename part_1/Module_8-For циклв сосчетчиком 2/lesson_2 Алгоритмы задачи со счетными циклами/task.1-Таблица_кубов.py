n = int(input("Введите число"))
count_integration = 0
for num in range(1, n // 2 + 1):
	num *= 2
	print( num, "** 3 =", num ** 3)