hours = int(input('Сколько сейчас часов? '))
if (hours >= 8 and hours < 10) or (hours >= 12 and hours < 14) or (hours >= 15 and hours < 18) or (hours >= 20 and hours < 22):
    print('Можно получить посылку')
else:
    print('Посылку получить нельзя')