# Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов, после чего дробная часть копеек
# отбрасывается. Определите, через сколько лет вклад составит не менее Y рублей.
# Напишите программу, которая по данным числам X, Y, P определяет, сколько лет пройдёт,
# прежде чем сумма достигнет значения Y.
order = int(input('Введите сумму счета: '))
proc = int(input('Введите процент по вкладу: '))
total = int(input('Введите размер вклада для снятия: '))
years = 0
while order < total:
    order += int((order * proc )/100)
    years += 1
print(years, 'лет пройдёт, прежде чем сумма достигнет значения ', total)