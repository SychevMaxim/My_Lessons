temperatur = int(input("Введите температуру в помещении "))
if temperatur < 0 or temperatur > 100:
	print("Внимание опасная температура")
else:
	print("Температура в приделах нормы")