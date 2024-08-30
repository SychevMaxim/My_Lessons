goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print("Текущий ассортимент:", goods)
counter = 0
new_fruct = [input("Введите фрукт: ")]
pay = int(input("Цена: "))
new_fruct.append(pay)
goods.append(new_fruct)
print('список с новым фруктом',goods)
for _ in range(len(goods)):
	goods[counter][1] += int(goods[counter][1] / 100 * 8)
	counter += 1
print('список с новыми фруктами и новыми ценами:', goods)