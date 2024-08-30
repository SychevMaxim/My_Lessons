def get_higher_price(percent, price):
	return round(price * (1 * percent / 100), 2)

price_now = []

for _ in range(5):

	a = float(input(f'введите цену на товар:'))
	price_now.append(a)

first_percent = int(input(f'Повышение цен на первый год: '))

second_percent = int(input(f'Повышение цен на второй год: '))

price_first = [get_higher_price(first_percent, i_price) for i_price in price_now]

price_second = [get_higher_price(second_percent, i_price) for i_price in price_now]

print(sum(price_now), sum(price_now + price_first), sum(price_now + price_first + price_second))