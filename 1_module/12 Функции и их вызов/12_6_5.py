# Продолжаем разрабатывать новый текстовый редактор.
# В этот раз нам поручили написать для него код, который считает,
# сколько раз в тексте встречается любая выбранная буква или цифра
# (а не только буквы Ы, как раньше).
#
# Напишите функцию count_letters(), которая принимает на вход текст и
# подсчитывает, какое в нём количество цифр K и букв N.
# Функция должна вывести на экран информацию о найденных буквах и
# цифрах в определённом формате.
#
# Пример:
#
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? Л
#
# Количество цифр 0: 2
# Количество букв Л: 1
symbol = ''
digs = ''


def count_letters(text, symbol):
    count = 0
    for char in text:
        if char == symbol:
            count += 1
    print(f"Количество букв {symbol}", count)


def count_digs(text, digs):
    count_digs = 0
    for char in text:
        if char == digs:
            count_digs += 1
    print(f"Количество букв {digs}", count_digs)


text = input("Введите текст: ")
symbol = input("Какую букву ищем: ")
digs = input("Какую цифру ищем: ")
count_letters(text, symbol)
count_digs(text, digs)