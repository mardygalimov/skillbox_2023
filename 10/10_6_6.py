h = int(input('Введите высоту треугольника: '))
for i in range(1, h+1):
    space = " " * (h -i)
    hash = "#" * (2*i-1)
    print(space+hash)