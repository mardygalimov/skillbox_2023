winners = 0
for number in (345,19,87,1020,421):
    if (1 <= (number/100) <= 9) and ((number % 5) == 0):
        print(number, " - Выигрышный билет!")
        winners += 1
print('Выигрышных билетов: ', winners)