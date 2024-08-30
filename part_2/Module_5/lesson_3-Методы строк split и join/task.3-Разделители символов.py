str_name = input(f'Список людей через запятую:').split(', ')
str_age = input(f'Список возрастов через пробел').split(' ')
birthday = []
for counter in range(len(str_age)):
	print(f'С днём рождения, {str_name[counter]}! С {str_age[counter]}-летием тебя!')
	birthday.append([str_name[counter], str_age[counter]])
print(birthday)