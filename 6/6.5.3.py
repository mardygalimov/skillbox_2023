count = int(input('Сколько мешков наловили?: '))
total_waight = 0
waight = 0
num = 0
while num < count:
    waight = int(input('Введите вес мешка: '))
    total_waight += waight
    num += 1
print('Суммарны вес всех мешков: ', total_waight)