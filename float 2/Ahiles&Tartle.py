#e = 1/0! + 1/1! + 1/2! + 1/3!

import math

precision = float(input('Точность: '))
result = 0
i = 0
addMember = 1

while addMember > precision:
    addMember = 1 / math.factorial(i)
    result += addMember
    i += 1

print('Результат: ', result)
print('Константа: ', math.e)