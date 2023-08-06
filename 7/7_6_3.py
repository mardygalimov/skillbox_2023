n = int(input('Введите числоя для вычисления факториала:'))
fact = 1
for num in range(1,n+1):
    fact = fact*num
print('Факториал числа ', n, ' равен ', fact)
