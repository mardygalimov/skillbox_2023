# Вариант когда статично задается значение выбора компьютера
# Вский варианты с модулем random не использовался так как в курсе еще не проходили
def rock_paper_scissors():
    comp = 'бумага'
    user = input('Введите камень, ножницы или бумага: ')
    if user == 'камень' and comp == 'ножницы':
        print(f'Компютер выбрал: {comp}')
        print('Вы победили')
    elif user == 'камень' and comp == 'бумага':
        print(f'Компютер выбрал: {comp}')
        print('Вы проиграли')
    elif user == 'ножницы' and comp == 'камень':
        print(f'Компютер выбрал: {comp}')
        print('Вы проиграли')
    elif user == 'ножницы' and comp == 'бумага':
        print(f'Компютер выбрал: {comp}')
        print('Вы выйграли')
    elif user == 'бумага' and comp == 'ножницы':
        print(f'Компютер выбрал: {comp}')
        print('Вы проиграли')
    elif user == 'бумага' and comp == 'камень':
        print(f'Компютер выбрал: {comp}')
        print('Вы выйрали')
    else:
        print(f'Компютер выбрал: {comp}')
        print('Ничья')


def guess_the_number():
    while True:
        comp = 5
        user = int(input('Введите число от 1 до 10:  '))
        if comp != user:
            print(f'Компютер загадал число: {comp}')
            print('Вы не отгадали, попробуйте еще раз:')
            print()
        else:
            print(f'Компютер загадал число: {comp}')
            print('Вы отгадали. Молодец.')
            print('Игра завершена.')
            break


def mainMenu():
    a = int(
        input('Выберите игру:\n 1) Камень.Ножницы.Бумага.\n 2) Угадай число.\n Ваш выбор: '))
    if a == 1:
        print()
        rock_paper_scissors()
    elif a == 2:
        print()
        guess_the_number()
    else:
        print('Неправильный выбор. Выберите игру.')


mainMenu()