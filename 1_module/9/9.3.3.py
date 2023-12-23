bigSym = 0
smallSym = 0
text = input('Введите текст: ')

for let in text:
    if let == 'Ы':
        bigSym += 1
    if let == 'ы':
        smallSym += 1

print('Болших Ы: ', bigSym)
print('Маленьких ы: ', smallSym)