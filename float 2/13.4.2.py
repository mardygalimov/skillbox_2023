def eqv(a,b,c):
    if abs((a + b) - c) <= 1e-15:
        print(True)
    else:
        print(False)

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
eqv(a, b, c)


