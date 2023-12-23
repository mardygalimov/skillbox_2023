weather = int(input('Введите температуру: '))
meter = 0
while weather > 15:
    meter += 20
    weather -= 2
    if weather <= 15:
        break
    meter += 10
print('Пройдено шагов: ', meter)