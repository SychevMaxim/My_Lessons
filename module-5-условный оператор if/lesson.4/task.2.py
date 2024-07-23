score = int(input("Сколько балло набрал? "))
coin = int(input('Есть медаль? '))
if score >= 280 and coin > 0:
	print("Поздравляю! ты поступил!")
else:
	print("к сожелению, ты не прошел в наш университет")