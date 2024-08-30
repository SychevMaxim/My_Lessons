letter = 0
bigLetter = 0
text = input("Введите текст")
for symbal in text:
	if symbal == "ы":
		letter += 1
	elif symbal == "Ы":
		bigLetter += 1
	print(text)
print("Количество ы =", letter)
print("Количество Ы =", bigLetter)