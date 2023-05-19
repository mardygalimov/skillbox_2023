hours = int(input('Введите отработанные часы:'))
credit = int(input('Введите остаток по кредиту:'))
food = int(input('Введите траты на еду:'))
zp = (200 * hours)/(2**3) + hours
#print(zp)
if zp >= (food + credit):
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать больше!')