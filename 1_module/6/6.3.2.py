number = int(input('Введите число:'))
last_num = 0
summ = 0
while number != 0:
    last_num = number % 10
    print(last_num)
    if last_num == 5:
        break
        print('Обнаружен разрыв')
    summ += last_num
    number //= 10
print('Расшифрованное число :', summ)