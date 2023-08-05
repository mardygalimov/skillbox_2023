hours = 8
tickets = 0
summ_tickets = 0
hour = 0
coll = 0
coll_check = False
print('Начался восьмичасовой рабочий день.')
while hours != hour:
    hour += 1
    print(hour, '-й час')
    tickets = int(input('Сколько задач решит Максим?'))
    coll = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет):'))
    summ_tickets += tickets
    if coll == 1:
        coll_check = True
print('Рабочий день закончился. Всего выполнено задач: ', summ_tickets)
if coll_check:
    print('Нужно зайти в магазин.')
