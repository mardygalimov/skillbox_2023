badGradeCount = 0
for student in range(5):
    answer = input('Кто написал произведение? ')
    if (answer == 'Пушкин') or (answer == 'пушкин'):
        print('Верно!')
        break
    badGradeCount += 1
    print('Не верно! Два')
print('Двоечников: ', badGradeCount)