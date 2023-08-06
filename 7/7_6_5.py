a = int(input('Введите числоа a: '))
b = int(input('Введите числоа b: '))
summ = 0
buff = 0
count = 0
for num in range(a,b+1):
    if num % 3 == 0:
        summ += num
        count += 1
print('Среднее арифметическое всех чисет отрезка от', a, ' до ', b, ' равна ', (summ/count))
