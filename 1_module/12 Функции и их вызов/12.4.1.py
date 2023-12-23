import math

def mean_calc(x, y):

    # Без цикла

    print("Среднее:", round((x + y) / 2, 2))


a = int(input("Введите a: "))
b = int(input("Введите b: "))

if a > b:
    a, b = b, a

mean_calc(a, b)
