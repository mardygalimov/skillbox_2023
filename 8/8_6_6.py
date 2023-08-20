educational_grant = int(input('Введите стипендию: '))
pay_month = int(input('Введите расходы на проживание: '))
lacks = 0
for month in range(1, 11, 1):
    lacks += pay_month - educational_grant
    print(month, 'месяц траты', pay_month, 'не хватает', round(lacks, 2))
    gross = pay_month*0.03
#    print(gross)
    pay_month += gross
print('Нужно попросить у родителей: ', round(lacks, 2))