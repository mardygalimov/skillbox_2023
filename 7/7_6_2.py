total_pay = 0
pay = 0
for month in range(1,13):
    print(month, '-й месяц')
    pay = int(input('Введите зарплату за месяц: '))
    total_pay += pay
print('Средняя зарплата за год: ', total_pay/12)