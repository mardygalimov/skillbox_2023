guest = int(input('Кубик Кости:'))
owner = int(input('Кубик владельца:'))
if guest >= owner:
    print('Разность:', guest - owner)
    print('Игрок платит')
else:
    print('Самма:', guest + owner)
    print('Владелец платит')
print('Игра окончена')