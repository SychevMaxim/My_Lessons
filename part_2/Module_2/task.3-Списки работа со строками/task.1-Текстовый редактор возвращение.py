text = input("Введите текст")
symbol = input("Введите символ который хотите заменить")
new_sym = input("на какой? ")
new_text = []
text = list(text)
a = ""
count = 0
for num in text:
	if num == symbol:
		new_text.append(new_sym)
		count += 1
	else:
		new_text.append(num)
for full_text in new_text:
	a += full_text
print("Исправленная строка: ", a)
print("Кол-во замен: ", count)