import math

rasst = float(input("Введите пройденное расстояние: "))
angle = float(input("Введите угол: "))
angle /= 57.2958

x = rasst * math.cos(angle)
y = rasst * math.sin(angle)
print("Координаты: ", x, y)