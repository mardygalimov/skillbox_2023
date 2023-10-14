import math
count = int(input("Введите кол-во чисел: "))

for i in range(count):
    number = float(input("Введите число: "))
    if number > 0:
        x = math.ceil(number)
        print("x=", x, end=' ')
        print("log(x)=", math.log(x), end='')
    else:
        x = math.floor(number)
        print("x= ", x, end=' ')
        print("exp(x)= ", math.exp(x), end='')
    print()