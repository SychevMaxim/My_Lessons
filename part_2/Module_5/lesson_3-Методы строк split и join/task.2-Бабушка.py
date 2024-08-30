lst = input('Введите текст: ').split()
str_list = ''
for letter in lst:
	str_list += letter + ' '
print('Исправленный список:', str_list)