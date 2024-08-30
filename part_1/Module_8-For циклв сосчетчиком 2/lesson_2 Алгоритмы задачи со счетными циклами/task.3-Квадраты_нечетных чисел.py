n = int(input("Введите число"))
count = 1
for number in range(1, n // 2 + 1):
	print(count, "** 3 =", count ** 3)
	count += 2
