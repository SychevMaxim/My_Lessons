wake_up = int(input("Во сколько проснулся: "))
water = 0
sum_kalories = 0
for hours in range(wake_up, 23, 3):
	water += 1
	print("Сейчас", hours, "часов")
	kalories = int(input("Сколько съел: "))
	sum_kalories += kalories
print("Воды выпито:", water)
print("Калорий съедено", sum_kalories)
