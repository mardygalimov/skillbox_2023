p1 = int(input('Введите первое число:'))
p2 = int(input('Введите второе число:'))
p3 = int(input('Введите третье число:'))
if (p1 >= p2 and p1 >= p3):
    print('Максимальное число:', p1)
elif (p2 >= p3 and p2 >= p1):
    print('Максимальное число:', p2)
elif (p3 >= p2 and p3 >= p1):
    print('Максимальное число:', p3)