coins = int(input('Сколько баллов набрал?'))
gold_medal = int(input('Есть медаль?'))
if coins > 280 and gold_medal == 1:
    print('Поздравляем! Ты посутпил!')
else:
    print('К сожалению, ты не прошел в наш университет.')