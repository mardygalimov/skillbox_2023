# Дано положительное действительное число X.
# Выведите его первую цифру после десятичной точки.
# При решении этой задачи нельзя пользоваться условной инструкцией,
# циклом или строками.
import math
x = 1.364
x = round(x,2)
z = math.floor(x)
w = int((x - z) * 10)
print(w)