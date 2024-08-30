count_people = int(input("Введите количество участников: "))
Count_peopleinGroup = int(input("Кол-во человек в группе: "))
Count_People = Count_peopleinGroup
member = []
count = 1
if count_people % Count_peopleinGroup == 0:
	for _ in range(Count_peopleinGroup - 1):
		member.append(list(range(count, Count_peopleinGroup + 1)))
		count += Count_People
		Count_peopleinGroup += Count_People

	print(member)
else:
	print("Невозможно поделить")