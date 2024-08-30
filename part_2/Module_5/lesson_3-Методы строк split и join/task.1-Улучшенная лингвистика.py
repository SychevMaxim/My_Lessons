words = input('Введите слова: ').split()
lst = input('Введите строку: ').split()
counter = 0
for current_word in lst:
	for current_letter in words:
		if current_word == current_letter:
			counter += 1
print('количество использований слов:', counter)