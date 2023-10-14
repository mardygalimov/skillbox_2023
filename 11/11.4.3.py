# Напишите программу, которая получает от пользователя вещественное число,
# по очереди применяет к нему функции модуля Math и выводит результат:
#
# округляет вниз
# округляет вверх
# берет модуль числа
# извлекает квадратный корень
# возводит экспоненту в степень, равную числу
# считает натуральный логарифм числа
# считает логарифм числа по основанию 2
# считает логарифм числа по основанию 10
# считает синус и косинус числа
# И так как Кеша самый умный в классе, он решил попробовать посчитать факториал числа.
# Для этого ему пришлось придумать и реализовать контроль ввода: факториал вычисляется, только если введенное число было натуральным.

user_number = float(input("Введите число: "))
print(math.floor(user_number))
print(math.ceil(user_number))
print(abs(user_number))
print(math.sqrt(user_number))
print(math.exp(user_number))
print(math.log(user_number))
print(math.log2(user_number))
print(math.log10(user_number))
print(math.sin(user_number), math.cos(user_number))
if user_number % 1 == 0:
    print(math.factorial(int(user_number)))