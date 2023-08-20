#
total_doldiers = int(input('Сколько солдат: '))
total_rules = int(input('Сколько правил в уставе: '))
push_up = 0
total_push_up = 0
for soldier in range(total_doldiers-3, 0, -1):
    print('Солдать с порядкоавым номером: ', soldier)
    rules = int(input('Солдат, сколько правил в уставе?: '))
    if rules != total_rules:
        push_up = soldier * 10
        print('Солдать номер', soldier, 'упал и отжался ', push_up, ' раз')
        total_push_up += push_up
print("Всего отжиманий было: ", total_push_up)
