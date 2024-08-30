text = int(input('Введите размер'))
for row in range(text):
	for col in range (text):
		if row == col:
			print(text , " ", end="")
		if row > col:
			print(text - 1, " ", end="")
		if col > row:
			print(text + 1, " ", end="")
	print()