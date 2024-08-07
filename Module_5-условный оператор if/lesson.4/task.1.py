print('\nЗадача task1. .\n')

# РЕШЕНИЕ
# Напишите программу, которую мы разбирали в рамках теории. Нашему ребёнку нужен новый велосипед. Правда, никто из нас в них не разбирается. Нужно, чтобы велосипед не был устаревшим и скоростей на нём было побольше, а сколько он стоит — пока неважно. Чтобы не искать велосипед на сайте вручную, мы хотим написать программу, которая будет проверять каждый велосипед на нужный нам год выпуска и количество скоростей.
#
# Используя один из логических операторов (and, or), напишите программу из видео, которая запрашивает год выпуска велосипеда и количество скоростей и выводит на экран сообщение о том, подходит этот велик или нет.
#
# Условия, которые надо проверить:
#
# год выпуска — не старше 2018-го;
# количество скоростей — не менее 24.
# =============================





# region {===== Основной код =====}
year_of_release = int(input("Введеите год выпуска велосипеда: "))
speed = int(input(" Введите количество скоростей"))
if year_of_release >= 2018 and speed >= 24:
	print('Велосипед подходит')
else:
	print("Велосипед не подходит")


# endregion {===== Основной код =====}