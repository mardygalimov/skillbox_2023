print('Задача 5. Часы')

# Напишите программу,
# которая получает на вход число n — количество минут, — затем считает,
# 1) сколько это будет в часах
# 2) сколько минут останется
# и выводит на экран эти два результата.
# (В вычислениях вам помогут операции // и %)
m = int(input('Ввудите количество минут:'))
print(m,'минут соответствует', m // 60, 'часам')
print('Останется минут:', m % 60)