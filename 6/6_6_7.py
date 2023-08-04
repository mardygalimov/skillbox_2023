numbs = 7
counts = 0
while True:
    n = int(input('Введите число: '))
    if n < numbs:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
        counts += 1
    elif n > numbs:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
        counts += 1
    else:
        counts += 1
        print('Вы угадали! ', 'Число попыток', counts)
        break