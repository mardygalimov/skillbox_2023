for row in range(21):
    for col in range(31):
        if col == 0 or col == 30:
            print('|', end = '')
        elif row == 0 or row == 20:
            print('-', end = '')
        else:
            print(' ', end= '')
    print()