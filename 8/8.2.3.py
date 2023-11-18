# Деление клеток
cells = 1
all_time = int(input("Введите время эксперимента в часах: "))
for hour in range(1, all_time // 3 + 1):
  cells *= 2
  print('Прошло часов: ', hour * 3)
  print('Клеток: ', cells)
  print('Часов до конца эксперимента: ', all_time - hour *3)
  print()
print('Эксперимент завершен!')
