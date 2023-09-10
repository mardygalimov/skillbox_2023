# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Ему особенно понравилась книга «Преступление и наказание».
# Паоло решил найти самое длинное слово в этой книге,
# чтобы сравнить его с аналогом на своём языке.

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
