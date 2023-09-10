#север (клавиша W) , юг (клавиша S), запад (клавиша A) или восток (клавиша D)
x = 8 #max 15
y = 10 #max 20
while True:
  print('[Программа]:', 'Марсоход находится на позиции', x, ',', y, 'введите команду:')
  command = input('[Оператор]: ')
  if (command == 'W') and (x < 15):
      x += 1
  if (command == 'S') and (x > 1):
      x -= 1
  if (command == 'A') and (y > 1):
      y -= 1
  if (command == 'D') and (y < 20):
      y += 1