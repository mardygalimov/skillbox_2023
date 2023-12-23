# Вася выложил своё новое приложение на платформу для начинающих разработчиков,
# на ней пользователи могут ставить оценку приложению:
# от −100 до 100. Ему захотелось сравнить количество положительных и отрицательных отзывов,
# для этого он заранее отфильтровал все отзывы так, чтобы в конце были те, которые равны нулю.
# Напишите программу, которая находит количество положительных и количество отрицательных чисел в последовательности.
# Последовательность заканчивается на числе 0.
count_pol = 0
count_otr = 0
while True:
    num = int(input('Введите число: '))
    if num > 0:
        count_pol += 1
    elif num < 0:
        count_otr += 1
    else:
        break
print('Кол-во положительных чисел: ', count_pol)
print('Кол-во отрицательных чисел: ', count_otr)