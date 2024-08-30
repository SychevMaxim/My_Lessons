def count_letter(sym_list):
	sym_dict = dict()
	for letter in sym_list:
		if letter in sym_dict:
			sym_dict[letter] += 1
		else:
			sym_dict[letter] = 1
	return sym_dict
text = input('введите текст: ').lower()
hist = count_letter(text)

for i_sym in sorted(hist.keys()):
	print(f'{i_sym}: {hist[i_sym]}')