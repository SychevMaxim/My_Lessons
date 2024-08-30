original_prices = [-12, 3, 5, -2, 1]
nums = 0

new_prices = original_prices

for i in range(len(original_prices)):
	if new_prices[i] < 0:
		nums += new_prices[i]
		new_prices[i] = 0

print("Мы потеряли: ", nums)