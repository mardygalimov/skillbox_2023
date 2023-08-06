N = int(input('Введите колчиество учеников на уроке: '))
count_3 = 0
count_4 = 0
count_5 = 0
ocenka = 0
for bla in range(1,N+1):
    ocenka = int(input('Введите оценку для ученика:'))
    if ocenka == 3:
        count_3 += 1
    elif ocenka == 4:
        count_4 += 1
    elif ocenka == 5:
        count_5 += 1
print('троек', count_3)
print('четверок', count_4)
print('пятерок', count_5)
if count_3 < count_5 > count_4:
    print('Отличиников больше')
elif count_3 < count_4 > count_5:
    print('Хорошистов больше')
else:
    print('Троечников больше')
