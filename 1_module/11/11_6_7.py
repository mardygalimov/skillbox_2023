# Вы встретились со старым другом, который тоже изучает программирование,
# но в другом учебном заведении. За чашкой кофе он пожаловался, что их сумасбродный
# препод дал задание написать программу, которая из двух введённых чисел определяет наибольшее,
# не используя при этом условные операторы, циклы и встроенные функции вроде max/min/sorted.
# Радуясь, что на вашем курсе такого не требуют, вы всё-таки решаете помочь другу.
# Напишите для него программу.
#
# Пример:
#
# Введите первое число: 10
#
# Введите второе число: 5
#
# Наибольшее число: 10
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = round(((a + b) - abs(a - b)) / 2)
d = a + b - c
print(d)