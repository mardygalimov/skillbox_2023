print('Задача 7. Режем число на части')

# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных
z = int(input('Введите любое 4х значное число:'))
print(z // 1000)
print((z % 1000) // 100)
print((z % 100) // 10 )
print(z % 10)