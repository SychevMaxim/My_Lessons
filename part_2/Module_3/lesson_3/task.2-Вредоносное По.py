count_first_mark = 0
count_second_mark = 0
first_massage = input("Введите первое сообщение: ")
last_first_massage = ''
second_massage = input("Введите второе сообщение ")
last_second_massage = ''
for first_mark in first_massage:
	if first_mark == '!' or first_mark == '?':
		count_first_mark += 1
for second_mark in second_massage:
	if second_mark == '!' or second_mark == '?':
		count_second_mark += 1
first_massage = list(first_massage)
second_massage = list(second_massage)
if first_massage > second_massage:
	first_massage.extend(second_massage)
	for num in first_massage:
		last_first_massage += num
	print(last_first_massage)
elif first_massage < second_massage:
	second_massage.extend(first_massage)
	for num in second_massage:
		last_second_massage += num
	print(last_second_massage)
else:
	print("Ой")