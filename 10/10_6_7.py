n = int(input('Введите высоту треугольника: '))
#n=5
number = 1
for row in range(1, n+1):
    print('\t'*(n-row), end='')
    for col in range(row):
        print(number, end='')
        number +=2
        print('\t' * 2, end='')
    print()
