count_id = int(input("Введите количество сотрудников"))
intut = []
current_id = 0
TrueOrFalse = False
for num in range(count_id):
	current_id = int(input("ID: "))
	intut.append(current_id)
secret_id = int(input("какой ID ищем? "))
for number in intut:
	if number == secret_id:
		TrueOrFalse = True
if TrueOrFalse == True:
	print("Сотрудник работает!")
else:
	print("Сотрудник не работает!")