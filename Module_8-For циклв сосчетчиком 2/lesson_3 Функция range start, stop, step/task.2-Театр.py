n = int(input("ведите количесто стульев: "))
sum_chair = 0
for chair in range(1, n + 1, 5):
	print('Номер стула: ', chair)
	sum_chair += chair
print(sum_chair)