count_people = int(input("Введите количество сотрудников"))
count_not0people = 0
PAY = []
for current_people in range(1, count_people + 1):
	print("введите зарплату", current_people, "сотрудника", end=" ")
	people = int(input())
	if people > 0:
		count_not0people += 1
		PAY.append(people)
print(count_not0people)
print(PAY)