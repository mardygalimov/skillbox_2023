while True:
  print('Введите местоположение фигуры', end = '\n')
  x = float(input('По горизонтали: '))
  y = float(input('По вертикали: '))
  h = int(x * 10)
  v = int(y * 10)
  if x < 0 or y < 0 or x > 0.8 or y > 0.8:
      print('Клетки с такой координатой не существует')
  else:
      print('Фигура находится в клетке: ', h, v)