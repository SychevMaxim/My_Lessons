import random
first_group = [random.randint(50, 80) for _ in range(1, 10)]
second_group = [random.randint(30, 60) for _ in range(1, 10)]
threed_group = ['погиб' if first_group[i_damage] + second_group[i_damage] > 100 else 'Выжил' for i_damage in range(9)]
print('урон первой группы', first_group)
print('урон второй группы', second_group)
print('состояние третей группы', threed_group)