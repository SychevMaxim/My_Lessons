counter = 0
punction = {".", ";", ":", "!", "?"}
text = input('Введите текст: ')
for letter in text:
	if letter in punction:
		counter += 1
print(f'Количество знаков пунктуации: {counter}')