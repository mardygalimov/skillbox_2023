girls = int(input('Введите количество девочек: '))
boys = int(input('Введите количество мальчиков: '))
buff = ''
if (boys > 2 * girls) or (girls > 2 * boys):
    print('Нет решения.')
# мальчиков больше
elif boys >= girls:
    over = boys - girls
    for bgb in range(over):
        buff += 'BGB'
    for bg in range(girls - over):
        buff += 'BG'
# девочек больше
else:
    over = girls - boys
    for gbg in range(over):
        buff += 'GBG'
    for gb in range(boys - over):
        buff += 'GB'
print(buff)

