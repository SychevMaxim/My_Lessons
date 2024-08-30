import math

distance = float(input("Введите расстояние"))
angle = float(input("введите угол в градусах: "))
angle /= 57.2958

x = math.cos(angle) * distance
y = math.sin(angle) * distance

print("Координаты игрока:", x,y)