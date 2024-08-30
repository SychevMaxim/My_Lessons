print('\nЗадача task.2. .\n')

# РЕШЕНИЕ
# Напишите программу, где пользователь вводит любые два целых положительных числа.
# А программа суммирует все числа в
# диапазоне от первого до второго. Гарантируется, что первое введённое число всегда меньше второго.
# =============================



# region {===== Основной код =====}

first_number = int(input("Введите первое число: "))

end_first_number = first_number

second_number = int(input("Введите второе число: "))
summ = 0

for sum_number in range(first_number, second_number ):

	first_number = first_number + 1
	summ += first_number

print(summ + end_first_number)

# endregion {===== Основной код =====}