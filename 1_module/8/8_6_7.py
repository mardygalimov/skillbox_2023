n = int(input('Введите N: '))
summ = 0
elem = 0
for i in range(0, n, 1):
    elem = (-1)**i*(1/2)**i
    summ += elem
print('Ответ: ', summ)