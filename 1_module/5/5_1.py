skill = int(input('Введите количество опыта:'))
if (skill >= 1000) and (skill < 2500):
    print('Ваш уровень 2')
elif (skill >= 2500) and (skill < 5000):
    print('Ваш уровень 3')
elif skill >= 5000:
    print('Ваш уровень 4')
else:
    print('Ваш уровень 1')