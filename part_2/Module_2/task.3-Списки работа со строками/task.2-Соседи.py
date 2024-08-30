text = input("введите текст")
a = int(input("Введите номер символа"))
text = list(text)
count = 0
print("Символ слева", text[a - 2])
print("Символ справа", text[a])
for num in text:
	if num == text[a - 1]:
		count += 1
print("Есть ровно:", count - 1, "такой же символ")