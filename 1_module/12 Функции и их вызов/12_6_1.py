# Напишите функцию summa_n, которая принимает одно целое положительное
# число N и выводит сумму всех чисел от 1 до N включительно.
#
# Пример работы программы:
#
# Введите число: 5
#
# Я знаю, что сумма чисел от 1 до 5 равна 15

sum_all = 0


def summa_n(n):
    sum_all = (n * (n + 1) // 2)
    print("Я знаю, что сумма чисел от 1 до 5 равна ", sum_all)


n = int(input("Введите число: "))
summa_n(n)

