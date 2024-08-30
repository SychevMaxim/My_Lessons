text = list(input('Введите строку: '))
symbal = list(input("Введите символ: "))
last_text = [a * 2 for a in text]
last_symbal = [b * 2 + '!' for b in text]
print(f'Список удвоенных символов:{last_text}')
print(f'Склейка с дополнительным символом:{last_symbal}')
