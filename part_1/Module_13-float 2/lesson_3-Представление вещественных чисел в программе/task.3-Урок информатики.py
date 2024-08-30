n = int(input("введите число"))
count = 0
while n > 10:
	count += 1
	n /= 10
print("Формат плавающей точки x =", n, "* 10 **", count)