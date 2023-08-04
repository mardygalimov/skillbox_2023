order = int(input('Введите сумму счета: '))
proc = int(input('Введите процент по вкладу: '))
total = int(input('Введите размер вклада для снятия: '))
years = 0
while order < total:
    order += int((order * proc )/100)
    print(order)
    years += 1
print(years)