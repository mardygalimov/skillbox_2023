#5........5
#54......45
#543....345
#5432..2345
#5432112345
depth = int(input('Введите число для ландшафта: '))
for line in range(depth):
  for left_number in range(depth, depth - line - 1, -1):
      print(left_number, end='')
  point_count = 2 * (depth - line - 1)
  print('.' * point_count, end='')
  for right_number in range(depth-line, depth+1):
      print(right_number, end='')
  print()