hours = int(input('Сколько сейчас часов? '))
if (hours >= 14 and hours < 15) or (hours >= 10 and hours < 12) or (hours >= 18 and hours < 20) or (hours >= 23 and hours < 24) or (hours >= 0 and hours < 8):
    print('Посылку получить нельзя')
else:
    print('Можно получить посылку')