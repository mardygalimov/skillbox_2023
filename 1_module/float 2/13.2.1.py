# Пользователь вводит число N. Напишите функцию summa_n, которая принимает одно целое положительное число N и находит сумму всех чисел от 1 до N включительно. Функция вызывается два раза: сначала от числа N, а затем от полученной суммы.
#
# Пример работы программы:
#
# Введите число: 5
# Сумма от 1 до 5 = 15
# Сумма от 1 до 15 = 120

def summ_n(number):
    summ = 0
    for i in range(number+1):
        summ += i
    return summ


number = int(input("Введите число: "))
summ = summ_n(number)
if number > 0:
    print(f"Сумма от 1 до {number} =", summ)
    print(f"Сумма от 1 до {summ} =", summ_n(summ))
else:
    print("Введите положительное число")
