main = input("main: ")
main = list(main)
first_company = input("first_company: ")
first_company = list(first_company)
second_company = input("second_company: ")
second_company = list(second_company)
third_company = input("third_company")
third_company = list(third_company)
main.extend(first_company)
main.extend(second_company)
main.extend(third_company)
bad_pack = 0
for num in main:
	if num == '0':
		bad_pack += 1
print('Общая статистика компаний', main)
print('Количество не выполненных задач:', bad_pack)