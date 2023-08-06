#Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Напишите программу, которая поможет найти потерянную карточку, если номера оставшихся известны. Найдите её, зная номера оставшихся карточек.
#Введите число карточек — N.
#Затем введите N − 1 номера оставшихся карточек. Они могут быть введены в любом порядке.
all_cards = int(input('Введите число карточек: '))
all_summ = 0
count = 0
no_lost_summ = 0
lost_num = 0
for card in range(1,all_cards+1):
    all_summ += card
    count += 1
    if count < all_cards:
        no_lost_card = int(input('Введите номер оставшейся карточки:'))
        no_lost_summ += no_lost_card
    else:
        lost_num = all_summ - no_lost_summ
        break
print('Номер пропавшей карточки:', lost_num)

