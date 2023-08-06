count = 10
check = 0
while count != 0:
    num = int(input('Введите число: '))
    count -= 1
    if (num > 0) and (num%2 == 0):
        check += 1
print(check, 'чисел ялвется положительными и четными')