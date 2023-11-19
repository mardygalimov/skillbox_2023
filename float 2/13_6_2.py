# Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать.
# Он захотел написать функцию, которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть. Юра задумался:
# может быть, её можно как-то использовать для нахождения максимума уже от трёх чисел?
#
# Помогите Юре написать программу, которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.
#
# По итогу в программе должны быть реализованы две функции:
#
# maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх);
# при этом она должна использовать для сравнений первую функцию maximum_of_two.
def maximum_of_two(a, b):
    if a > b:
        max1 = a
    else:
        max1 = b
    return max1

def maximum_of_tree(a, b, c):
    max1 = maximum_of_two(a, b)
    if max1 > c:
        max2 = max1
    else:
        max2 = c
    print("Maximum number: ", max2)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
maximum_of_tree(a, b, c)
