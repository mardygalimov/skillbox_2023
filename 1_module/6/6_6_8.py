# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
# Напишите программу, которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.
low = 1
high = 100
while True:
    N = (low + high) // 2
    print('Твое число равно, больше или меньше числа', N, '?')
    answer = int(input('1 - равно, 2 - больше, 3 - меньше:'))
    if answer == 1:
        print('Я угадал!')
        break
    elif answer == 2:
        low = (N+1) #51
        N = (N+high+1)//2 #75
    else:
        high = (N-1) #74
        N = (low+high+1) //2
