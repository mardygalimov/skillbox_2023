number = int(input('Введите число N: '))
for i in range(number - number % 2, 0, -2):
    print(i)