name = input('Введите ваше имя: ')
balance = int(input('Введите сумму долга: '))
print(name, 'ваша задолженность составляет', balance)
debt = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
while balance > debt:
    print('Маловато, Василий. Давайте ещё раз.')
    debt = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
print('Отлично, Василий! Вы погасили долг. Спасибо!')