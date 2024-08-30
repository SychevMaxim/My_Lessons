zoo = []
input_key = ''
while input_key != "end":
	input_key = input("введите животное: ")
	zoo.append(input_key)
	if input_key == "end":
		break
cell_lion = zoo.index('lion')
cell_monkey = zoo.index('monkey')
print("Лев в клетке номер:", cell_lion + 1)
print("Обезьяна в клетке номер:", cell_monkey + 1)