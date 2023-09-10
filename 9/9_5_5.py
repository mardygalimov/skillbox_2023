text = input('Введите текст: ')
count = 0
max_count = 0
buffer = 0
count_word = 0
for symbol in text:
    if symbol != ' ':
        count += 1
        if symbol == '.':
          count -= 1
#          print('найдена точка')
#          print('count=', count)
    else:
        if max_count < count:
          max_count = count
          count = 0
if max_count >= count:
    pass
else:
    max_count = count
print('Самое длинное слово,', max_count, 'букв')
