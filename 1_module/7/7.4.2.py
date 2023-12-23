start = int(input('Введите начальное число для диапазона: '))
end = int(input('Введите конечное число для диапазона: '))
total = 0
for num in range(start,end+1):
    total += num
print('Сумма чисел от', start, ' до ', end, ' равна ', total)