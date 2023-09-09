number = int(input('Первый член прогрессии для IP: '))
step = int(input('Введите шаг для подсчета чисел: '))
summ = 0
for count in range(3):
    print(number, end='.')
    summ += number
    number += step
print(summ)
