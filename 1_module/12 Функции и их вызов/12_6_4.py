# Вводится последовательность чисел, оканчивающаяся нулём.
# Реализуйте функцию, которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.
def n_revers():
    revers_n = ''
    for i in n:
        revers_n = i + revers_n
    print('Число наоборот будет: ', revers_n)


while True:
    n = input('Введите число: ')
    if n != '0':
        n_revers()
    else:
        print('Введите корректное число')