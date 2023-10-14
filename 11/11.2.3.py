#Индекс массы тела
w = float(input('Введите ваш вес: '))
h = float(input('Введите ваш рост: '))
bmi = round(w / h ** 2, 2)

if bmi < 18.5:
    print('У вас недобор веса')
elif bmi < 25:
    print('У вас нормальный вес')
elif bmi < 30:
    print('У вас избыточный вес')
else:
    print('У вас ожирение!')

print('Индекс маccы тела: ', bmi)