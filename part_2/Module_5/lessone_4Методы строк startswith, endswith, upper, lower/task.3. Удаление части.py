counter_upper = 0
counter_lower = 0
text = input('Введите строку: ')
for letter in text:
	if letter.isupper():
		counter_upper += 1
	else:
		counter_lower += 1
if counter_upper < counter_lower:
	print(text.lower())
else:
	print(text.upper())