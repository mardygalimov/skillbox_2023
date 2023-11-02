import math

def sphereArea(radius):
    print(4 * math.pi * radius ** 2)

def sphereVolume(radius):
    print(4 / 3 * math.pi * radius ** 3)


radius_of_planet = float(input("Введите радиус планеты: "))
sphereArea(radius_of_planet)
sphereVolume(radius_of_planet)
