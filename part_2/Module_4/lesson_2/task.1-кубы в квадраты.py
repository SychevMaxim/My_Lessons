left = int(input("Введите левую границу: "))
right = int(input("Введите правую границу: "))
left_lst = [x ** 3 for x in range(left, right + 1)]
right_lst = [a ** 2 for a in range(left, right + 1)]
print(f'\nСписок кубов чисел в диапазоне от {left} до {right}: {left_lst}')
print(f'Список кубов чисел в диапазоне от {left} '
  f'до {right}: {right_lst}')