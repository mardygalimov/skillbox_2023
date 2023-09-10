text = input('Введите текст: ')
count = 0
max_count = 0
buffer = 0
for symbol in text:
    if symbol == ' ' or symbol == '.':
        count = 0
        print('конец слова')
    else:
          count += 1
          print('count=', count)
          buffer = count
          if buffer > max_count:
               max_count = buffer
print('Самое длинное слово,', max_count, 'букв')
