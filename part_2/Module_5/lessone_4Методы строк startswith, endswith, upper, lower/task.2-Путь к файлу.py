road_file = input('Путь к файлу: ').lower()
disk = input('На каком диске должен лежать файл: ').lower()
expansion = input('Введите требуемое расширение: ').lower()
if road_file.startswith(disk) and road_file.endswith(expansion):
	print('Путь корректен')
else:
	print('Путь не корректен')