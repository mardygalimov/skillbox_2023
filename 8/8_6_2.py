# Напишите программу, которая получает данные о количестве должников,
# а затем спрашивает у каждого пятого (начиная с нуля) его долг.
# В конце выводится общая сумма долгов.
count_debtors = int(input('Введите количество должников: '))
total_credit = 0
for debtor in range(0, count_debtors, 5):
    print('Должник с номером: ', debtor)
    credit = int(input('Сколько должны? '))
    total_credit += credit
print('Общая сумма долга: ', total_credit)
