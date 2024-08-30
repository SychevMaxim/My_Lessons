nums_list = []
zero = False
N = int(input('Кол-во чисел в списке: '))

for cums in range(1, N + 1):
	num = int(input('Очередное число: '))
	nums_list.append(num)
	if num > 0:
		zero = True
if zero == True:
	maximum = 1

	minimum = 1
else:
	maximum = -100000000
	minimum = 0
for i in nums_list:

	if maximum <= i:
		maximum = i

	if minimum >= i:
		minimum = i

print('Максимальное число в списке:', maximum)

print('Минимальное число в списке:', minimum)