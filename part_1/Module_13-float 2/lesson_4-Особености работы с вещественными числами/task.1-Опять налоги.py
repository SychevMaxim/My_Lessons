totalTax = float(input("Введите бюджет страны"))
newTax = float(input("новое поступление (налог): "))
numbers = ""
for we in str(totalTax):
	if we != "e" or we != "е":
		numbers += we
if newTax > float(numbers):
	print("Бюджет увеличен")
else:
	print("Бюджет не изменился")