#Напишите функцию, вычисляющую наибольший общий делитель двух чисел.
def mygcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
#        a, b = b, a % b
    print("НОД", a + b)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

mygcd(a, b)