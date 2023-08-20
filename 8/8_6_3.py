reverse_timer = int(input('Введите время разогревы еды: '))
for time in range(reverse_timer, 0, -1):
    print(time)
    ansver = int(input('Вы готовы остановить разгрев и забрать еду, да - 1, нет - 0? '))
    if ansver == 1:
        print('Разогрев прерван на ', reverse_timer - time, 'минуте!')
        break
print('Ваша еда готова, осторожно горячo!')