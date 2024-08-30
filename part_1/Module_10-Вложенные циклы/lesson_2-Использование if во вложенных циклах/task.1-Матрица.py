print('\nЗадача task.3-Матрица. .\n')

# РЕШЕНИЕ
#
# =============================





# region {===== Основной код =====}

text = 5

for row in range (1, text + 1, 1):

	for col in  range(1, text +1, 1):
		if row % 2 == 0:

			print(row * text, end=" ")

		elif row % 2 != 0:
			print(col, end=" ")

		print()

# endregion {===== Основной код =====}