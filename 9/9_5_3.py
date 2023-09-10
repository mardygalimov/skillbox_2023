row = int(input("Введите кол-во рядов: "))
length = int(input("Введите кол-во сидений в ряде: "))
spase = int(input("Введите кол-во метров между рядами: "))

print('\nСцена\n')
for repiat in range(row):
  print('=' * length,'*' * spase, '=' * length)