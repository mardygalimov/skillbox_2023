for row in range(21):
    for col in range(31):
        if row == 0:
            print('_', end = '')
        elif col == 0 or col == 30:
            print('|', end = '')
        else:
            print(' ', end= '')
    print()