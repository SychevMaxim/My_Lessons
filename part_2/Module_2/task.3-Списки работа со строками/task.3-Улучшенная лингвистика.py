first_word = input("Введите 1 слово")
count_first_word = 0
second_word = input("Введите 2 слово")
count_second_word = 0
three_word = input("Введите 3 слово")
count_three_word = 0
word = ""
while word != "end":
	word = input("Слово из текста: ")
	if word == first_word:
		count_first_word += 1
	elif word == second_word:
		count_second_word += 1
	elif word == three_word:
		count_three_word += 1
	elif word == "end":
		break
print(first_word + ":", count_first_word)
print(second_word + ":", count_second_word)
print(three_word + ":", count_three_word)