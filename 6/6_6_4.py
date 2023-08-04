count_pol = 0
count_otr = 0
while True:
    num = int(input('Введите число: '))
    if num > 0:
        count_pol += 1
    elif num < 0:
        count_otr += 1
    else:
        break
print('Кол-во положительных чисел: ', count_pol)
print('Кол-во отрицательных чисел: ', count_otr)
