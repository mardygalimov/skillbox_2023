summ = int(input('Введите стартовую сумму:'))
while summ < 10000:
    num = int(input('Сколько выпало на кубике:'))
    if num != 3:
        summ += 500
        print('Вы выиграли 500 рублей!')
    else:
        print('Вы проиграли всё!')
        summ = 0
        break
print('Игра закончена.')
print('Итого осталось :', summ,' рублей')