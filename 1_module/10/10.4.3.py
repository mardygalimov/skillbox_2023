size = int(input('Введите N для построения матрицы: '))
for row in range(size+1):
    for col in range(size+1):
        if col == row:
          print(col, end = ' ')
        elif col >= row:
            print(col, end=' ')
    print()