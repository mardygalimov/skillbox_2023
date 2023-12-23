import math

v_z = (1.08321 * 10 ** 12)
radius_planet = float(input("Введите радиус случайной планеты: "))
v_planet = (4 * 3.14 * radius_planet ** 3) / 3
if v_z < v_planet:
    print("Объём планеты Земля меньше в (1/", end='')
    print(round(v_z/v_planet,3),end=')')
    print(" =", round(1/(v_z/v_planet),3), "раза")
else:
    print("Объем планеты Земля больше в", round(v_z / v_planet,3), "раза")
