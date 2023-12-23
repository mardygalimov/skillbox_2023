# Напишите программу,
# которая выводит «лестницу» из чисел, когда пользователь вводит число N
size = int(input('Введите число: '))
for col in range(1, size+1):
    for row in range(1, size+1):
        if col == row:
            print(col, end= ' ')
        elif col >= row:
            print(col, end= ' ')
    print()