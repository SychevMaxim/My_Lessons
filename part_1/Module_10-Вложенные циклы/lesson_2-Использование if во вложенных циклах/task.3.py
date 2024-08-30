for col in range (20):
	for row in range (50):
		if col == 9:
			print("-", end=" ")
		elif row == 24:
			print("|", end=" ")
		else:
			print(" ", end=" ")
	print()