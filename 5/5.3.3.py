m1 = int(input('Введите вес 1 монеты в г:'))
m2 = int(input('Введите вес 2 монеты в г:'))
m3 = int(input('Введите вес 3 монеты в г:'))
if m1 > m2:
    print('Вторая монета фальшивая')
elif m2 > m1:
    print('Первая монета фальшивая')
else:
    print('Третья монета фальшивая')