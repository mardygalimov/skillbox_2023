count = 0
for candidate in range(10):
    word = input('Скажите слово: ')
    if word == 'Карамба' or word == 'карамба':
        print('Правильное слово! Добро пожаловать на борт - Пират!')
        count += 1
    else:
        print('Ты не Пират!')
print('На борт попадут ', count, ' из 10 кандидатов')