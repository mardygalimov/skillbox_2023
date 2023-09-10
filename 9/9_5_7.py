#Напишите программу-дешифратор, которая расшифровала бы введённые сообщения.
# Пример:
# Введите зашифрованное сообщение: shacnidw.
# Расшифрованное сообщение: sandwich.
word = input('Введите слово для расшифровки: ')
#word = 'shacnidw'
count = 0
w1 = ''
w2 = ''

for symbol in word:
    count += 1
    if (count % 2 == 1):
        w1 += symbol
        #print('w1=', w1)
    else:
        sum2 = symbol + w2
        #print('w2=', w2)

print('Расшифрованое слово', w1 + w2)