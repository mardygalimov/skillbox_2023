count = int(input('Сколько мешков наловили?: '))
total_weight = 0
weight = 0
num = 0
while num < count:
    weight = int(input('Введите вес мешка: '))
    total_weight += weight
    num += 1
print('Суммарны вес всех мешков: ', total_weight)