num = int(input('Введите целое число: '))
num_lst = []
for current_num in range(1,6):
	num_lst.append(current_num)
num = {}
for degree in num_lst:
	num[degree] = degree * degree
print(f'Результат: {num}')