profit = int(input('Введите ваш доход:'))
if profit < 10000:
    print('Налог составит (13%): ', profit / 100 * 13)
elif profit > 50000:
    print('Налог составит (30%): ', profit / 100 * 30)
elif profit < 0:
    print('Ошибка: доход не может быть отрицательным')
else:
    print('Налог составит (20%): ', profit / 100 * 20)